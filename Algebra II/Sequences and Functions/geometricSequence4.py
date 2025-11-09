from manim import *

class ExponentialSequenceHalfPower(Scene):
    def construct(self):
        # Title
        title = Text("The Sequence: (1/2)^x + 2", font_size=48, color=YELLOW).to_edge(UP)
        self.play(Write(title))

        # Axes (smaller y-range since values stay close to 2–3)
        axes = Axes(
            x_range=[0, 6, 1],       # x from 0 to 6
            y_range=[2, 3.5, 0.25],  # y from 2 to ~3.5
            axis_config={"color": WHITE},
            x_length=6,
            y_length=4,
        ).shift(DOWN * 0.5)

        x_label = Text("x", font_size=28, color=WHITE).next_to(axes.x_axis.get_end(), DOWN)
        y_label = Text("y = (1/2)^x + 2", font_size=28, color=WHITE).next_to(axes.y_axis.get_end(), LEFT)

        self.play(Create(axes), Write(x_label), Write(y_label))

        # Define function
        def func(x): 
            return (0.5)**x + 2

        # Graph of function
        graph = axes.plot(func, color=BLUE)
        graph_label = Text("y = (1/2)^x + 2", font_size=24, color=BLUE).next_to(graph, UR)

        self.play(Create(graph), Write(graph_label))

        # Sequence points (integer x-values)
        sequence_points = []
        for x in range(7):  # x = 0 to 6
            y = func(x)
            dot = Dot(axes.coords_to_point(x, y), color=RED, radius=0.08)
            label = Text(f"({x}, {round(y,2)})", font_size=20, color=RED).next_to(dot, UP)

            # Scoot label for (6, 2.02) to the right
            if x == 6:
                label.shift(RIGHT * 0.5)

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
            "The sequence values approach 2 as x increases",
            font_size=28, color=YELLOW
        ).next_to(axes, DOWN * 2)

        self.play(Write(conclusion))
        self.wait(2)
