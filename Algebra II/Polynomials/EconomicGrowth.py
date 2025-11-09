from manim import *
import math

class EconomicPolynomialReality(Scene):
    def construct(self):
        # ----------------------------------------
        # Title
        # ----------------------------------------
        title = Text("Economic Reality as Polynomial Interaction", font_size=34).to_edge(UP)
        self.play(Write(title))

        # ----------------------------------------
        # Axes Setup
        # ----------------------------------------
        axes = Axes(
            x_range=[1950, 2020, 10],
            y_range=[0, 12, 2],
            x_length=9,
            y_length=5,
            axis_config={"include_tip": True}
        ).shift(DOWN * 0.5)

        x_label = Text("Year", font_size=26).next_to(axes.x_axis.get_end(), DOWN)

        # Position wages label first (left of graph)
        y_label_left = Text("Wages as % of GDP", font_size=24, color=BLUE)
        y_label_left.next_to(axes.y_axis.get_end(), RIGHT * 2)

        # Place profits label directly below wages label
        y_label_right = Text("Corporate Profits as % of GDP", font_size=24, color=RED)
        y_label_right.next_to(y_label_left, RIGHT*4, buff=0.2)

        self.play(Create(axes), Write(x_label), Write(y_label_left), Write(y_label_right))


        # Wages: slowly declining curve with mild oscillation
        def wages_func(x):
            t = (x - 1950) / 70  # normalize over time
            return 6 - 1.5 * t + 0.3 * math.sin(3 * t * math.pi) + 0.2 * math.cos(6 * t * math.pi)

        # Profits: rising nonlinear pattern with volatility
        def profits_func(x):
            t = (x - 1950) / 70
            return 3 + 6 * (t**2) - 1.2 * t + 0.5 * math.sin(4 * t * math.pi)

        # ----------------------------------------
        # Create the two curves
        # ----------------------------------------
        wages_curve = axes.plot(wages_func, x_range=[1950, 2020], color=BLUE)
        profits_curve = axes.plot(profits_func, x_range=[1950, 2020], color=RED)

        wages_label = Text("Wages", font_size=24, color=BLUE).next_to(axes, UP + LEFT)

        self.play(Create(wages_curve), Write(wages_label))
        self.wait(1)
        self.play(Create(profits_curve))
        self.wait(2)

        # ----------------------------------------
        # Animate progression over time
        # ----------------------------------------
        tracker = ValueTracker(1950)
        moving_dot_wages = always_redraw(
            lambda: Dot(color=BLUE).move_to(axes.c2p(tracker.get_value(), wages_func(tracker.get_value())))
        )
        moving_dot_profits = always_redraw(
            lambda: Dot(color=RED).move_to(axes.c2p(tracker.get_value(), profits_func(tracker.get_value())))
        )

        time_text = always_redraw(
            lambda: Text(f"Year: {int(tracker.get_value())}", font_size=26).next_to(title, DOWN)
        )

        self.play(FadeIn(moving_dot_wages), FadeIn(moving_dot_profits), Write(time_text))
        self.play(tracker.animate.set_value(2020), run_time=8, rate_func=linear)
        self.wait(1)

        # ----------------------------------------
        # Fade-out to summary
        # ----------------------------------------
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        end_text = Text(
            "Polynomials aren't just abstract curves — they describe how economies evolve,\n"
            "oscillate, and balance competing trends over decades.",
            font_size=30
        )
        self.play(Write(end_text))
        self.wait(4)
