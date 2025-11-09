from manim import *

class FactoringAndGraphingNoLatex(Scene):
    def construct(self):
        # ----------------------------------------
        # Title
        # ----------------------------------------
        title = Text("Factoring and Graphing  y = x² + 7x + 12", font_size=38).to_edge(UP)
        self.play(Write(title))

        # ----------------------------------------
        # Step 1: Identify coefficients
        # ----------------------------------------
        eqn = Text("y = x² + 7x + 12", font_size=46)
        self.play(Write(eqn))
        self.wait(1)

        labels = VGroup(
            Text("Leading coefficient (a) = 1", font_size=30),
            Text("Linear coefficient (b) = 7", font_size=30),
            Text("Constant term (c) = 12", font_size=30)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(eqn, DOWN, buff=0.8)

        for label in labels:
            self.play(Write(label))
            self.wait(0.5)

        self.wait(1)
        self.play(FadeOut(labels))

        # ----------------------------------------
        # Step 2: Explain factoring logic
        # ----------------------------------------
        step1 = Text("Find two numbers that multiply to 12 and add to 7.", font_size=32).next_to(eqn, DOWN)
        self.play(Write(step1))
        self.wait(1.5)

        pairs = Text("(1, 12), (2, 6), (3, 4)", font_size=34).next_to(step1, DOWN)
        self.play(Write(pairs))
        self.wait(1.5)

        highlight = Text("3 × 4 = 12 and 3 + 4 = 7 ✅", font_size=34, color=GREEN).next_to(pairs, DOWN)
        self.play(Write(highlight))
        self.wait(2)

        # ----------------------------------------
        # Step 3: Show factored form (move up after fadeout)
        # ----------------------------------------
        self.play(FadeOut(step1, pairs, highlight))
        self.wait(0.3)
        factored = Text("Factored form: y = (x + 3)(x + 4)", font_size=38).next_to(eqn, DOWN, buff=0.3)
        self.play(Transform(eqn, factored))
        self.wait(1)
        
        roots = Text("x-intercepts at (-3, 0) and (-4, 0)", font_size=32, color=YELLOW).next_to(factored, DOWN)
        self.play(Write(roots))
        self.wait(1.5)

        # ----------------------------------------
        # Step 4: Vertex calculation (fade out factored + roots)
        # ----------------------------------------
        self.play(FadeOut(roots))
        self.wait(0.3)
        vertex_text = Text("Find vertex using formula  x = -b / (2a)", font_size=32).next_to(eqn, DOWN)
        self.play(Write(vertex_text))
        self.wait(1.5)
        
        vertex_calc1 = Text("x = -7 / (2 × 1) = -3.5", font_size=34, color=BLUE).next_to(vertex_text, DOWN)
        vertex_calc2 = Text("y = (-3.5)² + 7(-3.5) + 12 = -0.25", font_size=34, color=BLUE).next_to(vertex_calc1, DOWN)
        vertex_point = Text("Vertex: (-3.5, -0.25)", font_size=34, color=YELLOW).next_to(vertex_calc2, DOWN, buff=0.1)

        self.play(Write(vertex_calc1))
        self.wait(0.8)
        self.play(Write(vertex_calc2))
        self.wait(0.8)
        self.play(Write(vertex_point))
        self.wait(1.5)

        self.play(FadeOut(eqn, vertex_calc1, vertex_calc2, vertex_point, vertex_text))
        self.wait(0.5)

        # ----------------------------------------
        # Step 5: Graph the function
        # ----------------------------------------
        axes = Axes(
            x_range=[-7, 2, 1],
            y_range=[-5, 15, 5],
            x_length=8,
            y_length=5,
        ).to_edge(DOWN, buff=0.5)

        # Plain text axis labels (no LaTeX)
        x_label = Text("x", font_size=26).next_to(axes.x_axis.get_end(), DOWN)
        y_label = Text("y", font_size=26).next_to(axes.y_axis.get_end(), LEFT)

        graph = axes.plot(lambda x: x**2 + 7*x + 12, x_range=[-7, 2], color=BLUE)
        graph_label = Text("y = x² + 7x + 12", font_size=28, color=BLUE).next_to(axes, UP)

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(0.5)
        self.play(Create(graph), Write(graph_label))
        self.wait(1)

        # Plot points: roots, vertex, y-intercept
        root1 = Dot(axes.coords_to_point(-3, 0), color=YELLOW)
        root2 = Dot(axes.coords_to_point(-4, 0), color=YELLOW)
        vertex_dot = Dot(axes.coords_to_point(-3.5, -0.25), color=RED)
        yint_dot = Dot(axes.coords_to_point(0, 12), color=GREEN)

        root_labels = VGroup(
            Text("(-3, 0)", font_size=24, color=YELLOW).next_to(root1, DOWN),
            Text("(-4, 0)", font_size=24, color=YELLOW).next_to(root2, DOWN),
        )

        # ↓ Move vertex label slightly lower to avoid overlapping
        vertex_label = Text("Vertex (-3.5, -0.25)", font_size=26, color=RED).next_to(vertex_dot, DOWN*1.9)

        # ↓ Move y-intercept label slightly left so it doesn’t touch y-axis
        yint_label = Text("y-intercept (0, 12)", font_size=26, color=GREEN).next_to(yint_dot, LEFT*1.5 + UP*0.2)

        self.play(FadeIn(root1, root2, vertex_dot, yint_dot))
        self.play(Write(root_labels), Write(vertex_label), Write(yint_label))
        self.wait(3)

        # ----------------------------------------
        # End
        # ----------------------------------------
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        end_text = Text("Factoring reveals structure. The graph shows behavior.", font_size=34)
        self.play(Write(end_text))
        self.wait(2)
