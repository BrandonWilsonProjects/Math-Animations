from manim import *

class ExponentialGrowthPlain(Scene):
    def construct(self):
        # Create axes (without LaTeX)
        axes = Axes(
            x_range=[-2, 5, 1],
            y_range=[0, 40, 5],
            x_length=6,
            y_length=5,
            axis_config={"include_tip": True, "numbers_to_exclude": [0]},
        ).to_edge(LEFT, buff=1)

        # Plain text axis labels
        x_text = Text("x", font_size=24).next_to(axes.x_axis.get_right(), DOWN)
        y_text = Text("y", font_size=24).next_to(axes.y_axis.get_top(), LEFT)

        self.play(Create(axes), FadeIn(x_text), FadeIn(y_text))

        # Exponential function y = 2^x
        def exp_func(x): return 2 ** x
        graph = axes.plot(exp_func, x_range=[-2, 5], color=BLUE)
        graph_label = Text("y = 2^x", font_size=20, color=BLUE)
        graph_label.next_to(axes.c2p(2.5, 2 ** 2.5), RIGHT)

        self.play(Create(graph), FadeIn(graph_label))

        # Plot dots at each integer x
        dots = VGroup()
        for x in range(-2, 6):
            y = 2 ** x
            dot = Dot(axes.c2p(x, y), color=YELLOW)
            dots.add(dot)

        self.play(LaggedStartMap(FadeIn, dots, shift=UP, lag_ratio=0.15))

        # Add a caption at the top
        caption = Text("Exponential Growth", font_size=30, weight=BOLD)
        caption.to_edge(UP)
        self.play(FadeIn(caption))
        self.wait(1.5)
 