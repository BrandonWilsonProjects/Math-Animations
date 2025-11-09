from manim import *

class RelativeMinMaxAnimation(Scene):
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

        # Create dots for relative max and min
        max_point = Dot(axes.c2p(-1, 2), color=RED, radius=0.1)
        min_point = Dot(axes.c2p(1, -2), color=GREEN, radius=0.1)

        # Create labels for the points
        max_label = Text("Relative Max", font_size=30, color=RED).next_to(max_point, UP + LEFT)
        min_label = Text("Relative Min", font_size=30, color=GREEN).next_to(min_point, DOWN + RIGHT)


        # Animate the axes and graph
        self.play(Create(axes), Create(graph), run_time=2)
        self.wait(1)

        # Animate the max and min points with labels
        self.play(FadeIn(max_point), Write(max_label), run_time=1)
        self.play(FadeIn(min_point), Write(min_label), run_time=1)
        self.wait(1)