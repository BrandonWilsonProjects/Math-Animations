from manim import *
import numpy as np

class Log10Graph(Scene):
    def construct(self):
        # Axes without auto number labels (to avoid LaTeX)
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-2, 2, 1],
            x_length=8,
            y_length=5,
            axis_config={"include_numbers": False, "include_ticks": True, "stroke_width": 2},
            tips=True,
        ).to_edge(LEFT, buff=0.8)

        self.play(Create(axes))

        # Manual tick labels (plain Text)
        x_tick_labels = VGroup()
        for xv in [0.1, 1, 2, 5, 10]:
            lbl = Text(str(xv), font_size=20)
            lbl.next_to(axes.c2p(xv, 0), DOWN, buff=0.12)
            x_tick_labels.add(lbl)

        y_tick_labels = VGroup()
        for yv in range(-2, 3):
            if yv == 0:
                continue
            lbl = Text(str(yv), font_size=20)
            lbl.next_to(axes.c2p(0, yv), LEFT, buff=0.12)
            y_tick_labels.add(lbl)

        self.play(FadeIn(x_tick_labels), FadeIn(y_tick_labels))

        # Axis titles (plain Text)
        x_text = Text("x", font_size=24).next_to(axes.x_axis.get_right(), DOWN)
        y_text = Text("y", font_size=24).next_to(axes.y_axis.get_top(), LEFT)
        self.play(FadeIn(x_text), FadeIn(y_text))

        # Graph y = log10(x)
        log10_graph = axes.plot(lambda x: np.log10(x), x_range=[0.1, 10], color=YELLOW)

        # Curve label (plain Text)
        log10_label = Text("log10(x)", font_size=20).set_color(YELLOW)
        log10_label.next_to(axes.c2p(8, np.log10(8)), UR, buff=0.2)

        # Title (plain Text)
        title = Text("Base-10 Logarithm", font_size=30).to_edge(UP)

        # Animate
        self.play(Create(log10_graph), FadeIn(log10_label), FadeIn(title))
        self.wait(2)

        # Clean exit
        self.play(
            FadeOut(
                axes, x_tick_labels, y_tick_labels,
                x_text, y_text, log10_graph, log10_label, title
            )
        )
        self.wait(0.5)
