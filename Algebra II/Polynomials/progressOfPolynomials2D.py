from manim import *

class PolynomialDimensions(Scene):
    def construct(self):
        # X-axis
        x_axis = NumberLine(
            x_range=[-4, 4, 1],
            length=8,
            include_numbers=False,
            color=WHITE
        ).shift(DOWN*3)

        # Y-axis
        y_axis = NumberLine(
            x_range=[-6, 6, 1],
            length=6,
            include_numbers=False,
            rotation=90*DEGREES,
            color=WHITE
        ).shift(LEFT*4)

        # Axis labels (plain Text)
        x_label = Text("x", font_size=28, color=WHITE).next_to(x_axis.get_end(), RIGHT)
        y_label = Text("y", font_size=28, color=WHITE).next_to(y_axis.get_end(), UP)

        # Group axes
        axes = VGroup(x_axis, y_axis, x_label, y_label)

        self.play(Create(axes))

        # Functions plotted manually with ParametricFunction
        line = ParametricFunction(lambda t: [t, t, 0], t_range=[-4, 4], color=BLUE)
        parabola = ParametricFunction(lambda t: [t, t**2 - 2, 0], t_range=[-3, 3], color=GREEN)
        cubic = ParametricFunction(lambda t: [t, 0.2*t**3 - t, 0], t_range=[-3, 3], color=RED)

        # Labels (plain Text)
        line_label = Text("Degree 1: Line", font_size=24, color=BLUE).to_corner(UL)
        parabola_label = Text("Degree 2: Parabola", font_size=24, color=GREEN).next_to(line_label, DOWN)
        cubic_label = Text("Degree 3: Cubic", font_size=24, color=RED).next_to(parabola_label, DOWN)

        # Animate progression
        self.play(Create(line), Write(line_label))
        self.wait(2)

        self.play(Transform(line, parabola), Write(parabola_label))
        self.wait(2)

        self.play(Transform(line, cubic), Write(cubic_label))
        self.wait(3)
