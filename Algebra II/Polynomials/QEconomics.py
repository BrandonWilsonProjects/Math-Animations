from manim import *

class QuadraticEconomics(Scene):
    def construct(self):
        # -----------------------------
        # Title
        # -----------------------------
        title = Text("Quadratic Models in Economics", font_size=36).to_edge(UP)
        self.play(Write(title))

        # -----------------------------
        # Axes setup
        # -----------------------------
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-10, 30, 5],
            x_length=8,
            y_length=5,
            axis_config={"include_tip": True}
        ).shift(DOWN * 0.5)

        x_label = Text("Quantity", font_size=26).next_to(axes.x_axis.get_end(), DOWN)
        y_label = Text("Profit ($)", font_size=26).next_to(axes.y_axis.get_end(), LEFT)
        self.play(Create(axes), Write(x_label), Write(y_label))

        # -----------------------------
        # Profit curve
        # -----------------------------
        profit_graph = axes.plot(lambda x: -x**2 + 8*x - 5, x_range=[0, 10], color=GREEN)
        profit_label = Text("Profit Curve", font_size=26, color=GREEN).next_to(axes, UP)
        self.play(Create(profit_graph), Write(profit_label))
        self.wait(1)

        # -----------------------------
        # Highlight vertex (max profit)
        # -----------------------------
        vertex_x = 4
        vertex_y = -vertex_x**2 + 8*vertex_x - 5
        vertex_point = Dot(axes.c2p(vertex_x, vertex_y), color=YELLOW)
        vertex_text = Text("Maximum Profit", font_size=24).next_to(vertex_point, UP)
        self.play(FadeIn(vertex_point), Write(vertex_text))
        self.wait(1)

        # -----------------------------
        # Moving dot along the curve
        # -----------------------------
        tracker = ValueTracker(0)

        moving_dot = always_redraw(
            lambda: Dot(color=RED).move_to(
                axes.c2p(tracker.get_value(), -tracker.get_value()**2 + 8*tracker.get_value() - 5)
            )
        )

        dynamic_text = always_redraw(
            lambda: Text(
                f"Profit = {-tracker.get_value()**2 + 8*tracker.get_value() - 5:.1f}",
                font_size=26
            ).next_to(title, DOWN*4)
        )

        self.play(FadeIn(moving_dot), Write(dynamic_text))
        self.play(tracker.animate.set_value(8), run_time=6, rate_func=there_and_back)
        self.wait(1)
        # -----------------------------
        # Symmetry line
        # -----------------------------
        symmetry_line = axes.get_vertical_line(axes.c2p(vertex_x, vertex_y), color=BLUE)
        symmetry_label = Text("Axis of Symmetry", font_size=24, color=BLUE).next_to(symmetry_line, RIGHT*9)
        self.play(Create(symmetry_line), Write(symmetry_label))
        self.wait(2)

        # -----------------------------
        # Ending message
        # -----------------------------
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        conclusion = Text(
            "Quadratic models help identify the best production level\n"
            "to maximize economic profit.",
            font_size=30
        )
        self.play(Write(conclusion))
        self.wait(3)
