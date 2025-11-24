from manim import *

class LinearVsRational(Scene):
    def construct(self):
        # AXES
        axes = Axes(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            x_length=8,
            y_length=8,
            tips=False
        ).to_edge(LEFT, buff=0.5)

        self.play(Create(axes))
        self.wait(1)

        # Manual x and y labels (NO LATEX)
        x_label = Text("x", font_size=32).next_to(axes.x_axis, RIGHT)
        y_label = Text("y", font_size=32).next_to(axes.y_axis, DOWN)

        self.play(FadeIn(x_label), FadeIn(y_label))
        self.wait(1)

        # ===========================
        # 1. Graph y = x + 3
        # ===========================
        linear = lambda x: x + 3

        line_graph = axes.plot(linear, color=BLUE)
        line_text = Text("Graphing: y = x + 3", color=BLUE).scale(0.6)
        line_text.next_to(axes, RIGHT, buff=0.5)

        self.play(Create(line_graph), FadeIn(line_text))
        self.wait(2)

        # Remove linear graph
        self.play(FadeOut(line_graph), FadeOut(line_text))
        self.wait(1)

        # ===========================
        # 2. Graph y = (x + 3) / x
        # ===========================
        rational = lambda x: (x + 3) / x

        left_branch = axes.plot(rational, x_range=[-10, -0.2], color=YELLOW)
        right_branch = axes.plot(rational, x_range=[0.2, 10], color=YELLOW)

        rational_text = Text("Graphing: y = (x + 3) / x", color=YELLOW).scale(0.6)
        rational_text.next_to(axes, RIGHT, buff=0.5)

        self.play(Create(left_branch), Create(right_branch), FadeIn(rational_text))
        self.wait(2)

        # ===========================
        # 3. ASYMPTOTES
        # ===========================

        # Vertical asymptote at x = 0
        vert_asym = axes.get_vertical_line(axes.c2p(0, 0), color=RED)
        vert_label = Text("Vertical asymptote at x = 0", color=RED).scale(0.5)
        vert_label.next_to(rational_text, DOWN * 2 + LEFT * 0.5)

        self.play(Create(vert_asym), FadeIn(vert_label))
        self.wait(1)

        # Horizontal asymptote at y = 1
        horiz_asym = axes.plot(lambda x: 1, color=RED)
        horiz_label = Text("Horizontal asymptote at y = 1", color=RED).scale(0.5)
        horiz_label.next_to(rational_text, DOWN * 4 + LEFT * 0.2)

        self.play(Create(horiz_asym), FadeIn(horiz_label))
        self.wait(2)

        # ===========================
        # 4. Summary text
        # ===========================
        self.play(FadeOut(axes, x_label, y_label, vert_asym, vert_label, left_branch, right_branch, rational_text, horiz_asym, horiz_label))
        summary = Text(
            "The denominator creates a break at x = 0.\n"
            "The graph approaches y = 1 as x becomes large.",
            color=WHITE,
            font_size=30
        )

        self.play(FadeIn(summary))
        self.wait(5)
