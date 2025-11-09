from manim import *
import numpy as np

class AngleBisector(Scene):
    def construct(self):
        # Title
        title = Text("Angle Bisector", font_size=40, color=YELLOW).to_edge(UP)
        self.play(Write(title))

        # Triangle vertices
        A = np.array([-3, -1, 0])
        B = np.array([3, -1, 0])
        C = np.array([0, 2, 0])

        # Draw triangle
        triangle = Polygon(A, B, C, color=WHITE)
        self.play(Create(triangle))

        # Dots and labels
        dot_A = Dot(A, color=RED); label_A = Text("A", font_size=24, color=RED).next_to(dot_A, LEFT)
        dot_B = Dot(B, color=RED); label_B = Text("B", font_size=24, color=RED).next_to(dot_B, RIGHT)
        dot_C = Dot(C, color=RED); label_C = Text("C", font_size=24, color=RED).next_to(dot_C, UP)
        self.play(FadeIn(dot_A), Write(label_A),
                  FadeIn(dot_B), Write(label_B),
                  FadeIn(dot_C), Write(label_C))

        # --- Compute intersection of bisector with BC ---
        # Unit vectors along AB and AC
        uAB = (B - A) / np.linalg.norm(B - A)
        uAC = (C - A) / np.linalg.norm(C - A)
        bisector_dir = (uAB + uAC) / np.linalg.norm(uAB + uAC)

        # Solve for intersection of A + t*bisector_dir with BC
        # Line BC: B + s*(C-B)
        M = np.array([[bisector_dir[0], -(C-B)[0]],
                      [bisector_dir[1], -(C-B)[1]]])
        rhs = np.array([B[0]-A[0], B[1]-A[1]])
        t, s = np.linalg.solve(M, rhs)
        D = A + t*bisector_dir  # intersection point

        # Draw bisector
        bisector = Line(A, D, color=YELLOW)
        self.play(Create(bisector))

        # Mark intersection D
        dot_D = Dot(D, color=BLUE)
        label_D = Text("D", font_size=24, color=BLUE).next_to(dot_D, DOWN)
        self.play(FadeIn(dot_D), Write(label_D))

        # Interior angle arcs
        arc1 = Angle(Line(A, B), Line(A, D), radius=0.5, other_angle=False, color=GREEN)
        arc2 = Angle(Line(A, D), Line(A, C), radius=0.7, other_angle=False, color=GREEN)
        self.play(Create(arc1), Create(arc2))

        # Closing text
        conclusion = Text("The angle bisector divides ∠A into two equal parts", 
                          font_size=28, color=YELLOW).to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(3)
