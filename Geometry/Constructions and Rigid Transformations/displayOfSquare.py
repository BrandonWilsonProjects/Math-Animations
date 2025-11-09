from manim import *
import numpy as np

# ---------------------------
# 2D: Square Transformation
# ---------------------------

class SquareIsometry(Scene):
    def construct(self):
        # Define original square
        A = np.array([-3, -1, 0])
        B = np.array([-1, -1, 0])
        C = np.array([-1,  1, 0])
        D = np.array([-3,  1, 0])

        square = Polygon(A, B, C, D, color=BLUE_D)
        labels = VGroup(
            Text("A").scale(0.6).next_to(A, DL, buff=0.15),
            Text("B").scale(0.6).next_to(B, DR, buff=0.15),
            Text("C").scale(0.6).next_to(C, UR, buff=0.15),
            Text("D").scale(0.6).next_to(D, UL, buff=0.15)
        )
        group = VGroup(square, labels)

        # Construct target square by isometry (rotate + translate)
        theta = PI / 6
        R = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
        T = np.array([4, 2])
        def transform_point(P):
            v = P[:2]
            v2 = R @ v + T
            return np.array([v2[0], v2[1], 0])

        A2, B2, C2, D2 = [transform_point(P) for P in [A, B, C, D]]
        square_tgt = Polygon(A2, B2, C2, D2, color=GREEN_D)
        labels_tgt = VGroup(
            Text("A'").scale(0.6).next_to(A2, DL, buff=0.15),
            Text("B'").scale(0.6).next_to(B2, DR, buff=0.15),
            Text("C'").scale(0.6).next_to(C2, UR, buff=0.15),
            Text("D'").scale(0.6).next_to(D2, UL, buff=0.15)
        )
        group_tgt = VGroup(square_tgt, labels_tgt)

        self.play(Create(group))
        self.play(Create(group_tgt))
        self.wait(0.5)

        step1 = Text("Step 1: Translate A → A'", font_size=30, color=YELLOW).to_edge(DOWN)
        self.play(FadeIn(step1))
        shift_vec = A2 - A
        self.play(group.animate.shift(shift_vec), run_time=1.5)
        self.wait(0.5)

        step2 = Text("Step 2: Rotate to align AB → A'B'", font_size=30, color=YELLOW).to_edge(DOWN)
        self.play(ReplacementTransform(step1, step2))
        v1 = (B + shift_vec) - (A + shift_vec)
        v2 = B2 - A2
        ang = np.arctan2(v2[1], v2[0]) - np.arctan2(v1[1], v1[0])
        self.play(group.animate.rotate(ang, about_point=A2), run_time=1.5)
        self.wait(0.5)


# ---------------------------
# 3D: Cube Transformation
# ---------------------------

class CubeIsometry(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)

        title = Text("Uniqueness of Transformations: Cube → Cube", weight=BOLD).to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(FadeIn(title))

        # Original cube
        cube1 = Cube(side_length=2, fill_opacity=0.2, stroke_color=BLUE)
        cube1.shift(LEFT * 3)
        self.play(Create(cube1))

        # Target cube (rotated + translated)
        cube2 = Cube(side_length=2, fill_opacity=0.2, stroke_color=GREEN)
        cube2.shift(RIGHT * 3 + UP)
        cube2.rotate(PI / 6, axis=UP)
        cube2.rotate(PI / 8, axis=RIGHT)
        self.play(Create(cube2))

        # Step by step
        step1 = Text("Step 1: Translate a vertex A → A'", font_size=28, color=YELLOW).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(step1)
        self.play(FadeIn(step1))
        self.play(cube1.animate.shift(RIGHT * 6 + UP), run_time=2)

        step2 = Text("Step 2: Rotate to align edges", font_size=28, color=YELLOW).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(step2)
        self.play(ReplacementTransform(step1, step2))
        self.play(Rotate(cube1, PI / 6, axis=UP), Rotate(cube1, PI / 8, axis=RIGHT), run_time=2)

        step3 = Text("Result: Cube1 coincides with Cube2 (Unique isometry)", font_size=28, color=YELLOW).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(step3)
        self.play(ReplacementTransform(step2, step3))
        self.wait(2)