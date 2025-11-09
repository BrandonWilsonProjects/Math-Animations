from manim import *

class RemainderTheoremPlain(Scene):
    def construct(self):
        # ---------------------------------------
        # Title
        # ---------------------------------------
        title = Text("The Remainder Theorem", font_size=48, color=YELLOW).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # ---------------------------------------
        # Intro Idea
        # ---------------------------------------
        intro = Text(
            "If a polynomial f(x) is divided by (x - a), the remainder is f(a).",
            font_size=34
        ).next_to(title, DOWN)
        self.play(Write(intro))
        self.wait(2)
        self.play(FadeOut(intro))

        # ---------------------------------------
        # Algebraic Setup
        # ---------------------------------------
        eq1 = Text("f(x) = (x - a) * q(x) + r", font_size=42).shift(UP*1)
        eq2 = Text("If the divisor is (x - a), then r = f(a)", font_size=34).next_to(eq1, DOWN)

        self.play(Write(eq1))
        self.wait(1)
        self.play(Write(eq2))
        self.wait(2)

        # ✅ Fix 1: Store each rectangle separately so they can fade properly
        blue_box = SurroundingRectangle(eq1, color=BLUE)
        self.play(Create(blue_box))
        self.wait(1)

        green_box = SurroundingRectangle(eq2, color=GREEN)
        self.play(ReplacementTransform(blue_box, green_box))
        self.wait(2)

        # ✅ Fade everything (including the green box)
        self.play(FadeOut(green_box), FadeOut(eq1), FadeOut(eq2))
        self.wait(0.5)

        # ---------------------------------------
        # Example Polynomial
        # ---------------------------------------
        example_title = Text("Example:", font_size=36).to_edge(UP)
        poly = Text("f(x) = x^3 - 2x^2 + 4x - 8", font_size=40).next_to(example_title, DOWN)
        division = Text("Divide by (x - 2)", font_size=34).next_to(poly, DOWN)

        # ✅ Fade out main title as Example enters
        self.play(FadeOut(title))
        self.play(Write(example_title), Write(poly))
        self.wait(1)
        self.play(Write(division))
        self.wait(2)

        substitution = Text(
            "f(2) = 2^3 - 2*(2^2) + 4*2 - 8 = 8 - 8 + 8 - 8 = 0",
            font_size=32
        ).next_to(division, DOWN*1.2)

        conclusion = Text(
            "So remainder r = 0 → (x - 2) is a factor.",
            font_size=34, color=YELLOW
        ).next_to(substitution, DOWN)

        self.play(Write(substitution))
        self.wait(2)
        self.play(Write(conclusion))
        self.wait(3)
        self.play(FadeOut(example_title), FadeOut(poly), FadeOut(division),
                  FadeOut(substitution), FadeOut(conclusion))

        # ---------------------------------------
        # Graphical Illustration (Plain Text Labels)
        # ---------------------------------------
        axes = Axes(
            x_range=[-1, 5],
            y_range=[-10, 10],
            x_length=8,
            y_length=4,
        ).shift(DOWN*0.5)

        x_label = Text("x", font_size=28).next_to(axes.x_axis.get_end(), DOWN)
        y_label = Text("f(x)", font_size=28).next_to(axes.y_axis.get_end(), LEFT)

        graph = axes.plot(lambda x: x**3 - 2*x**2 + 4*x - 8, color=BLUE)
        point = Dot(axes.coords_to_point(2, 0), color=YELLOW)
        label = Text("(2, 0)", font_size=26, color=YELLOW).next_to(point, UR, buff=0.1)

        self.play(Create(axes))
        self.play(Write(x_label), Write(y_label))
        self.play(Create(graph))
        self.wait(1)
        self.play(FadeIn(point), Write(label))
        self.wait(2)

        text_explain = Text(
            "Since f(2)=0, (x - 2) is a factor.",
            font_size=34, color=GREEN
        ).next_to(axes, DOWN)
        self.play(Write(text_explain))
        self.wait(3)

        # ✅ Fade out graph and axis labels completely
        self.play(
            FadeOut(axes),
            FadeOut(graph),
            FadeOut(point),
            FadeOut(label),
            FadeOut(text_explain),
            FadeOut(x_label),
            FadeOut(y_label)
        )

        # ---------------------------------------
        # Critical Significance Section
        # ---------------------------------------
        summary_title = Text("Why It Matters", font_size=42, color=YELLOW).to_edge(UP)
        self.play(Write(summary_title))

        bullet_points = VGroup(
            Text("1. Simplifies polynomial division without long division.", font_size=30),
            Text("2. Quickly tests if (x - a) is a factor.", font_size=30),
            Text("3. Forms the foundation of the Factor Theorem.", font_size=30),
            Text("4. Connects algebraic evaluation with geometric roots.", font_size=30)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(summary_title, DOWN, buff=0.6)

        for bullet in bullet_points:
            self.play(Write(bullet))
            self.wait(1)

        closing = Text(
            "The Remainder Theorem bridges computation, reasoning, and visualization.",
            font_size=28,
            color=BLUE
        ).next_to(bullet_points, DOWN, buff=0.8)

        self.play(Write(closing))
        self.wait(3)

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.play(Write(Text("End of Scene", font_size=26, color=GRAY).to_edge(DOWN)))
        self.wait(1)
