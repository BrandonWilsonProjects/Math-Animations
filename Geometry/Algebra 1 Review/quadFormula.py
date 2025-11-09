from manim import *
import math

class QuadraticFormulaDemo(Scene):
    def construct(self):
        # Quadratic: y = x^2 - 3x - 4  (roots at x = -1, 4)
        a, b, c = 1, -3, -4

        # Axes
        axes = Axes(
            x_range=[-4, 6, 1],
            y_range=[-6, 8, 2],
            x_length=7,
            y_length=5,
            axis_config={"include_numbers": False, "include_ticks": True, "stroke_width": 2},
        ).to_edge(LEFT, buff=0.8)
        self.play(Create(axes))

        # Axis labels
        x_lbl = Text("x", font_size=22).next_to(axes.x_axis.get_right(), DOWN)
        y_lbl = Text("y", font_size=22).next_to(axes.y_axis.get_top(), LEFT)
        self.play(FadeIn(x_lbl), FadeIn(y_lbl))

        # Define and plot the quadratic
        def f(x): return a*x*x + b*x + c
        graph = axes.plot(f, x_range=[-4, 6], color=BLUE)
        graph_label = Text("y = ax^2 + bx + c", font_size=22, color=BLUE)\
            .next_to(graph.get_center(), UP, buff=0.3)
        self.play(Create(graph), FadeIn(graph_label))

        # Discriminant and roots
        D = b*b - 4*a*c
        if D >= 0:
            sqrtD = math.sqrt(D)
            x1 = (-b - sqrtD) / (2*a)
            x2 = (-b + sqrtD) / (2*a)

            # Mark roots on x-axis
            root1 = Dot(axes.c2p(x1, 0), color=YELLOW)
            root2 = Dot(axes.c2p(x2, 0), color=YELLOW)

            # Move x1 label LEFT and x2 label RIGHT to clear the parabola
            r1_label = Text(f"x1 ≈ {x1:.2f}", font_size=22, color=YELLOW)\
                .next_to(root1, DOWN, buff=0.2).shift(LEFT * 0.8)
            r2_label = Text(f"x2 ≈ {x2:.2f}", font_size=22, color=YELLOW)\
                .next_to(root2, DOWN, buff=0.2).shift(LEFT * 0.10, DOWN * 0.2)

            self.play(FadeIn(root1), FadeIn(root2), FadeIn(r1_label), FadeIn(r2_label))

        # Vertex
        xv = -b / (2*a)
        yv = f(xv)
        vertex = Dot(axes.c2p(xv, yv), color=RED)
        v_label = Text("Vertex", font_size=20, color=RED).next_to(vertex, UP, buff=0.15)
        self.play(FadeIn(vertex), FadeIn(v_label))

        # Quadratic Formula panel — move WAY DOWN (bottom-right corner)
        panel = RoundedRectangle(corner_radius=0.2, width=6.6, height=3.0)\
            .set_fill(BLACK, 0.2).set_stroke(WHITE, 1)
        panel.to_corner(DR, buff=0.35)  # bottom-right keeps it clear of the x-axis

        t0 = Text("Quadratic Formula:", font_size=28, weight=BOLD)
        t1 = Text("x = (-b ± √(b^2 - 4ac)) / (2a)", font_size=26)
        t2 = Text(f"a = {a},  b = {b},  c = {c}", font_size=24)
        t3 = Text(f"Discriminant D = b^2 - 4ac = {D}", font_size=24)
        if D >= 0:
            t4 = Text(f"Roots ≈ {x1:.2f} and {x2:.2f}", font_size=26, color=YELLOW)
        else:
            t4 = Text("No real roots (D < 0)", font_size=26, color=YELLOW)

        info = VGroup(t0, t1, t2, t3, t4).arrange(DOWN * 0.5, aligned_edge=LEFT, buff=0.02)
        info.move_to(panel.get_center())

        self.play(FadeIn(panel), FadeIn(info))
        self.wait(2)
