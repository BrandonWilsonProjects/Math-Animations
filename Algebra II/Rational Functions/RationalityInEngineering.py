from manim import *

class RationalEngineering(Scene):
    def construct(self):

        # Title
        title = Text("Rational Functions in Engineering", font_size=52)
        self.play(FadeIn(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Explanatory subtitle
        subtitle = Text(
            "Why ratios of quantities describe stability, limits, and system behavior",
            font_size=28, color=GRAY
        ).next_to(title, DOWN)
        self.play(FadeIn(subtitle))
        self.wait(1)

        # Number plane
        plane = NumberPlane(
            x_range=[-1, 10, 1],
            y_range=[-5, 15, 1],
            background_line_style={"stroke_opacity": 0.3}
        ).shift(DOWN * 0.5)
        self.play(Create(plane))

        # Rational function example used for beam deflection:
        # y = 10 / (4 - x)
        # (Load F approaching the failure load at F = 4)
        def func(x):
            return 10 / (4 - x)

        # Vertical asymptote
        asymptote = Line(
            start=plane.c2p(4, -10),
            end=plane.c2p(4, 15),
            color=RED
        )
        asym_label = Text("System Limit\n(Failure Load)", font_size=28, color=RED)
        asym_label.next_to(asymptote, RIGHT)

        # Show asymptote
        self.play(Create(asymptote))
        self.play(FadeIn(asym_label))
        self.wait(1)

        # Plot graph
        graph = plane.plot(
            func,
            x_range=[-0.5, 3.8, 0.01],
            color=BLUE
        )
        graph2 = plane.plot(
            func,
            x_range=[4.2, 9.5, 0.01],
            color=BLUE
        )

        graph_label = Text("Beam Deflection = 10 / (4 - Load)", font_size=26, color=BLUE)
        graph_label.next_to(plane, DOWN)

        self.play(Create(graph), Create(graph2), FadeIn(graph_label))
        self.wait(1)

        # Highlight engineering meaning
        note1 = Text(
            "As load approaches the maximum safe limit,\ndeflection increases rapidly.",
            font_size=26
        ).to_edge(LEFT).shift(UP * 1)
        self.play(FadeIn(note1))
        self.wait(1)

        # Moving point approaching the asymptote
        dot = Dot(color=YELLOW, radius=0.09)
        dot_label = Text("", font_size=24, color=YELLOW)

        def update_dot(mob, alpha):
            x = interpolate(1, 3.75, alpha)
            y = func(x)
            mob.move_to(plane.c2p(x, y))

        def update_label(mob):
            x, y = plane.p2c(dot.get_center())
            mob.become(Text(f"Load: {x:.2f}\nDeflection: {y:.2f}", font_size=22, color=YELLOW)
                       .next_to(dot, UR, buff=0.2))

        dot.add_updater(update_dot)
        dot_label.add_updater(update_label)

        self.add(dot, dot_label)
        self.play(Wait(run_time=7))
        self.wait(1)

        # Remove dot
        dot.remove_updater(update_dot)
        dot_label.remove_updater(update_label)
        self.play(FadeOut(dot), FadeOut(dot_label))

        # Horizontal asymptote concept
        h_label = Text(
            "Many rational functions flatten out,\nrepresenting system stability over time.",
            font_size=26
        ).to_edge(RIGHT).shift(UP)
        self.play(FadeIn(h_label))
        self.wait(1)

        # New rational function: y = (5x) / (x + 2)
        def func2(x):
            return (5 * x) / (x + 2)

        graph3 = plane.plot(
            func2,
            x_range=[0.1, 9.5, 0.01],
            color=GREEN
        )

        graph3_label = Text(
            "Signal Response = (5·input) / (input + 2)",
            font_size=26,
            color=GREEN
        ).next_to(plane, DOWN)

        self.play(Create(graph3), FadeIn(graph3_label))
        self.wait(1)

        plateau = Line(
            start=plane.c2p(-1, 5),
            end=plane.c2p(10, 5),
            color=GREEN
        )
        plateau_label = Text("Long-term Output → 5", font_size=24, color=GREEN)
        plateau_label.next_to(plateau, RIGHT)

        self.play(Create(plateau), FadeIn(plateau_label))
        self.wait(2)

        # Final summary
        summary = Text(
            "Rational functions describe:\n"
            "• Limits and failure points\n"
            "• Stability levels of systems\n"
            "• Ratios of forces, flow, pressure, current, and more\n"
            "Essential for real engineering models.",
            font_size=30
        ).to_edge(DOWN)
        self.play(FadeIn(summary))
        self.wait(2)

        self.play(*map(FadeOut, [subtitle, note1, h_label, graph_label, graph3_label]))
        self.wait(2)
