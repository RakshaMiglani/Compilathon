import re
import sys

# pPIM ISA definition based on the paper
isa = {
    # Memory operations
    'LD':   '0001',    # Load from memory
    'ST':   '0010',    # Store to memory
    # Arithmetic operations
    'ADD':  '0011',    # Add
    'SUB':  '0100',    # Subtract
    'MUL':  '0101',    # Multiply
    'MAC':  '0110',    # Multiply-accumulate
    # Data movement
    'MOV':  '0111',    # Move
    # Control flow
    'BR':   '1000',    # Branch
    'CMP':  '1001',    # Compare
    # pPIM specific
    'PROG': '1010',    # Program LUT
    'EXE':  '1011',    # Execute operation
    'END':  '1100',    # End operation (replaces EXIT)
    'HALT': '1100',    # Alternative for END
    'BARRIER': '1101', # Synchronization
    'NOP':  '1110',    # No operation
    # Special
    'SYNC': '1111'     # Synchronize
}

# Register mapping (expanded for pPIM)
registers = {
    'R0': '0000', 'R1': '0001', 'R2': '0010', 'R3': '0011',
    'R4': '0100', 'R5': '0101', 'R6': '0110', 'R7': '0111',
    'R8': '1000', 'R9': '1001', 'R10': '1010', 'R11': '1011',
    'R12': '1100', 'R13': '1101', 'R14': '1110', 'R15': '1111',
    # Special registers for pPIM
    'A': '0000', 'AH': '0001', 'AL': '0010',
    'B': '0011', 'BH': '0100', 'BL': '0101',
    'C': '0110', 'ACC': '0111', 'TMP': '1000'
}

def clean_line(line):
    """Remove comments and whitespace"""
    line = line.split(';')[0].strip()
    return line

def parse_operand(op):
    """Parse operand that could be register, immediate, or label"""
    if op in registers:
        return (True, registers[op])  # Is register
    elif op.isdigit():
        return (False, format(int(op), '016b'))  # Immediate value
    else:
        return (False, op)  # Presume label to be resolved later

def assemble_line(line, labels=None):
    line = clean_line(line)
    if not line:
        return None
    
    # Handle labels
    if line.endswith(':'):
        return (line[:-1], None)  # Return label name
    
    parts = [p.strip() for p in re.split(r'[,\s]+', line) if p.strip()]
    if not parts:
        return None
    
    op = parts[0].upper()
    
    # Map EXIT to END (per pPIM paper)
    if op == 'EXIT':
        op = 'END'
    
    if op not in isa:
        raise ValueError(f"Unknown instruction: {op}")
    
    binary = isa[op]
    
    # Instruction encoding
    if op in ['LD', 'ST']:
        # Format: OP dest, src
        if len(parts) < 3:
            raise ValueError(f"Invalid {op} instruction format: {line}")
        
        dest = parse_operand(parts[1])
        src = parse_operand(parts[2])
        
        if dest[0]:  # If destination is register
            binary += dest[1]
        else:
            binary += '0000'  # Default register if immediate
        
        binary += src[1][-12:]  # Use 12 bits for address/immediate
    
    elif op == 'PROG':
        # Format: PROG cores=N func=NAME
        cores = 1
        func = '0'*8
        for param in parts[1:]:
            if '=' in param:
                key, val = param.split('=')
                if key == 'cores':
                    cores = int(val)
                elif key == 'func':
                    func = format(hash(val) % 256, '08b')  # Simple hash
        binary += format(cores, '04b') + func
    
    elif op == 'EXE':
        # Format: EXE op=NAME [in1=REG] [in2=REG] [out=REG] [steps=N]
        opcode = '0000'
        in1 = '0000'
        in2 = '0000'
        out = '0000'
        steps = '0000'
        
        for param in parts[1:]:
            if '=' in param:
                key, val = param.split('=')
                if key == 'op':
                    opcode = format(hash(val) % 16, '04b')
                elif key == 'in1':
                    in1 = registers.get(val, '0000')
                elif key == 'in2':
                    in2 = registers.get(val, '0000')
                elif key == 'out':
                    out = registers.get(val, '0000')
                elif key == 'steps':
                    steps = format(int(val), '04b')
        
        binary += opcode + in1 + in2 + out + steps
    
    elif op in ['END', 'HALT', 'BARRIER', 'NOP', 'SYNC']:
        binary += '0'*12
    
    elif op in ['ADD', 'SUB', 'MUL', 'MAC', 'MOV']:
        # Format: OP dest, src1, [src2]
        if len(parts) < 3:
            raise ValueError(f"Invalid {op} instruction format: {line}")
        
        dest = parse_operand(parts[1])
        src1 = parse_operand(parts[2])
        src2 = parse_operand(parts[3]) if len(parts) > 3 else (True, '0000')
        
        if not (dest[0] and src1[0] and src2[0]):
            raise ValueError(f"{op} instruction requires register operands: {line}")
        
        binary += dest[1] + src1[1] + src2[1]
    
    elif op == 'BR':
        # Format: BR [cond,] target
        if len(parts) < 2:
            raise ValueError(f"Invalid BR instruction format: {line}")
        
        if len(parts) >= 3 and parts[1].upper() == 'COND':
            # Conditional branch
            cond = parse_operand(parts[2])
            target = parse_operand(parts[3])
            binary += cond[1] + '0'*4 + target[1][-8:]
        else:
            # Unconditional branch
            target = parse_operand(parts[1])
            binary += '0000' + target[1][-12:]
    
    return (None, binary)  # No label, just binary

def assemble_file(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    # First pass: collect labels
    labels = {}
    address = 0
    for line in lines:
        line = clean_line(line)
        if not line:
            continue
        
        if line.endswith(':'):
            label = line[:-1]
            labels[label] = format(address, '012b')
        else:
            address += 1
    
    # Second pass: generate machine code
    machine_code = []
    for line in lines:
        line = clean_line(line)
        if not line:
            continue
        
        try:
            label, binary = assemble_line(line, labels)
            if label:
                machine_code.append(f"{label}:")
            elif binary:
                # Replace label references
                for lbl, addr in labels.items():
                    binary = binary.replace(lbl, addr)
                machine_code.append(f"{binary} ; {line}")
        except ValueError as e:
            print(f"Error in line: {line}\n{str(e)}")
            sys.exit(1)
    
    with open(output_file, 'w') as f:
        f.write('\n'.join(machine_code))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python assembler.py <input.asm> <output.mc>")
        sys.exit(1)
    
    try:
        assemble_file(sys.argv[1], sys.argv[2])
        print(f"Successfully assembled to {sys.argv[2]}")
    except Exception as e:
        print(f"Assembly failed: {str(e)}")
        sys.exit(1)