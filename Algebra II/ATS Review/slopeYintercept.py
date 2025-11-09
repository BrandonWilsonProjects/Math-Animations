from manim import *

class SlopeIntercept(Scene):
    def construct(self):
        axes = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            background_line_style={"stroke_opacity": 0.4},
        )
        self.play(Create(axes))

        # Manually add coordinate labels using Text() to avoid LaTeX
        for x in range(-5, 6):
            if x != 0:
                label = Text(str(x), font_size=20)
                label.next_to(axes.c2p(x, 0), DOWN, buff=0.1)
                self.add(label)
        for y in range(-5, 6):
            if y != 0:
                label = Text(str(y), font_size=20)
                label.next_to(axes.c2p(0, y), LEFT, buff=0.1)
                self.add(label)

        # Plot y = 2x + 1
        graph = axes.plot(lambda x: 2 * x + 1, color=BLUE)
        self.play(Create(graph))

        # Y-intercept at (0,1)
        y_intercept = Dot(axes.c2p(0, 1), color=YELLOW)
        y_label = Text("y-int = 1", font_size=24).next_to(y_intercept, RIGHT).shift(RIGHT * 0.5)
        self.play(FadeIn(y_intercept), Write(y_label))

        # Rise over run: (0,1) to (1,3)
        run_arrow = Arrow(axes.c2p(0, 1), axes.c2p(1, 1), color=RED)
        rise_arrow = Arrow(axes.c2p(1, 1), axes.c2p(1, 3), color=GREEN)
        run_label = Text("Run = 1", font_size=20).next_to(run_arrow, DOWN, buff=0.1)
        rise_label = Text("Rise = 2", font_size=20).next_to(rise_arrow, RIGHT, buff=0.1)
        slope_text = Text("Slope = 2", font_size=24).to_corner(UL)

        self.play(GrowArrow(run_arrow), Write(run_label))
        self.play(GrowArrow(rise_arrow), Write(rise_label))
        self.play(Write(slope_text))

        self.wait()
