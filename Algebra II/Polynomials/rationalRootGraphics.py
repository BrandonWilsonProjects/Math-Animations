from manim import *

class RationalRootTheoremGraphicalFixed(Scene):
    def construct(self):
        # -------------------------------------
        # Title
        # -------------------------------------
        title = Text("The Power of the Rational Root Theorem", font_size=40, color=YELLOW).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # -------------------------------------
        # Step 1: Polynomial introduction
        # -------------------------------------
        eq = Text("Polynomial: 2x^3 - 3x^2 - 8x + 3", font_size=34)
        self.play(Write(eq))
        self.wait(2)

        desc = Text(
            "The theorem helps us predict where rational roots may appear on the graph.",
            font_size=28, color=BLUE
        ).next_to(eq, DOWN)
        self.play(Write(desc))
        self.wait(2)
        self.play(FadeOut(eq), FadeOut(desc), FadeOut(title))

        # -------------------------------------
        # Step 2: Graph setup (plain text labels)
        # -------------------------------------
        axes = Axes(
            x_range=[-3, 4, 1],
            y_range=[-15, 15, 5],
            x_length=8,
            y_length=5,
        ).shift(DOWN * 0.5)
        self.play(Create(axes))
        self.wait(1)

        x_label = Text("x", font_size=28).next_to(axes.x_axis.get_end(), RIGHT)
        y_label = Text("y", font_size=28).next_to(axes.y_axis.get_end(), UP)
        self.play(Write(x_label), Write(y_label))
        self.wait(1)

        # -------------------------------------
        # Step 3: Plot the polynomial
        # -------------------------------------
        def poly(x):
            return 2*x**3 - 3*x**2 - 8*x + 3

        graph = axes.plot(poly, color=ORANGE)
        self.play(Create(graph))
        self.wait(2)

        # -------------------------------------
        # Step 4: Display predicted roots
        # -------------------------------------
        root_text = Text("Predicted rational roots: ±1, ±3, ±1/2, ±3/2", font_size=30, color=GREEN).to_edge(DOWN)
        self.play(Write(root_text))
        self.wait(3)
        self.play(FadeOut(root_text))

        # -------------------------------------
        # Step 5: Highlight correct root visually
        # -------------------------------------
        correct_root_x = -1.595741  # 3/2 is rational and a true zero
        correct_dot = Dot(axes.c2p(correct_root_x, 0), color=YELLOW)
        label = Text("x = -1.5", font_size=28, color=YELLOW).next_to(correct_dot, UP + LEFT*1.5)

        self.play(GrowFromCenter(correct_dot))
        self.play(Write(label))
        self.wait(2)

        glow = Circle(radius=0.3, color=YELLOW).move_to(correct_dot)
        self.play(Indicate(correct_dot), Create(glow))
        self.wait(2)
        self.play(FadeOut(glow))
        self.wait(1)
        self.play(FadeOut(label))
        self.play(FadeOut(correct_dot))

        # -------------------------------------
        # Step 6: Explanation (non-overlapping)
        # -------------------------------------
        meaning1 = Text(
            "The Rational Root Theorem correctly predicted this crossing point.",
            font_size=30, color=BLUE
        ).to_edge(DOWN)
        self.play(Write(meaning1))
        self.wait(3)
        self.play(FadeOut(meaning1))

        meaning2 = Text(
            "It saves time by showing which rational values are worth testing.",
            font_size=30, color=GREEN
        ).to_edge(DOWN)
        self.play(Write(meaning2))
        self.wait(3)
        self.play(FadeOut(meaning2))

        meaning3 = Text(
            "It connects algebraic predictions directly to the visual graph.",
            font_size=30, color=RED
        ).to_edge(DOWN)
        self.play(Write(meaning3))
        self.wait(3)
        self.play(FadeOut(meaning3))

        # -------------------------------------
        # Step 7: Final message
        # -------------------------------------
        self.play(FadeOut(graph), FadeOut(axes), FadeOut(x_label), FadeOut(y_label))

        conclusion = Text(
            "The Rational Root Theorem turns algebra into insight —\nrevealing structure through logic and visualization.",
            font_size=32, color=YELLOW
        ).move_to(ORIGIN)
        self.play(Write(conclusion))
        self.wait(3)

        self.play(FadeOut(conclusion), FadeOut(title))
