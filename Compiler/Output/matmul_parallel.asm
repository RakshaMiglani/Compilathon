; Parallel Matrix Multiplication
; Matrix size: 4x4

; Initialize PEs
PE_0_0_INIT:
  LD R0, A_0_0  ; Load row 0 of A
  LD R1, B_0_0  ; Load column 0 of B
  MUL R2, R0, R1  ; Initial multiplication
  MOV R3, R2      ; Initialize accumulator

PE_0_1_INIT:
  LD R0, A_0_0  ; Load row 0 of A
  LD R1, B_0_1  ; Load column 1 of B
  MUL R2, R0, R1  ; Initial multiplication
  MOV R3, R2      ; Initialize accumulator

PE_0_2_INIT:
  LD R0, A_0_0  ; Load row 0 of A
  LD R1, B_0_2  ; Load column 2 of B
  MUL R2, R0, R1  ; Initial multiplication
  MOV R3, R2      ; Initialize accumulator

PE_0_3_INIT:
  LD R0, A_0_0  ; Load row 0 of A
  LD R1, B_0_3  ; Load column 3 of B
  MUL R2, R0, R1  ; Initial multiplication
  MOV R3, R2      ; Initialize accumulator

PE_1_0_INIT:
  LD R0, A_1_0  ; Load row 1 of A
  LD R1, B_0_0  ; Load column 0 of B
  MUL R2, R0, R1  ; Initial multiplication
  MOV R3, R2      ; Initialize accumulator

PE_1_1_INIT:
  LD R0, A_1_0  ; Load row 1 of A
  LD R1, B_0_1  ; Load column 1 of B
  MUL R2, R0, R1  ; Initial multiplication
  MOV R3, R2      ; Initialize accumulator

PE_1_2_INIT:
  LD R0, A_1_0  ; Load row 1 of A
  LD R1, B_0_2  ; Load column 2 of B
  MUL R2, R0, R1  ; Initial multiplication
  MOV R3, R2      ; Initialize accumulator

PE_1_3_INIT:
  LD R0, A_1_0  ; Load row 1 of A
  LD R1, B_0_3  ; Load column 3 of B
  MUL R2, R0, R1  ; Initial multiplication
  MOV R3, R2      ; Initialize accumulator

PE_2_0_INIT:
  LD R0, A_2_0  ; Load row 2 of A
  LD R1, B_0_0  ; Load column 0 of B
  MUL R2, R0, R1  ; Initial multiplication
  MOV R3, R2      ; Initialize accumulator

PE_2_1_INIT:
  LD R0, A_2_0  ; Load row 2 of A
  LD R1, B_0_1  ; Load column 1 of B
  MUL R2, R0, R1  ; Initial multiplication
  MOV R3, R2      ; Initialize accumulator

PE_2_2_INIT:
  LD R0, A_2_0  ; Load row 2 of A
  LD R1, B_0_2  ; Load column 2 of B
  MUL R2, R0, R1  ; Initial multiplication
  MOV R3, R2      ; Initialize accumulator

PE_2_3_INIT:
  LD R0, A_2_0  ; Load row 2 of A
  LD R1, B_0_3  ; Load column 3 of B
  MUL R2, R0, R1  ; Initial multiplication
  MOV R3, R2      ; Initialize accumulator

PE_3_0_INIT:
  LD R0, A_3_0  ; Load row 3 of A
  LD R1, B_0_0  ; Load column 0 of B
  MUL R2, R0, R1  ; Initial multiplication
  MOV R3, R2      ; Initialize accumulator

PE_3_1_INIT:
  LD R0, A_3_0  ; Load row 3 of A
  LD R1, B_0_1  ; Load column 1 of B
  MUL R2, R0, R1  ; Initial multiplication
  MOV R3, R2      ; Initialize accumulator

PE_3_2_INIT:
  LD R0, A_3_0  ; Load row 3 of A
  LD R1, B_0_2  ; Load column 2 of B
  MUL R2, R0, R1  ; Initial multiplication
  MOV R3, R2      ; Initialize accumulator

PE_3_3_INIT:
  LD R0, A_3_0  ; Load row 3 of A
  LD R1, B_0_3  ; Load column 3 of B
  MUL R2, R0, R1  ; Initial multiplication
  MOV R3, R2      ; Initialize accumulator

