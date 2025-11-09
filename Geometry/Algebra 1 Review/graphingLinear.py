from manim import *

class GraphLinearFunction(Scene):
    def construct(self):
        # Axes setup
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 10, 1],
            x_length=8,
            y_length=6,
            tips=True,
            axis_config={"color": WHITE}
        ).to_edge(DOWN)

        # Replace default number labels with plain Text
        for x in range(-4, 5):
            if x != 0:
                label = Text(str(x), font_size=18).move_to(axes.c2p(x, 0) + DOWN * 0.3)
                self.add(label)

        for y in range(-4, 11, 2):
            if y != 0:
                label = Text(str(y), font_size=18).move_to(axes.c2p(0, y) + LEFT * 0.3)
                self.add(label)

        self.play(Create(axes))

        # Linear function: y = 2x + 1
        def linear(x):
            return 2 * x + 1

        graph = axes.plot(linear, color=BLUE, x_range=[-3.5, 3.5])
        graph_label = Text("y = 2x + 1", font_size=24, color=BLUE).move_to(axes.c2p(2.5, linear(2.5)) + UR * 0.5)

        self.play(Create(graph), Write(graph_label))
        self.wait(2)

        # Add title
        title = Text("Graphing a Linear Function", font_size=30).to_edge(UP)
        self.play(Write(title))
        self.wait(2)
