from manim import *

class SquareDomainRange(Scene):
    def construct(self):
        # Title
        title = Text("Domain and Range of f(x) = x^2", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Axes setup
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-70, 70, 10],
            x_length=7,
            y_length=6,
        ).to_edge(DOWN)

        x_label = Text("x", font_size=24).next_to(axes.x_axis.get_end(), DOWN)
        y_label = Text("f(x)", font_size=24).next_to(axes.y_axis.get_end(), LEFT)

        self.play(Create(axes), Write(x_label), Write(y_label))

        # Graph of sqaure function
        square_graph = axes.plot(lambda t: 3*t**2, x_range=[-4,4], color=YELLOW)
        graph_label = Text("f(x) = x^2", font_size=24).next_to(square_graph, UR)

        self.play(Create(square_graph), FadeIn(graph_label))

        # Domain annotation (x-axis extends forever)
        domain_text = Text("Domain: all real numbers for x (-∞, ∞)", font_size=28).to_edge(LEFT*0.1).shift(DOWN*2)
        self.play(Write(domain_text))

        # Range annotation (y-axis extends forever)
        range_text = Text("Range: all real numbers for y [0, ∞)", font_size=28).to_edge(RIGHT).shift(DOWN*2)
        self.play(Write(range_text))

        self.wait(3)
