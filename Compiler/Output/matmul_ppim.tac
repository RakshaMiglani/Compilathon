1: PROG cores=1 func=ALU
2: EXE op=BLOCK
3: BR %4
4: BR %10
5: END
6: PROG cores=1 func=ALU
7: EXE op=BLOCK
8: ADD %8, nuw nsw i64 %5, 1
9: BR %9, %6, %4
10: END
11: PROG cores=1 func=ALU
12: EXE op=BLOCK
13: GEP %12, %2, i64
14: BR %16
15: END
16: PROG cores=1 func=ALU
17: EXE op=BLOCK
18: ADD %14, nuw nsw i64 %11, 1
19: BR %15, %7, %10
20: END
21: PARALLEL LD %19, %18, align 4, !tbaa !8
22: PROG cores=1 func=ALU
23: EXE op=BLOCK
24: GEP %18, %0, i64
25: GEP %20, %1, i64
26: END
27: PARALLEL LD %21, %20, align 4, !tbaa !8
28: PARALLEL LD %23, %12, align 4, !tbaa !8
29: PROG cores=1 func=ALU
30: EXE op=BLOCK
31: MUL %22, nsw i32 %21, %19
32: ADD %24, nsw i32 %23, %22
33: END
34: PROG cores=1 func=ALU
35: EXE op=BLOCK
36: ADD %25, nuw nsw i64 %17, 1
37: BR %26, %13, %16
38: END
