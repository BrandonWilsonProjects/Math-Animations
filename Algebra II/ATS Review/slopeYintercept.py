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
        labels = VGroup()
        for x in range(-5, 6):
            if x != 0:
                label = Text(str(x), font_size=20)
                label.next_to(axes.c2p(x, 0), DOWN, buff=0.1)
                labels.add(label)
        for y in range(-5, 6):
            if y != 0:
                label = Text(str(y), font_size=20)
                label.next_to(axes.c2p(0, y), LEFT, buff=0.1)
                labels.add(label)
        self.add(labels)
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
        slope_formula = Text("Rise / Run", font_size=24).to_corner(UR)
        slope_text = Text("Slope = 2", font_size=24).to_corner(UL)

        self.play(GrowArrow(run_arrow), Write(run_label))
        self.play(GrowArrow(rise_arrow), Write(rise_label))
        self.play(Write(slope_text))
        self.play(Write(slope_formula))
        self.wait()

        self.play(FadeOut(axes, labels, graph, y_intercept, y_label, run_arrow, run_label, rise_arrow, rise_label, slope_text, slope_formula))
        
        # Closing text concisely expounding on the concept of 'slope'
        
        summary = VGroup(
            Text("Slope - The steepness, incline, or grade of a line", font_size=32, weight=BOLD),
            Text("Positive slope: The line rises from left to right.", font_size=26).shift(DOWN * 0.6),
            Text("Negative slope: The line falls from left to right", font_size=26).shift(DOWN * 1.1),
            Text("Zero slope: The line is horizontal.", font_size=26).shift(DOWN * 1.6),
            Text("Undefined slope: The line is vertical, and division by zero occurs in the formula", font_size=26).shift(DOWN * 2.1)
        )
        
        callout = VGroup(
            MarkupText("<i>m</i> = (<i>y</i><sub>2</sub> - <i>y</i><sub>1</sub>) / (<i>x</i><sub>2</sub> - <i>x</i><sub>1</sub>)", slant=ITALIC).scale(0.45)).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        callout_bg = RoundedRectangle(corner_radius=0.2, height=callout.height+0.5, width=callout.width+0.6)\
            .set_stroke(width=1).set_fill(color=BLACK, opacity=0.2)
        callout_group = VGroup(callout_bg, callout)
        callout_group.next_to(summary, UP, buff=1.5)

        self.play(FadeIn(summary, shift=UP * 0.5, lag_ratio=0.2), run_time=2)
        self.wait(5)
        self.play(FadeIn(callout_group, shift=RIGHT*0.2))
        self.wait(9)