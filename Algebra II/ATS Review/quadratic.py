from manim import *

class QuadraticPolynomialGraph(Scene):
    def construct(self):
        # Set up the axes
        axes = Axes(
            x_range=[-4, 5, 1],
            y_range=[-6, 8, 1],
            x_length=8,
            y_length=5,
            axis_config={"include_numbers": False, "include_ticks": True},
        ).to_edge(LEFT, buff=0.8)

        self.play(Create(axes))

        # Manually add tick labels using Text instead of LaTeX
        for x in range(-4, 6):
            if x != 0:
                label = Text(str(x), font="Consolas", font_size=20)
                label.next_to(axes.coords_to_point(x, 0), DOWN, buff=0.15)
                self.add(label)

        for y in range(-5, 9, 2):
            if y != 0:
                label = Text(str(y), font="Consolas", font_size=20)
                label.next_to(axes.coords_to_point(0, y), LEFT, buff=0.15)
                self.add(label)

        # Add axis labels
        x_label = Text("x", font_size=24).next_to(axes.x_axis.get_end(), RIGHT, buff=0.1).shift(DOWN * 0.2)
        y_label = Text("f(x)", font_size=24).next_to(axes.y_axis.get_end(), LEFT)
        self.play(FadeIn(x_label), FadeIn(y_label))

        # Define the quadratic function f(x) = x^2 - 2x - 3
        def quadratic(x):
            return x**2 - 2*x - 3

        # Plot the function
        graph = axes.plot(quadratic, x_range=[-4, 5], color=BLUE)
        graph_label = Text("f(x) = x² - 2x - 3", font_size=20, color=BLUE)
        graph_label.next_to(graph, UP, buff=0.3).shift(RIGHT * 1)

        self.play(Create(graph), FadeIn(graph_label))
        self.wait(1)

        # Highlight vertex
        vertex_x = 1
        vertex_y = quadratic(vertex_x)
        vertex_point = Dot(axes.coords_to_point(vertex_x, vertex_y), color=YELLOW)
        vertex_label = Text("Vertex", font_size=20).next_to(vertex_point, UP, buff=0.2)

        self.play(FadeIn(vertex_point), FadeIn(vertex_label))
        self.wait(1)

        # Show symmetry
        symmetry_line = DashedLine(
            start=axes.coords_to_point(vertex_x, -6),
            end=axes.coords_to_point(vertex_x, 8),
            color=GRAY
        )
        self.play(Create(symmetry_line))
        self.wait(1)
