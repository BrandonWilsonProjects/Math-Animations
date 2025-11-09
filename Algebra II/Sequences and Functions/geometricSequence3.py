from manim import *

class ExponentialSequence3xPlus2(Scene):
    def construct(self):
        # Title
        title = Text("The Sequence: 3^x + 2", font_size=48, color=YELLOW).to_edge(UP)
        self.play(Write(title))

        # Axes (shifted up for space below)
        axes = Axes(
            x_range=[0, 5, 1],       # x from 0 to 5
            y_range=[0, 250, 25],    # y from 0 to 250 (smaller growth than 4^x + 1)
            axis_config={"color": WHITE},
            x_length=6,
            y_length=4,
        ).shift(DOWN * 0.5)

        x_label = Text("x", font_size=28, color=WHITE).next_to(axes.x_axis.get_end(), DOWN)
        y_label = Text("y = 3^x + 2", font_size=28, color=WHITE).next_to(axes.y_axis.get_end(), LEFT)

        self.play(Create(axes), Write(x_label), Write(y_label))

        # Define function
        def func(x): 
            return 3**x + 2

        # Graph of function
        graph = axes.plot(func, color=BLUE)
        graph_label = Text("y = 3^x + 2", font_size=24, color=BLUE).next_to(graph, UR)

        self.play(Create(graph), Write(graph_label))

        # Sequence points (integer x-values)
        sequence_points = []
        for x in range(6):  # x = 0 to 5
            y = func(x)
            dot = Dot(axes.coords_to_point(x, y), color=RED, radius=0.08)
            label = Text(f"({x}, {int(y)})", font_size=20, color=RED).next_to(dot, UP)

            # Scoot the label for the last point left if needed
            if x == 5:
                label.shift(LEFT * 0.6)

            sequence_points.append((dot, label))

        # Animate points one by one
        for dot, label in sequence_points:
            self.play(FadeIn(dot, scale=0.5))
            self.play(Write(label))
            self.wait(0.3)

        # Arrows to show alignment with curve
        arrows = [
            Arrow(start=dot.get_bottom(), end=axes.c2p(x, func(x)), buff=0.1, color=GREEN)
            for x, (dot, _) in enumerate(sequence_points)
        ]
        self.play(*[GrowArrow(a) for a in arrows])

        # Closing remark
        conclusion = Text(
            "The sequence values are samples of the curve 3^x + 2",
            font_size=28, color=YELLOW
        ).next_to(axes, DOWN * 2)

        self.play(Write(conclusion))
        self.wait(2)
