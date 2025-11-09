from manim import *

class RationalRootTheoremPlain(Scene):
    def construct(self):
        # -------------------------------------
        # Title
        # -------------------------------------
        title = Text("The Importance of the Rational Root Theorem", font_size=40, color=YELLOW).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # -------------------------------------
        # Step 1: Introduce polynomial
        # -------------------------------------
        eq = Text("Example Polynomial: 2x^3 - 3x^2 - 8x + 3 = 0", font_size=34)
        self.play(Write(eq))
        self.wait(2)

        explain = Text(
            "We want to find rational roots quickly, not by guessing everything!",
            font_size=28, color=BLUE
        ).next_to(eq, DOWN)
        self.play(Write(explain))
        self.wait(2)
        self.play(FadeOut(explain))

        # -------------------------------------
        # Step 2: State the theorem
        # -------------------------------------
        rule_title = Text("Rational Root Theorem says:", font_size=32, color=GREEN).next_to(eq, DOWN)
        rule = Text(
            "Possible roots = ± (factors of constant term) / (factors of leading coefficient)",
            font_size=26
        ).next_to(rule_title, DOWN)
        self.play(Write(rule_title))
        self.play(Write(rule))
        self.wait(2)

        # -------------------------------------
        # Step 3: Display possible roots
        # -------------------------------------
        roots = Text("Possible roots: ±1, ±3, ±1/2, ±3/2", font_size=30, color=ORANGE).next_to(rule, DOWN)
        self.play(Write(roots))
        self.wait(2)

        # -------------------------------------
        # Step 4: Testing and result
        # -------------------------------------
        trial = Text("Testing shows x = 3/2 works!", font_size=34, color=YELLOW).next_to(roots, DOWN)
        factor = Text("So (2x - 3) is a factor of the polynomial.", font_size=30, color=GREEN).next_to(trial, DOWN)
        self.play(Write(trial))
        self.wait(1)
        self.play(Write(factor))
        self.wait(2)
        self.play(FadeOut(title))

        # -------------------------------------
        # Step 5: Fade out and introduce summary
        # -------------------------------------
        self.play(FadeOut(eq), FadeOut(rule_title), FadeOut(rule), FadeOut(roots), FadeOut(trial), FadeOut(factor))
        summary_title = Text("Why It Matters", font_size=36, color=YELLOW).to_edge(UP)
        self.play(Write(summary_title))

        points = VGroup(
            Text("• Narrows down possible zeros.", font_size=30),
            Text("• Helps factor complex polynomials faster.", font_size=30),
            Text("• Prevents blind guessing.", font_size=30),
            Text("• Connects algebraic roots to graph intersections.", font_size=30)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(summary_title, DOWN, buff=0.6)
        self.play(LaggedStart(*[Write(p) for p in points], lag_ratio=0.5))
        self.wait(2)

        # -------------------------------------
        # Step 6: Final message
        # -------------------------------------
        final = Text(
            "The Rational Root Theorem saves time and reveals structure in every polynomial.",
            font_size=28, color=BLUE
        ).to_edge(DOWN)
        self.play(Write(final))
        self.wait(3)

        self.play(FadeOut(summary_title), FadeOut(points), FadeOut(final))
