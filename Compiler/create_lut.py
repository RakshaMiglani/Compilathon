import sys
from collections import defaultdict

def analyze_tac(tac_file):
    op_counts = defaultdict(int)
    with open(tac_file, 'r') as f:
        for line in f:
            if '=' in line:
                # Extract the operation
                rhs = line.split('=')[1].strip()
                if ' ' in rhs:
                    op = rhs.split(' ')[0].strip()
                    op_counts[op] += 1
    
    return op_counts

def generate_lut(op_counts):
    # Simple ISA mapping - this would be customized for your actual ISA
    lut = {
        'add': 'ADD',
        'sub': 'SUB',
        'mul': 'MUL',
        'load': 'LD',
        'store': 'ST',
        'icmp': 'CMP',
        'br': 'BR',
        'getelementptr': 'GEP',
        'sext': 'SEXT',
        'trunc': 'TRUNC',
        'phi': 'PHI'
    }
    
    # Generate frequency report
    print("Operation Frequency:")
    for op, count in op_counts.items():
        print(f"{op}: {count}")
    
    print("\nLookup Table:")
    for llvm_op, isa_op in lut.items():
        print(f"{llvm_op.ljust(15)} -> {isa_op}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python create_lut.py <tac_file>")
        sys.exit(1)
    
    op_counts = analyze_tac(sys.argv[1])
    generate_lut(op_counts)
