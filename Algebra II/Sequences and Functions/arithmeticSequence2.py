from manim import *

class LinearSequence(Scene):
    def construct(self):
        # Title
        title = Text("The Sequence: (3/2)x + 4", font_size=48, color=YELLOW).to_edge(UP)
        self.play(Write(title))

        # Axes (linear growth, so keep y-range modest)
        axes = Axes(
            x_range=[0, 6, 1],       # x from 0 to 6
            y_range=[0, 15, 1.5],    # y values will stay under ~15
            axis_config={"color": WHITE},
            x_length=6,
            y_length=4,
        ).shift(DOWN * 0.5)

        x_label = Text("x", font_size=28, color=WHITE).next_to(axes.x_axis.get_end(), DOWN)
        y_label = Text("y = (3/2)x + 4", font_size=28, color=WHITE).next_to(axes.y_axis.get_end(), LEFT)

        self.play(Create(axes), Write(x_label), Write(y_label))

        # Define function
        def func(x): 
            return (1.5) * x + 4

        # Graph of function
        graph = axes.plot(func, color=BLUE)
        graph_label = Text("y = (3/2)x + 4", font_size=24, color=BLUE).next_to(graph, UR)

        self.play(Create(graph), Write(graph_label))

        # Sequence points (integer x-values)
        sequence_points = []
        for x in range(7):  # x = 0 to 6
            y = func(x)
            dot = Dot(axes.coords_to_point(x, y), color=RED, radius=0.08)
            label = Text(f"({x}, {y:.1f})", font_size=20, color=RED).next_to(dot, UP)

            # Scoot far-right label if needed
            if x == 6:
                label.shift(LEFT * 0.5)

            sequence_points.append((dot, label))

        # Animate points one by one
        for dot, label in sequence_points:
            self.play(FadeIn(dot, scale=0.5))
            self.play(Write(label))
            self.wait(0.3)

        # Arrows to show alignment with line
        arrows = [
            Arrow(start=dot.get_bottom(), end=axes.c2p(x, func(x)), buff=0.1, color=GREEN)
            for x, (dot, _) in enumerate(sequence_points)
        ]
        self.play(*[GrowArrow(a) for a in arrows])

        # Closing remark
        conclusion = Text(
            "This sequence grows linearly with slope 1.5",
            font_size=28, color=YELLOW
        ).next_to(axes, DOWN * 2)

        self.play(Write(conclusion))
        self.wait(2)