; Parallel computation
PE_0_0_STEP_1:
  LD R0, A_0_1  ; Load A[0][1]
  LD R1, B_1_0  ; Load B[1][0]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_0_1_STEP_1:
  LD R0, A_0_1  ; Load A[0][1]
  LD R1, B_1_1  ; Load B[1][1]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_0_2_STEP_1:
  LD R0, A_0_1  ; Load A[0][1]
  LD R1, B_1_2  ; Load B[1][2]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_0_3_STEP_1:
  LD R0, A_0_1  ; Load A[0][1]
  LD R1, B_1_3  ; Load B[1][3]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_1_0_STEP_1:
  LD R0, A_1_1  ; Load A[1][1]
  LD R1, B_1_0  ; Load B[1][0]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_1_1_STEP_1:
  LD R0, A_1_1  ; Load A[1][1]
  LD R1, B_1_1  ; Load B[1][1]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_1_2_STEP_1:
  LD R0, A_1_1  ; Load A[1][1]
  LD R1, B_1_2  ; Load B[1][2]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_1_3_STEP_1:
  LD R0, A_1_1  ; Load A[1][1]
  LD R1, B_1_3  ; Load B[1][3]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_2_0_STEP_1:
  LD R0, A_2_1  ; Load A[2][1]
  LD R1, B_1_0  ; Load B[1][0]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_2_1_STEP_1:
  LD R0, A_2_1  ; Load A[2][1]
  LD R1, B_1_1  ; Load B[1][1]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_2_2_STEP_1:
  LD R0, A_2_1  ; Load A[2][1]
  LD R1, B_1_2  ; Load B[1][2]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_2_3_STEP_1:
  LD R0, A_2_1  ; Load A[2][1]
  LD R1, B_1_3  ; Load B[1][3]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_3_0_STEP_1:
  LD R0, A_3_1  ; Load A[3][1]
  LD R1, B_1_0  ; Load B[1][0]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_3_1_STEP_1:
  LD R0, A_3_1  ; Load A[3][1]
  LD R1, B_1_1  ; Load B[1][1]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_3_2_STEP_1:
  LD R0, A_3_1  ; Load A[3][1]
  LD R1, B_1_2  ; Load B[1][2]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_3_3_STEP_1:
  LD R0, A_3_1  ; Load A[3][1]
  LD R1, B_1_3  ; Load B[1][3]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_0_0_STEP_2:
  LD R0, A_0_2  ; Load A[0][2]
  LD R1, B_2_0  ; Load B[2][0]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_0_1_STEP_2:
  LD R0, A_0_2  ; Load A[0][2]
  LD R1, B_2_1  ; Load B[2][1]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_0_2_STEP_2:
  LD R0, A_0_2  ; Load A[0][2]
  LD R1, B_2_2  ; Load B[2][2]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_0_3_STEP_2:
  LD R0, A_0_2  ; Load A[0][2]
  LD R1, B_2_3  ; Load B[2][3]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_1_0_STEP_2:
  LD R0, A_1_2  ; Load A[1][2]
  LD R1, B_2_0  ; Load B[2][0]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_1_1_STEP_2:
  LD R0, A_1_2  ; Load A[1][2]
  LD R1, B_2_1  ; Load B[2][1]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_1_2_STEP_2:
  LD R0, A_1_2  ; Load A[1][2]
  LD R1, B_2_2  ; Load B[2][2]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_1_3_STEP_2:
  LD R0, A_1_2  ; Load A[1][2]
  LD R1, B_2_3  ; Load B[2][3]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_2_0_STEP_2:
  LD R0, A_2_2  ; Load A[2][2]
  LD R1, B_2_0  ; Load B[2][0]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_2_1_STEP_2:
  LD R0, A_2_2  ; Load A[2][2]
  LD R1, B_2_1  ; Load B[2][1]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_2_2_STEP_2:
  LD R0, A_2_2  ; Load A[2][2]
  LD R1, B_2_2  ; Load B[2][2]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_2_3_STEP_2:
  LD R0, A_2_2  ; Load A[2][2]
  LD R1, B_2_3  ; Load B[2][3]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_3_0_STEP_2:
  LD R0, A_3_2  ; Load A[3][2]
  LD R1, B_2_0  ; Load B[2][0]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_3_1_STEP_2:
  LD R0, A_3_2  ; Load A[3][2]
  LD R1, B_2_1  ; Load B[2][1]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_3_2_STEP_2:
  LD R0, A_3_2  ; Load A[3][2]
  LD R1, B_2_2  ; Load B[2][2]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_3_3_STEP_2:
  LD R0, A_3_2  ; Load A[3][2]
  LD R1, B_2_3  ; Load B[2][3]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_0_0_STEP_3:
  LD R0, A_0_3  ; Load A[0][3]
  LD R1, B_3_0  ; Load B[3][0]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_0_1_STEP_3:
  LD R0, A_0_3  ; Load A[0][3]
  LD R1, B_3_1  ; Load B[3][1]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_0_2_STEP_3:
  LD R0, A_0_3  ; Load A[0][3]
  LD R1, B_3_2  ; Load B[3][2]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_0_3_STEP_3:
  LD R0, A_0_3  ; Load A[0][3]
  LD R1, B_3_3  ; Load B[3][3]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_1_0_STEP_3:
  LD R0, A_1_3  ; Load A[1][3]
  LD R1, B_3_0  ; Load B[3][0]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_1_1_STEP_3:
  LD R0, A_1_3  ; Load A[1][3]
  LD R1, B_3_1  ; Load B[3][1]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_1_2_STEP_3:
  LD R0, A_1_3  ; Load A[1][3]
  LD R1, B_3_2  ; Load B[3][2]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_1_3_STEP_3:
  LD R0, A_1_3  ; Load A[1][3]
  LD R1, B_3_3  ; Load B[3][3]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_2_0_STEP_3:
  LD R0, A_2_3  ; Load A[2][3]
  LD R1, B_3_0  ; Load B[3][0]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_2_1_STEP_3:
  LD R0, A_2_3  ; Load A[2][3]
  LD R1, B_3_1  ; Load B[3][1]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_2_2_STEP_3:
  LD R0, A_2_3  ; Load A[2][3]
  LD R1, B_3_2  ; Load B[3][2]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_2_3_STEP_3:
  LD R0, A_2_3  ; Load A[2][3]
  LD R1, B_3_3  ; Load B[3][3]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_3_0_STEP_3:
  LD R0, A_3_3  ; Load A[3][3]
  LD R1, B_3_0  ; Load B[3][0]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_3_1_STEP_3:
  LD R0, A_3_3  ; Load A[3][3]
  LD R1, B_3_1  ; Load B[3][1]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_3_2_STEP_3:
  LD R0, A_3_3  ; Load A[3][3]
  LD R1, B_3_2  ; Load B[3][2]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

