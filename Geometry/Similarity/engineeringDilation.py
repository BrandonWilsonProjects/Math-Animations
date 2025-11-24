from manim import *
import numpy as np

class EngineeringDilationFixed(Scene):
    def construct(self):

        BLUEPRINT = "#00CCFF"
        GHOST = "#66B2FF"

        # ----------------------------------------------------
        # TITLE
        # ----------------------------------------------------
        title = Text("Engineering with Dilation", font_size=44)
        subtitle = Text("How Scaling Completes Engineering Tasks", font_size=28).next_to(title, DOWN)

        self.play(FadeIn(title), FadeIn(subtitle))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))

        # ====================================================
        # =============== TASK 1 – BRIDGE TRUSS ===============
        # ====================================================

        task1 = Text("Task 1: Scale a Truss to Fit a Larger Bridge Span", font_size=36)
        task1.to_edge(UP)
        self.play(FadeIn(task1))
        self.wait(1)

        # ----------------------------------------------------
        # DEFINE TRUSS POINTS
        # ----------------------------------------------------
        A = np.array([-3, -1, 0])
        B = np.array([-1, 1.5, 0])
        C = np.array([1, -1, 0])
        D = np.array([3, 1.5, 0])
        E = np.array([5, -1, 0])

        # SHIFT EVERYTHING LEFT SO DILATION STAYS INSIDE FRAME
        SHIFT = np.array([-3, 0, 0])
        A, B, C, D, E = [p + SHIFT for p in (A, B, C, D, E)]

        # ----------------------------------------------------
        # ORIGINAL TRUSS
        # ----------------------------------------------------
        truss_segments = [
            Line(A, B), Line(B, C), Line(C, D), Line(D, E),
            Line(A, C), Line(B, D), Line(C, E)
        ]
        truss = VGroup(*truss_segments).set_stroke(BLUEPRINT, 3)

        label_original = Text("Original Truss (short span)", font_size=24, color=BLUEPRINT)
        label_original.next_to(truss, DOWN)

        self.play(Create(truss), FadeIn(label_original))
        self.wait(1)

        # ----------------------------------------------------
        # GHOST TRUSS (TARGET)
        # ----------------------------------------------------
        k = 1.4
        anchor = A  # anchor also shifted

        def dilate1(p):
            return anchor + k * (p - anchor)

        ghost_segments = [
            Line(dilate1(A), dilate1(B)),
            Line(dilate1(B), dilate1(C)),
            Line(dilate1(C), dilate1(D)),
            Line(dilate1(D), dilate1(E)),
            Line(dilate1(A), dilate1(C)),
            Line(dilate1(B), dilate1(D)),
            Line(dilate1(C), dilate1(E)),
        ]

        ghost_truss = VGroup(*ghost_segments).set_stroke(GHOST, 2, opacity=0.4)
        ghost_label = Text("Required Longer Truss (target)", font_size=20, color=GHOST)
        ghost_label.next_to(ghost_truss, UP)

        self.play(FadeIn(ghost_truss), FadeIn(ghost_label))
        self.wait(2)

        # ----------------------------------------------------
        # PERFECTLY MATCH DILATION TO GHOST
        # ----------------------------------------------------
        self.play(
            truss.animate.apply_function(dilate1),
            run_time=3
        )
        self.wait(2)

        success1 = Text("Dilation Complete – Perfect Alignment", font_size=30, color=GREEN).to_edge(DOWN)
        self.play(FadeIn(success1))
        self.wait(2)

        self.play(
            FadeOut(truss), FadeOut(ghost_truss), FadeOut(success1),
            FadeOut(label_original), FadeOut(ghost_label), FadeOut(task1)
        )
        self.wait(1)

        # ====================================================
        # =============== TASK 2 – MACHINE PART ===============
        # ====================================================

        task2 = Text("Task 2: Scale a Machine Part for a Larger Assembly", font_size=36)
        task2.to_edge(UP)
        self.play(FadeIn(task2))
        self.wait(1)

        # ----------------------------------------------------
        # MACHINE PART POINTS (SHIFTED UP TO AVOID LABEL OVERLAP)
        # ----------------------------------------------------
        P1 = np.array([-2, 1, 0])
        P2 = np.array([-1, 2, 0])
        P3 = np.array([1, 2, 0])
        P4 = np.array([2, 1, 0])
        P5 = np.array([1, -0.5, 0])
        P6 = np.array([-1, -0.5, 0])

        part_segments = [
            Line(P1, P2), Line(P2, P3), Line(P3, P4),
            Line(P4, P5), Line(P5, P6), Line(P6, P1)
        ]

        part = VGroup(*part_segments).set_stroke(ORANGE, 4)

        # TEXT MOVED **FURTHER DOWN** SO IT NEVER GETS OVERLAPPED
        label_part = Text("Original Part", font_size=24, color=ORANGE)
        label_part.next_to(part, DOWN * 2)

        self.play(Create(part), FadeIn(label_part))
        self.wait(1)
        self.play(FadeOut(label_part))

        # ----------------------------------------------------
        # TARGET GHOST PART
        # ----------------------------------------------------
        label_part_2 = Text("Dilated Part (Scaled to Parameters)", font_size=24, color=ORANGE)
        label_part_2.next_to(part, DOWN * 3)
        self.play(FadeIn(label_part_2))

        k2 = 1.3
        center2 = np.array([0, 1, 0])   # ⭐ scale upward, away from text

        def dilate2(p):
            return center2 + k2 * (p - center2)

        ghost2_segments = [
            Line(dilate2(P1), dilate2(P2)),
            Line(dilate2(P2), dilate2(P3)),
            Line(dilate2(P3), dilate2(P4)),
            Line(dilate2(P4), dilate2(P5)),
            Line(dilate2(P5), dilate2(P6)),
            Line(dilate2(P6), dilate2(P1)),
        ]

        ghost2 = VGroup(*ghost2_segments).set_stroke(WHITE, 2, opacity=0.35)
        ghost2_label = Text("Larger Assembly Template", font_size=24)
        ghost2_label.next_to(ghost2, UP)

        self.play(FadeIn(ghost2), FadeIn(ghost2_label))
        self.wait(2)

        # ----------------------------------------------------
        # DILATE PART WITHOUT TOUCHING TEXT
        # ----------------------------------------------------
        self.play(
            part.animate.apply_function(dilate2),
            run_time=3
        )
        self.wait(2)

        success2 = Text("Scaled to Assembly Specifications", font_size=30, color=GREEN).to_edge(DOWN)
        self.play(FadeIn(success2))
        self.wait(2)
