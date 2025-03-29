import subprocess
import os

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "Output"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def run_pipeline(input_file):

    """Runs the compilation process and returns the output machine code file path."""
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    llvm_ir = os.path.join(OUTPUT_FOLDER, f"{base_name}.ll")
    tac_file = os.path.join(OUTPUT_FOLDER, f"{base_name}.tac")
    lut_file = os.path.join(OUTPUT_FOLDER, f"{base_name}.lut")
    parallel_asm = os.path.join(OUTPUT_FOLDER, f"{base_name}_parallel.asm")
    final_mc = os.path.join(OUTPUT_FOLDER, f"{base_name}_parallel.mc")

    try:
        # Step 2: Generate LLVM IR
        subprocess.run(["clang", "-S", "-emit-llvm", "-O1", input_file, "-o", llvm_ir], check=True)

        # Step 3: Generate Three-Address Code
        m2r_file = os.path.join(OUTPUT_FOLDER, f"{base_name}_m2r.ll")
        subprocess.run(["opt", "-S", "-mem2reg", llvm_ir, "-o", m2r_file], check=True)
        subprocess.run(["python3", "Compiler/extract_tac.py", m2r_file], stdout=open(tac_file, "w"), check=True)

        # Step 4: Generate Lookup Table
        subprocess.run(["python3", "Compiler/create_lut.py", tac_file], stdout=open(lut_file, "w"), check=True)

        # Step 5: Generate Parallel Machine Code
        subprocess.run(["python3", "Compiler/generate_parallel.py", tac_file, "4"], check=True)

        # Step 6: Assemble to Machine Code
        subprocess.run(["python3", "Compiler/assembler.py", parallel_asm, final_mc], check=True)

        return final_mc  # Return path to compiled machine code
    except subprocess.CalledProcessError as e:
        return f"Error: {str(e)}"
