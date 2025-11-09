from manim import *

class RemainderTheoremReality(Scene):
    def construct(self):
        # ---------------------------------------
        # Title
        # ---------------------------------------
        title = Text("When the Remainder is NOT Zero", font_size=46, color=YELLOW).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # ---------------------------------------
        # Intro Explanation
        # ---------------------------------------
        intro = Text(
            "If f(a) ≠ 0, then (x - a) is NOT a factor.",
            font_size=34
        ).next_to(title, DOWN)
        self.play(Write(intro))
        self.wait(2)
        self.play(FadeOut(intro))
        self.play(FadeOut(title))

        # ---------------------------------------
        # Graph Setup
        # ---------------------------------------
        axes = Axes(
            x_range=[-1, 5],
            y_range=[-10, 10],
            x_length=8,
            y_length=4,
            axis_config={"include_tip": False}
        ).shift(DOWN*0.5)

        x_label = Text("x", font_size=28).next_to(axes.x_axis.get_end(), DOWN)
        y_label = Text("f(x)", font_size=28).next_to(axes.y_axis.get_end(), LEFT)

        # Polynomial that does NOT cross x-axis at x=3
        graph = axes.plot(lambda x: x**3 - 2*x**2 + 4*x - 8, color=BLUE)

        # ---------------------------------------
        # Highlight the chosen test value
        # ---------------------------------------
        a_value = 3
        f_a = a_value**3 - 2*a_value**2 + 4*a_value - 8  # Evaluate at x=3
        point = Dot(axes.coords_to_point(a_value, f_a), color=YELLOW)
        point_label = Text(f"(3, {int(f_a)})", font_size=26, color=YELLOW).next_to(point, UR, buff=0.1)

        # ---------------------------------------
        # Vertical guide line at x = 3
        # ---------------------------------------
        guide_line = DashedLine(
            start=axes.coords_to_point(a_value, 0),
            end=axes.coords_to_point(a_value, f_a),
            color=RED
        )
        remainder_label = Text("Remainder = f(3) = 13", font_size=30, color=RED).next_to(guide_line, RIGHT, buff=0.2)

        # ---------------------------------------
        # Draw and animate step by step
        # ---------------------------------------
        self.play(Create(axes))
        self.play(Write(x_label), Write(y_label))
        self.play(Create(graph))
        self.wait(1)

        self.play(FadeIn(point), Write(point_label))
        self.wait(1)
        self.play(Create(guide_line))
        self.play(Write(remainder_label))
        self.wait(2)

        # ---------------------------------------
        # Add explanatory text
        # ---------------------------------------
        text_explain = VGroup(
            Text("Here, f(3) = 13 → remainder is NOT zero.", font_size=32, color=GREEN),
        ).arrange(DOWN, aligned_edge=RIGHT).next_to(axes, DOWN, buff=0.9)

        for line in text_explain:
            self.play(Write(line))
            self.wait(1)

        self.wait(2)

        # ---------------------------------------
        # Fade out
        # ---------------------------------------
        self.play(
            FadeOut(axes),
            FadeOut(graph),
            FadeOut(point),
            FadeOut(point_label),
            FadeOut(guide_line),
            FadeOut(remainder_label),
            FadeOut(x_label),
            FadeOut(y_label),
            FadeOut(text_explain),
            FadeOut(title)
        )

        # ---------------------------------------
        # Closing summary
        # ---------------------------------------
        closing = Text(
            "The Remainder Theorem shows that a non-zero remainder means no root at that point.",
            font_size=25,
            color=WHITE
        )
        self.play(Write(closing))
        self.wait(3)
        self.play(FadeOut(closing))
