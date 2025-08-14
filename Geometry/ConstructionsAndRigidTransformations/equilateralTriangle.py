from manim import *
import numpy as np

class EquilateralTriangleWithSlashes(Scene):
    def construct(self):
        # Set side length and base points
        side_length = 4
        A = np.array([-side_length / 2, -1, 0])
        B = np.array([side_length / 2, -1, 0])
        height = (np.sqrt(3) / 2) * side_length
        C = np.array([0, -1 + height, 0])

        # Triangle and side lines
        triangle = Polygon(A, B, C, color=WHITE)
        side_AB = Line(A, B)
        side_BC = Line(B, C)
        side_CA = Line(C, A)

        # Draw triangle
        self.play(Create(triangle))

        # Add dots and labels
        dot_A = Dot(A, color=BLUE)
        dot_B = Dot(B, color=BLUE)
        dot_C = Dot(C, color=BLUE)
        label_A = Text("A").next_to(dot_A, DOWN)
        label_B = Text("B").next_to(dot_B, DOWN)
        label_C = Text("C").next_to(dot_C, UP)

        self.play(FadeIn(dot_A), Write(label_A))
        self.play(FadeIn(dot_B), Write(label_B))
        self.play(FadeIn(dot_C), Write(label_C))

        # Helper function to add slashes to a side
        def add_slashes(line, n=1, spacing=0.25, length=0.2):
            slashes = VGroup()
            for i in range(n):
                alpha = (i + 1) / (n + 1)
                point = line.point_from_proportion(alpha)
                direction = line.get_unit_vector()
                # Rotate 90 degrees for perpendicular slash
                perp = np.array([-direction[1], direction[0], 0])
                slash = Line(point - perp * length / 2, point + perp * length / 2)
                slashes.add(slash)
            return slashes

        # Create and show slashes on each side
        slashes_AB = add_slashes(side_AB)
        slashes_BC = add_slashes(side_BC)
        slashes_CA = add_slashes(side_CA)

        self.play(Create(slashes_AB), Create(slashes_BC), Create(slashes_CA))

        self.wait(2)