PE_3_3_STEP_3:
  LD R0, A_3_3  ; Load A[3][3]
  LD R1, B_3_3  ; Load B[3][3]
  MUL R2, R0, R1    ; Multiply
  ADD R3, R3, R2     ; Accumulate

; Store results
PE_0_0_STORE:
  ST C_0_0, R3  ; Store result in C[0][0]

PE_0_1_STORE:
  ST C_0_1, R3  ; Store result in C[0][1]

PE_0_2_STORE:
  ST C_0_2, R3  ; Store result in C[0][2]

PE_0_3_STORE:
  ST C_0_3, R3  ; Store result in C[0][3]

PE_1_0_STORE:
  ST C_1_0, R3  ; Store result in C[1][0]

PE_1_1_STORE:
  ST C_1_1, R3  ; Store result in C[1][1]

PE_1_2_STORE:
  ST C_1_2, R3  ; Store result in C[1][2]

PE_1_3_STORE:
  ST C_1_3, R3  ; Store result in C[1][3]

PE_2_0_STORE:
  ST C_2_0, R3  ; Store result in C[2][0]

PE_2_1_STORE:
  ST C_2_1, R3  ; Store result in C[2][1]

PE_2_2_STORE:
  ST C_2_2, R3  ; Store result in C[2][2]

PE_2_3_STORE:
  ST C_2_3, R3  ; Store result in C[2][3]

PE_3_0_STORE:
  ST C_3_0, R3  ; Store result in C[3][0]

PE_3_1_STORE:
  ST C_3_1, R3  ; Store result in C[3][1]

PE_3_2_STORE:
  ST C_3_2, R3  ; Store result in C[3][2]

PE_3_3_STORE:
  ST C_3_3, R3  ; Store result in C[3][3]

; Synchronization and exit
BARRIER
EXIT