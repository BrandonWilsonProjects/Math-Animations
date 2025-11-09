from manim import *

class CubicZerosAnimation(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-4, 4, 1],
            axis_config={"color": WHITE},
            x_length=8,
            y_length=6
        )

        # Define the cubic function f(x) = x^3 - 3x
        def cubic(x):
            return x**3 - 3*x

        # Create the graph of the function
        graph = axes.plot(cubic, color=BLUE)

        # Calculate zero points (roots)
        import math
        zero_neg = Dot(axes.c2p(-math.sqrt(3), 0), color=YELLOW, radius=0.1)
        zero_zero = Dot(axes.c2p(0, 0), color=YELLOW, radius=0.1)
        zero_pos = Dot(axes.c2p(math.sqrt(3), 0), color=YELLOW, radius=0.1)

        # Create labels for the zeros
        label_neg = Text("Zero", font_size=30, color=YELLOW).next_to(zero_neg, DOWN + LEFT)
        label_zero = Text("Zero", font_size=30, color=YELLOW).next_to(zero_zero, DOWN)
        label_pos = Text("Zero", font_size=30, color=YELLOW).next_to(zero_pos, DOWN + RIGHT)

        # Animate the axes and graph
        self.play(Create(axes), Create(graph), run_time=2)
        self.wait(1)

        # Animate the zero points with labels one by one
        self.play(FadeIn(zero_neg), Write(label_neg), run_time=1)
        self.play(FadeIn(zero_zero), Write(label_zero), run_time=1)
        self.play(FadeIn(zero_pos), Write(label_pos), run_time=1)
        self.wait(1)