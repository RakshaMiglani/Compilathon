import sys

def generate_parallel_code(tac_file, size=4):
    # Read the TAC
    with open(tac_file, 'r') as f:
        tac = [line.strip() for line in f if line.strip()]
    
    # Generate parallel machine code
    output = []
    
    # Prologue
    output.append("; Parallel Matrix Multiplication")
    output.append("; Matrix size: {}x{}".format(size, size))
    output.append("")
    
    # Initialize parallel processing elements (PEs)
    output.append("; Initialize PEs")
    for i in range(size):
        for j in range(size):
            output.append(f"PE_{i}_{j}_INIT:")
            output.append(f"  LD R0, A_{i}_0  ; Load row {i} of A")
            output.append(f"  LD R1, B_0_{j}  ; Load column {j} of B")
            output.append("  MUL R2, R0, R1  ; Initial multiplication")
            output.append("  MOV R3, R2      ; Initialize accumulator")
            output.append("")
    
    # Parallel computation
    output.append("; Parallel computation")
    for k in range(1, size):
        for i in range(size):
            for j in range(size):
                output.append(f"PE_{i}_{j}_STEP_{k}:")
                output.append(f"  LD R0, A_{i}_{k}  ; Load A[{i}][{k}]")
                output.append(f"  LD R1, B_{k}_{j}  ; Load B[{k}][{j}]")
                output.append("  MUL R2, R0, R1    ; Multiply")
                output.append("  ADD R3, R3, R2     ; Accumulate")
                output.append("")
    
    # Store results
    output.append("; Store results")
    for i in range(size):
        for j in range(size):
            output.append(f"PE_{i}_{j}_STORE:")
            output.append(f"  ST C_{i}_{j}, R3  ; Store result in C[{i}][{j}]")
            output.append("")
    
    # Epilogue
    output.append("; Synchronization and exit")
    output.append("BARRIER")
    output.append("EXIT")
    
    return '\n'.join(output)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_parallel.py <tac_file> [size]")
        sys.exit(1)
    
    size = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    parallel_code = generate_parallel_code(sys.argv[1], size)
    
    with open("Output/matmul_parallel.asm", 'w') as f:
        f.write(parallel_code)
    
    print("Parallel machine code generated in matmul_parallel.asm")
