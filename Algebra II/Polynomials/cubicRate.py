from manim import *

class CubicGrowthRateNoLatex(Scene):
    def construct(self):
        # Title
        title = Text("Rate of Growth of y = x³", font_size=36).to_edge(UP)
        self.play(Write(title))

        # --- Manual axes (no LaTeX) ---
        x_axis = NumberLine(
            x_range=[-3, 3, 1],
            length=8,
            include_numbers=False,
            color=WHITE
        ).shift(DOWN*3)

        y_axis = NumberLine(
            x_range=[-10, 10, 2],
            length=6,
            include_numbers=False,
            rotation=90*DEGREES,
            color=WHITE
        ).shift(LEFT*4)

        # Axis labels
        x_label = Text("x", font_size=28, color=WHITE).next_to(x_axis.get_end(), RIGHT)
        y_label = Text("y", font_size=28, color=WHITE).next_to(y_axis.get_end(), UP)

        axes_group = VGroup(x_axis, y_axis, x_label, y_label)
        self.play(Create(axes_group))

        # --- Plot cubic curve manually ---
        cubic_curve = ParametricFunction(
            lambda t: [t, t**3/3, 0],  # scaled down to fit
            t_range=[-3, 3],
            color=BLUE
        )
        cubic_label = Text("y = x³", font_size=24, color=BLUE).next_to(cubic_curve, UP+RIGHT)
        self.play(Create(cubic_curve), Write(cubic_label))
        self.wait(1)

        # Moving dot
        dot = Dot(color=YELLOW).move_to(cubic_curve.point_from_proportion(0))
        self.play(FadeIn(dot))

        # Tangent line
        tangent_line = always_redraw(
            lambda: Line(
                dot.get_center() + LEFT*0.5,
                dot.get_center() + RIGHT*0.5,
                color=RED
            ).rotate(
                angle=np.arctan(3*(dot.get_center()[0]+4)),
                about_point=dot.get_center()
            )
        )
        self.play(Create(tangent_line))

        # --- Slope meter (shifted inward from right edge) ---
        slope_line = NumberLine(
            x_range=[-10, 10, 2],
            length=6,
            include_numbers=False,
            rotation=90*DEGREES,
            color=WHITE
        ).shift(RIGHT*4)  # << shifted left from frame edge

        slope_label = Text("Slope (dy/dx)", font_size=24, color=YELLOW).next_to(slope_line, UP)

        slope_dot = always_redraw(
            lambda: Dot(color=GREEN).move_to(
                slope_line.n2p(min(10, max(-10, 3*((dot.get_center()[0]+4))**2 / 3)))
            )
        )
        self.play(Create(slope_line), Write(slope_label), FadeIn(slope_dot))

        # Animate dot along curve
        self.play(
            MoveAlongPath(dot, cubic_curve),
            run_time=8,
            rate_func=linear
        )

        # Closing text
        closing = Text("Growth accelerates: slope = 3x²", font_size=28, color=YELLOW).to_edge(DOWN)
        self.play(Write(closing))
        self.wait(3)
