from manim import *

class LinearSequenceNegativeMeander(Scene):
    def construct(self):
        # Title
        title = Text("The Sequence: (-2/5)x + 10", font_size=48, color=YELLOW).to_edge(UP)
        self.play(Write(title))

        # Axes
        axes = Axes(
            x_range=[0, 10, 1],      # x from 0 to 10
            y_range=[0, 12, 1],      # y values between 0 and 12
            axis_config={"color": WHITE},
            x_length=7,
            y_length=4,
        ).shift(DOWN * 0.5)

        x_label = Text("x", font_size=28, color=WHITE).next_to(axes.x_axis.get_end(), DOWN)
        y_label = Text("y = (-2/5)x + 10", font_size=28, color=WHITE).next_to(axes.y_axis.get_end(), LEFT)

        self.play(Create(axes), Write(x_label), Write(y_label))

        # Define function
        def func(x): 
            return (-0.4) * x + 10

        # Graph of function
        graph = axes.plot(func, color=BLUE)
        graph_label = Text("y = (-2/5)x + 10", font_size=24, color=BLUE).next_to(graph, UR)

        self.play(Create(graph), Write(graph_label))

        # Sequence points with meandering labels
        sequence_points = []
        for x in range(11):  # x = 0 to 10
            y = func(x)
            dot = Dot(axes.coords_to_point(x, y), color=RED, radius=0.08)

            # Alternate label placement: above for even x, below for odd x
            if x % 2 == 0:
                label = Text(f"({x}, {y:.1f})", font_size=20, color=RED).next_to(dot, UP)
            else:
                label = Text(f"({x}, {y:.1f})", font_size=20, color=RED).next_to(dot, DOWN)

            sequence_points.append((dot, label))

        # Animate points
        for dot, label in sequence_points:
            self.play(FadeIn(dot, scale=0.5))
            self.play(Write(label))
            self.wait(0.2)

        # Arrows showing connection to the curve
        arrows = [
            Arrow(start=dot.get_bottom(), end=axes.c2p(x, func(x)), buff=0.1, color=GREEN)
            for x, (dot, _) in enumerate(sequence_points)
        ]
        self.play(*[GrowArrow(a) for a in arrows])

        # Closing remark
        conclusion = Text(
            "Labels meander above and below the line for clarity",
            font_size=28, color=YELLOW
        ).next_to(axes, DOWN * 2)

        self.play(Write(conclusion))
        self.wait(2)
