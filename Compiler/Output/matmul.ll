; ModuleID = 'matmul.c'
source_filename = "matmul.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

; Function Attrs: nofree norecurse nosync nounwind uwtable
define dso_local void @matmul([4 x i32]* nocapture noundef readonly %0, [4 x i32]* nocapture noundef readonly %1, [4 x i32]* nocapture noundef %2) local_unnamed_addr #0 {
  br label %4

4:                                                ; preds = %3, %7
  %5 = phi i64 [ 0, %3 ], [ %8, %7 ]
  br label %10

6:                                                ; preds = %7
  ret void

7:                                                ; preds = %13
  %8 = add nuw nsw i64 %5, 1
  %9 = icmp eq i64 %8, 4
  br i1 %9, label %6, label %4, !llvm.loop !5

10:                                               ; preds = %4, %13
  %11 = phi i64 [ 0, %4 ], [ %14, %13 ]
  %12 = getelementptr inbounds [4 x i32], [4 x i32]* %2, i64 %5, i64 %11
  store i32 0, i32* %12, align 4, !tbaa !8
  br label %16

13:                                               ; preds = %16
  %14 = add nuw nsw i64 %11, 1
  %15 = icmp eq i64 %14, 4
  br i1 %15, label %7, label %10, !llvm.loop !12

16:                                               ; preds = %10, %16
  %17 = phi i64 [ 0, %10 ], [ %25, %16 ]
  %18 = getelementptr inbounds [4 x i32], [4 x i32]* %0, i64 %5, i64 %17
  %19 = load i32, i32* %18, align 4, !tbaa !8
  %20 = getelementptr inbounds [4 x i32], [4 x i32]* %1, i64 %17, i64 %11
  %21 = load i32, i32* %20, align 4, !tbaa !8
  %22 = mul nsw i32 %21, %19
  %23 = load i32, i32* %12, align 4, !tbaa !8
  %24 = add nsw i32 %23, %22
  store i32 %24, i32* %12, align 4, !tbaa !8
  %25 = add nuw nsw i64 %17, 1
  %26 = icmp eq i64 %25, 4
  br i1 %26, label %13, label %16, !llvm.loop !13
}

; Function Attrs: nofree nosync nounwind readnone uwtable
define dso_local i32 @main() local_unnamed_addr #1 {
  ret i32 0
}

attributes #0 = { nofree norecurse nosync nounwind uwtable "frame-pointer"="none" "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { nofree nosync nounwind readnone uwtable "frame-pointer"="none" "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }

!llvm.module.flags = !{!0, !1, !2, !3}
!llvm.ident = !{!4}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 7, !"PIC Level", i32 2}
!2 = !{i32 7, !"PIE Level", i32 2}
!3 = !{i32 7, !"uwtable", i32 1}
!4 = !{!"Ubuntu clang version 14.0.0-1ubuntu1.1"}
!5 = distinct !{!5, !6, !7}
!6 = !{!"llvm.loop.mustprogress"}
!7 = !{!"llvm.loop.unroll.disable"}
!8 = !{!9, !9, i64 0}
!9 = !{!"int", !10, i64 0}
!10 = !{!"omnipotent char", !11, i64 0}
!11 = !{!"Simple C/C++ TBAA"}
!12 = distinct !{!12, !6, !7}
!13 = distinct !{!13, !6, !7}
