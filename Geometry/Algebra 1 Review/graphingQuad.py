from manim import *

class GraphQuadraticFunction(Scene):
    def construct(self):
        # Axes setup
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 10, 1],
            x_length=8,
            y_length=6,
            axis_config={"color": WHITE},
            tips=True
        ).to_edge(DOWN)

        # Replace default number labels with Text (LaTeX-free)
        for x in range(-5, 6):
            if x != 0:
                label = Text(str(x), font_size=18).move_to(axes.c2p(x, 0) + DOWN * 0.3)
                self.add(label)

        for y in range(-5, 11, 2):
            if y != 0:
                label = Text(str(y), font_size=18).move_to(axes.c2p(0, y) + LEFT * 0.3)
                self.add(label)

        self.play(Create(axes))

        # Define quadratic function: y = x^2 - 2x - 3
        def quad(x):
            return x**2 - 2*x - 3

        graph = axes.plot(quad, color=YELLOW, x_range=[-4.5, 4.5])
        graph_label = Text("y = x^2 - 2x - 3", font_size=24, color=YELLOW).move_to(axes.c2p(2.5, quad(2.5)) + UR * 0.5)

        self.play(Create(graph), Write(graph_label))
        self.wait(2)

        # Add a title
        title = Text("Graph of a Quadratic Function", font_size=32).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
