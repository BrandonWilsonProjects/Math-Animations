from manim import *
import numpy as np

class PerfectSimilarity(Scene):
    def construct(self):

        # Title
        title = Text("The Power of Similarity in Geometry", font_size=40)
        title.to_edge(UP)
        self.play(FadeIn(title))

        # Triangle A
        A = np.array([-3, -1, 0])
        B = np.array([-1, 2, 0])
        C = np.array([2, -1, 0])
        triangleA = Polygon(A, B, C, color=BLUE, stroke_width=4)

        labelA = Text("Triangle A", font_size=28, color=BLUE).next_to(triangleA, DOWN)
        self.play(Create(triangleA), FadeIn(labelA))
        self.wait(1)

        # Similarity transform parameters
        k = 0.55
        shift_vec = np.array([4, 0, 0])

        # Forward and inverse transforms
        def sim_forward(p):
            return k * p + shift_vec

        def sim_inverse(p):
            return (p - shift_vec) / k

        # Triangle B — EXACT similarity transform
        triangleB = triangleA.copy()
        triangleB.apply_function(sim_forward)
        triangleB.set_color(YELLOW)

        labelB = Text("Triangle B", font_size=28, color=YELLOW).next_to(triangleB, DOWN)
        self.play(Create(triangleB), FadeIn(labelB))
        self.wait(1)

        # Angle arc helper
        def angle_arc(p1, v, p2, radius=0.3, color=WHITE):
            v1 = p1 - v
            v2 = p2 - v
            a1 = np.arctan2(v1[1], v1[0])
            a2 = np.arctan2(v2[1], v2[0])
            return Arc(
                start_angle=a1,
                angle=a2 - a1,
                radius=radius,
                arc_center=v,
                color=color
            )

        # Angle arcs for Triangle A
        arcA_A = angle_arc(C, A, B, radius=0.35, color=BLUE)
        arcB_A = angle_arc(A, B, C, radius=0.35, color=BLUE)
        arcC_A = angle_arc(B, C, A, radius=0.35, color=BLUE)

        # Triangle B angle arcs using transformed coordinates
        A2 = sim_forward(A)
        B2 = sim_forward(B)
        C2 = sim_forward(C)

        arcA_B = angle_arc(C2, A2, B2, radius=0.22, color=YELLOW)
        arcB_B = angle_arc(A2, B2, C2, radius=0.22, color=YELLOW)
        arcC_B = angle_arc(B2, C2, A2, radius=0.22, color=YELLOW)

        self.play(
            Create(arcA_A), Create(arcB_A), Create(arcC_A),
            Create(arcA_B), Create(arcB_B), Create(arcC_B),
            run_time=1.5
        )
        self.wait(1)

        # Info text
        info = Text("Triangle B is an exact scaled copy of Triangle A", font_size=28)
        info.to_edge(DOWN)
        self.play(FadeIn(info))
        self.wait(1)

        # 🔥 THE KEY FIX: use apply_function for inverse transform
        self.play(
            triangleB.animate.apply_function(sim_inverse),
            arcA_B.animate.apply_function(sim_inverse),
            arcB_B.animate.apply_function(sim_inverse),
            arcC_B.animate.apply_function(sim_inverse),
            run_time=2
        )

        self.wait(2)
