import re
import sys
from collections import defaultdict

# pPIM ISA operations mapping
PPIM_OPS = {
    # Arithmetic operations
    'add': 'ADD',
    'sub': 'SUB',
    'mul': 'MUL',
    'mac': 'MAC',
    # Memory operations
    'load': 'LD',
    'store': 'ST',
    # Bitwise operations
    'and': 'AND',
    'or': 'OR',
    'xor': 'XOR',
    'not': 'NOT',
    # Control flow
    'br': 'BR',
    # Special pPIM operations
    'prog': 'PROG',    # Program LUT
    'exec': 'EXE',     # Execute operation
    'end': 'END'       # End operation
}

def extract_tac(llvm_file):
    with open(llvm_file, 'r') as f:
        content = f.read()
    
    # Extract basic blocks and instructions
    functions = re.findall(r'define [^{]+{(.+?)}', content, re.DOTALL)
    
    tac = []
    current_operation = None
    operation_steps = defaultdict(list)
    
    for func in functions:
        # Split into instructions
        lines = [line.strip() for line in func.split('\n') if line.strip()]
        
        for line in lines:
            # Skip labels and metadata
            if line.startswith(';') or line.endswith(':'):
                continue
                
            # Simplify the instruction
            instr = line.split(';')[0].strip()
            
            # Convert LLVM IR to pPIM-compatible TAC
            if '=' in instr:
                lhs, rhs = instr.split('=', 1)
                lhs = lhs.strip()
                rhs = rhs.strip()
                
                # Handle memory operations
                if 'load' in rhs:
                    # Format: %var = load type, type* %ptr
                    ptr = rhs.split('*')[-1].strip()
                    tac.append(f"LD {lhs}, {ptr}")
                    
                elif 'store' in rhs:
                    # Format: store type %val, type* %ptr
                    val, ptr = rhs.replace('store', '').split(',')[:2]
                    val = val.strip().split()[-1]
                    ptr = ptr.strip().split('*')[-1]
                    tac.append(f"ST {ptr}, {val}")
                    
                # Handle arithmetic operations
                elif any(op in rhs for op in ['add', 'sub', 'mul']):
                    op = re.search(r'(add|sub|mul)', rhs).group(1)
                    operands = rhs.replace(op, '').strip().split(',')
                    op1 = operands[0].strip()
                    op2 = operands[1].strip().split(' ')[0]
                    tac.append(f"{PPIM_OPS[op]} {lhs}, {op1}, {op2}")
                    
                # Handle getelementptr (array access)
                elif 'getelementptr' in rhs:
                    # Format: %var = getelementptr type, type* %ptr, type %idx
                    ptr = rhs.split('*')[-1].split(',')[0].strip()
                    idx = rhs.split(',')[-1].strip().split(' ')[0]
                    tac.append(f"GEP {lhs}, {ptr}, {idx}")
                    
            # Handle branches
            elif 'br' in instr:
                # Format: br i1 %cond, label %true, label %false
                if ',' in instr:  # Conditional branch
                    parts = instr.replace('br', '').strip().split(',')
                    cond = parts[0].strip().split(' ')[-1]
                    true_label = parts[1].strip().replace('label', '').strip()
                    false_label = parts[2].strip().replace('label', '').strip()
                    tac.append(f"BR {cond}, {true_label}, {false_label}")
                else:  # Unconditional branch
                    label = instr.replace('br', '').strip().replace('label', '').strip()
                    tac.append(f"BR {label}")
                    
            # Handle function calls (map to pPIM operations)
            elif 'call' in instr:
                # Format: call return_type @func(args...)
                func_name = re.search(r'@(\w+)', instr).group(1)
                if func_name == 'matmul':
                    # Special handling for matrix multiplication
                    args = re.findall(r'%(\w+)', instr)
                    A, B, C = args[:3]
                    
                    # Add PROG instruction to program LUTs for MAC
                    tac.append("PROG cores=9 func=MAC")
                    
                    # Add memory loads
                    tac.append(f"LD bufA, {A}")
                    tac.append(f"LD bufB, {B}")
                    
                    # Add EXE instruction for matrix multiplication
                    tac.append("EXE op=MATMUL in1=bufA in2=bufB out=bufC steps=8")
                    
                    # Add memory store
                    tac.append(f"ST {C}, bufC")
                    
                    # Add END instruction
                    tac.append("END")
    
    return tac

def optimize_for_ppim(tac):
    """
    Optimize TAC for pPIM architecture:
    1. Group operations into PROG/EXE/END blocks
    2. Identify parallelizable operations
    3. Map to 4-bit/8-bit processing
    """
    optimized = []
    current_block = []
    
    for instr in tac:
        # Check for memory operations that can be parallelized
        if instr.startswith('LD') or instr.startswith('ST'):
            # In pPIM, we can perform parallel memory ops
            optimized.append(f"PARALLEL {instr}")
        elif 'MAC' in instr or 'MATMUL' in instr:
            # These are already pPIM-optimized
            optimized.append(instr)
        else:
            # For other operations, group into EXE blocks
            if not current_block:
                current_block.append("PROG cores=1 func=ALU")
                current_block.append("EXE op=BLOCK")
            
            current_block.append(instr)
            
            # End block after certain number of instructions
            if len(current_block) >= 4:  # pPIM processes 4 ops at once
                current_block.append("END")
                optimized.extend(current_block)
                current_block = []
    
    if current_block:
        current_block.append("END")
        optimized.extend(current_block)
    
    return optimized

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_tac_ppim.py <llvm_file>")
        sys.exit(1)
    
    tac = extract_tac(sys.argv[1])
    optimized_tac = optimize_for_ppim(tac)
    
    with open('matmul_ppim.tac', 'w') as f:
        for i, instr in enumerate(optimized_tac):
            f.write(f"{i+1}: {instr}\n")
    
    print("pPIM-optimized TAC generated in matmul_ppim.tac")