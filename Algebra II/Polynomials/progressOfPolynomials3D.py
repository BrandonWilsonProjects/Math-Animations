from manim import *

class PolynomialDimensions(ThreeDScene):
    def construct(self):
        # Set up 3D axes
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-5, 5, 1],
            z_range=[-5, 5, 1],
            x_length=7,
            y_length=5,
            z_length=5,
        )

        # Labels for axes (no LaTeX)
        labels = VGroup(
            Text("x", font_size=28, color=WHITE).next_to(axes.x_axis.get_end(), RIGHT),
            Text("y", font_size=28, color=WHITE).next_to(axes.y_axis.get_end(), UP),
            Text("z", font_size=28, color=WHITE).next_to(axes.z_axis.get_end(), OUT)
        )

        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES)
        self.play(Create(axes), Write(labels))

        # Linear (degree 1)
        line = axes.plot(lambda x: x, color=BLUE, x_range=[-3, 3])

        self.play(Create(line))
        self.wait(2)

        # Quadratic (degree 2)
        parabola = axes.plot(lambda x: x**2 - 2, color=GREEN, x_range=[-3, 3])

        self.play(Transform(line, parabola))
        self.wait(2)

        # Cubic (degree 3)
        cubic_curve = axes.plot(lambda x: 0.2 * x**3 - x, color=RED, x_range=[-3, 3])

        self.play(Transform(line, cubic_curve))
        self.wait(2)

        # Rotate camera to emphasize 3D
        self.move_camera(phi=75 * DEGREES, theta=120 * DEGREES, run_time=3)
        self.wait(3)
