from manim import *

class UnitCircleTrig(Scene):
    def construct(self):
        # Setup
        circle = Circle(radius=2, color=WHITE).move_to(ORIGIN)
        x_axis = NumberLine(x_range=[-3, 3, 1], length=6, include_tip=True)
        y_axis = NumberLine(x_range=[-3, 3, 1], length=6, include_tip=True, rotation=PI/2)

        axes = VGroup(x_axis, y_axis)
        axes.move_to(ORIGIN)

        self.play(Create(axes), Create(circle))

        # Angle theta
        angle = ValueTracker(PI/4)  # Start at 45 degrees

        # Moving point on circle
        def get_point():
            theta = angle.get_value()
            return 2 * np.array([np.cos(theta), np.sin(theta), 0])

        point = always_redraw(lambda: Dot(get_point(), color=YELLOW))

        # Hypotenuse line (from origin to point)
        hypotenuse = always_redraw(lambda: Line(ORIGIN, get_point(), color=BLUE))

        # Cosine line (adjacent side)
        adjacent = always_redraw(lambda: Line(ORIGIN, [get_point()[0], 0, 0], color=GREEN))

        # Sine line (opposite side)
        opposite = always_redraw(lambda: Line([get_point()[0], 0, 0], get_point(), color=RED))

        # Tangent line (extends from edge of circle vertically)
        def get_tangent_line():
            x = get_point()[0]
            y = np.tan(angle.get_value())
            return Line([x, 0, 0], [x, y, 0], color=ORANGE).scale(0.8)

        tangent_line = always_redraw(get_tangent_line)

        # Labels
        sin_label = Text("sin(θ)", font_size=24, color=RED).next_to(opposite, RIGHT, buff=0.1)
        cos_label = Text("cos(θ)", font_size=24, color=GREEN).next_to(adjacent, DOWN, buff=0.1)
        tan_label = Text("tan(θ)", font_size=24, color=ORANGE).next_to(tangent_line, RIGHT).shift(UP * 1.0)

        # Angle arc
        arc = always_redraw(lambda: Arc(
            radius=0.5,
            start_angle=0,
            angle=angle.get_value(),
            color=YELLOW
        ))

        theta_label = Text("θ", font_size=24, color=YELLOW).move_to(arc.point_from_proportion(0.5) + 0.3*UP + 0.3*RIGHT)

        self.play(Create(point), Create(hypotenuse), Create(adjacent), Create(opposite), Create(arc))
        self.wait(0.5)

        self.play(Write(sin_label), Write(cos_label), Create(tangent_line), Write(tan_label), Write(theta_label))
        self.wait(1)

        # Animate angle rotation
        self.play(angle.animate.set_value(PI/3), run_time=3)
        self.wait(1)
        self.play(angle.animate.set_value(PI/6), run_time=3)
        self.wait(1)
