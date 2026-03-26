from manim import *

class LogarithmicScalesImportance(Scene):
    def construct(self):
        # Title
        title = Title("The Power of Logarithmic Scales", font_size=72)
        subtitle = Text(
            "Why linear scales fail for exponential data\n — and why the base matters",
            font_size=50,
            color=BLUE_E
        ).next_to(title, DOWN, buff=0.3)

        self.play(Write(title))
        self.play(Write(subtitle))
        self.wait(1.5)

        self.play(
            title.animate.scale(0.7).to_edge(UP),
            subtitle.animate.scale(0.7).next_to(title, DOWN, buff=0.2)
        )
        self.play(FadeOut(title, subtitle))

        # ==================== LINEAR vs LOG COMPARISON ====================
        # ==================== LINEAR vs LOG COMPARISON (One at a Time) ====================
        comparison_title = Text("Linear Scale vs Logarithmic Scale", font_size=48, color=WHITE)
        self.play(Write(comparison_title))
        self.wait(1)
        self.play(comparison_title.animate.to_edge(UP))

        # ------------------- Linear Scale First -------------------
        linear_title = Text("Linear Scale", color=BLUE_D, font_size=42).next_to(comparison_title, DOWN, buff=0.6)

        linear_axes = Axes(
            x_range=[0, 8, 1],
            y_range=[0, 300, 50],
            x_length=7.5,
            y_length=5.2,
            axis_config={"color": BLUE_D, "include_numbers": True, "font_size": 24},
            tips=False
        ).move_to(ORIGIN)

        self.play(Write(linear_title), Create(linear_axes))
        self.wait(0.5)

        # Plot exponential on linear (looks bad)
        exp_linear = linear_axes.plot(lambda x: 2**x, x_range=[0, 8], color=YELLOW_E, stroke_width=6)
        self.play(Create(exp_linear), run_time=2.5)

        linear_problem = Text(
            "Problem: Early values are crushed\nLater values explode off the chart",
            font_size=28,
            color=RED_E
        ).next_to(linear_title, DOWN, buff=0.6)

        self.play(Write(linear_problem))
        self.wait(3)

        # Transition to Log Scale
        self.play(
            FadeOut(linear_title),
            FadeOut(linear_axes),
            FadeOut(exp_linear),
            FadeOut(linear_problem)
        )

        # ------------------- Log Scale Second -------------------
        log_title = Text("Logarithmic Scale \n(Base 2)", color=RED_D, font_size=42).next_to(comparison_title, DOWN, buff=0.6)

        log_axes = Axes(
            x_range=[0, 8, 1],
            y_range=[0, 8, 1],
            x_length=7.5,
            y_length=5.2,
            axis_config={"color": RED_D, "include_numbers": True, "font_size": 24},
            tips=False
        ).move_to(ORIGIN)

        # Custom labels showing actual values (2^0, 2^1, ...)
        log_tick_labels = VGroup(*[
            MathTex(f"2^{{{i}}}", font_size=26).next_to(log_axes.c2p(0, i), LEFT, buff=0.25)
            for i in range(9)
        ])

        self.play(Write(log_title), Create(log_axes), Write(log_tick_labels))
        self.wait(0.8)

        # Plot straight line on log scale (looks perfect)
        log_line = log_axes.plot(lambda x: x, x_range=[0, 8], color=YELLOW_E, stroke_width=6)
        self.play(Create(log_line), run_time=2.5)

        log_benefit = Text(
            "Advantage: Straight line =\n constant growth rate\nAll values are \nclearly visible!",
            font_size=32,
            color=GREEN_E
        ).next_to(UR, DOWN * 2 + RIGHT * 1.3, buff=0.6)

        self.play(Write(log_benefit))
        self.wait(4)

        # Clean up before moving to next part
        self.play(
            FadeOut(log_title),
            FadeOut(log_axes),
            FadeOut(log_tick_labels),
            FadeOut(log_line),
            FadeOut(log_benefit),
            FadeOut(comparison_title),
            run_time=1.2
        )

        # ==================== WHY BASE MATTERS ====================
        base_title = Text("Different Bases for Different Data", font_size=48).to_edge(UP)
        self.play(Write(base_title))

        base_formula = MathTex(
            r"\log_b(x) = \frac{\ln x}{\ln b} = \frac{\log_{10} x}{\log_{10} b}",
            font_size=52
        ).next_to(base_title, DOWN, buff=0.8)

        self.play(Write(base_formula))
        self.wait(1)

        # Three practical examples
        base_title = Text("Different Bases for Different Data", font_size=48).to_edge(UP)
        self.play(Write(base_title))

        base_formula = MathTex(
            r"\log_b(x) = \frac{\ln x}{\ln b} = \frac{\log_{10} x}{\log_{10} b}",
            font_size=52
        ).next_to(base_title, DOWN, buff=0.8)

        self.play(Write(base_formula))
        self.wait(1)

        # Base 2
        base2_group = VGroup(
            MathTex(r"\text{Base 2}", color=GREEN, font_size=48),
            Text("Doubling: bits, memory, population growth", font_size=32)
        ).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(FadeIn(base2_group, shift=UP * 0.5))
        self.wait(2)

        # Base 10
        base10_group = VGroup(
            MathTex(r"\text{Base 10}", color=BLUE, font_size=48),
            Text("Orders of magnitude: Richter scale, pH, decibels", font_size=32)
        ).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(
            FadeOut(base2_group, shift=DOWN * 0.5),
            FadeIn(base10_group, shift=UP * 0.5)
        )
        self.wait(2)

        # Base e
        basee_group = VGroup(
            MathTex(r"\text{Base } e", color=PURPLE, font_size=48),
            Text("Continuous growth: calculus, finance, radioactive decay", font_size=32)
        ).arrange(DOWN, buff=0.4).move_to(ORIGIN)

        self.play(
            FadeOut(base10_group, shift=DOWN * 0.5),
            FadeIn(basee_group, shift=UP * 0.5)
        )
        self.wait(3)

        # Final message
        final = Text(
            "Choose the base that matches your data's natural step size!",
            font_size=32,
            color=GOLD
        ).to_edge(DOWN)
        self.play(Write(final))
        self.wait(4)

        self.play(FadeOut(Group(*self.mobjects)))
        self.wait(1)