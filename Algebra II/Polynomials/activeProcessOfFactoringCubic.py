from manim import *

class CubicFactoringAndGraphing(Scene):
    def construct(self):
        # ----------------------------------------
        # Title
        # ----------------------------------------
        title = Text("Factoring and Graphing  y = x(x² + 7x + 10)", font_size=38).to_edge(UP)
        self.play(Write(title))

        # ----------------------------------------
        # Step 1: Show and expand equation
        # ----------------------------------------
        eqn = Text("y = x(x² + 7x + 10)", font_size=46)
        self.play(Write(eqn))
        self.wait(1.2)

        expanded = Text("Expanded form: y = x³ + 7x² + 10x", font_size=40).next_to(eqn, DOWN)
        self.play(Write(expanded))
        self.wait(1.5)

        self.play(FadeOut(expanded))

        # ----------------------------------------
        # Step 2: Identify coefficients
        # ----------------------------------------
        labels = VGroup(
            Text("Leading coefficient (a) = 1", font_size=30),
            Text("Middle coefficient (b) = 7", font_size=30),
            Text("Linear coefficient (c) = 10", font_size=30),
            Text("Constant term (d) = 0  (since no +d)", font_size=30)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(eqn, DOWN, buff=0.8)

        for label in labels:
            self.play(Write(label))
            self.wait(0.5)

        self.wait(1)
        self.play(FadeOut(labels))

        # ----------------------------------------
        # Step 3: Explain factoring logic for cubic
        # ----------------------------------------
        step1 = Text("Factor out x first: y = x(x² + 7x + 10)", font_size=34).next_to(eqn, DOWN)
        self.play(Write(step1))
        self.wait(1.5)

        step2 = Text("Now factor the quadratic part (x² + 7x + 10)", font_size=32).next_to(step1, DOWN)
        self.play(Write(step2))
        self.wait(1.5)

        pairs = Text("(1, 10), (2, 5)", font_size=32).next_to(step2, DOWN)
        highlight = Text("2 × 5 = 10 and 2 + 5 = 7 ✅", font_size=32, color=GREEN).next_to(pairs, DOWN)
        self.play(Write(pairs))
        self.wait(1)
        self.play(Write(highlight))
        self.wait(1.5)

        self.play(FadeOut(step1, step2, pairs, highlight))

        # ----------------------------------------
        # Step 4: Show fully factored form
        # ----------------------------------------
        factored = Text("Factored form: y = x(x + 2)(x + 5)", font_size=38).next_to(eqn, DOWN, buff=0.4)
        self.play(ReplacementTransform(eqn, factored))
        self.wait(1.5)

        roots = Text("x-intercepts at (0, 0), (-2, 0), (-5, 0)", font_size=32, color=YELLOW).next_to(factored, DOWN)
        self.play(Write(roots))
        self.wait(1.5)

        # ----------------------------------------
        # Step 5: Graph the cubic function
        # ----------------------------------------
        self.play(FadeOut(factored, roots))
        axes = Axes(
            x_range=[-7, 3, 1],
            y_range=[-10, 20, 5],
            x_length=8,
            y_length=5,
        ).to_edge(DOWN, buff=0.5)

        # Plain-text axis labels
        x_label = Text("x", font_size=26).next_to(axes.x_axis.get_end(), DOWN)
        y_label = Text("y", font_size=26).next_to(axes.y_axis.get_end(), LEFT)

        graph = axes.plot(lambda x: x**3 + 7*x**2 + 10*x, x_range=[-7, 3], color=BLUE)
        graph_label = Text("y = x(x² + 7x + 10)", font_size=28, color=BLUE).next_to(axes, UP)

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(0.5)
        self.play(Create(graph), Write(graph_label))
        self.wait(1)

        # ----------------------------------------
        # Step 6: Mark intercepts
        # ----------------------------------------
        root1 = Dot(axes.coords_to_point(0, 0), color=YELLOW)
        root2 = Dot(axes.coords_to_point(-2, 0), color=YELLOW)
        root3 = Dot(axes.coords_to_point(-5, 0), color=YELLOW)

        labels_roots = VGroup(
            Text("(0, 0)", font_size=24, color=YELLOW).next_to(root1, DOWN + RIGHT),
            Text("(-2, 0)", font_size=24, color=YELLOW).next_to(root2, DOWN + LEFT*0.2),
            Text("(-5, 0)", font_size=24, color=YELLOW).next_to(root3, DOWN + LEFT*2),
        )

        self.play(FadeIn(root1, root2, root3))
        self.play(Write(labels_roots))
        self.wait(2)

        # ----------------------------------------
        # End
        # ----------------------------------------
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        end_text = Text("Cubic functions reveal complex turning points and symmetry.", font_size=34)
        self.play(Write(end_text))
        self.wait(2)
