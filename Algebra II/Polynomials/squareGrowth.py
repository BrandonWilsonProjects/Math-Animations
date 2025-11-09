from manim import *

class QuadraticAreaGrowth(Scene):
    def construct(self):
        # Title
        title = Text("Quadratic Growth of Area (x^2)", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Axes for quadratic function (centered)
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 20, 5],
            x_length=6,
            y_length=4,
        ).shift(DOWN*1.2)  # keep graph a little lower

        # Labels
        label_x = Text("x", font_size=24).next_to(axes.x_axis.get_end(), DOWN)
        label_y = Text("Area = x^2", font_size=24).next_to(axes.y_axis.get_end(), LEFT)

        # Graph of quadratic function
        quad_graph = axes.plot(lambda t: t**2, x_range=[0, 4], color=YELLOW)
        graph_label = Text("x^2", font_size=24).next_to(quad_graph.get_end(), UP)

        # Animate graph
        self.play(Create(axes), Write(label_x), Write(label_y))
        self.play(Create(quad_graph), FadeIn(graph_label))

        # Square: centered horizontally, just slightly above the axes
        square = Square(
            side_length=0.01,
            fill_color=GREEN,
            fill_opacity=0.6,
            stroke_color=WHITE
        )
        square.move_to(axes.get_center() + UP*1)  # lower placement
        self.add(square)

        # Animate growth of the square while plotting points on graph
        for x in [0.5, 1, 1.5, 2, 2.5, 3]:
            new_square = Square(
                side_length=x,
                fill_color=GREEN,
                fill_opacity=0.6,
                stroke_color=WHITE
            )
            new_square.move_to(axes.get_center() + UP*2)  # stays low above graph
            self.play(Transform(square, new_square), run_time=1.2)

            # Add dot on 2D graph
            dot = Dot(axes.c2p(x, x**2), color=RED)
            self.play(FadeIn(dot), run_time=0.5)
            self.wait(0.3)

        self.wait(2)
