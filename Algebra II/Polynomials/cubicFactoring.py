from manim import *

class CubicFactoring3D(ThreeDScene):
    def construct(self):
        # -----------------------------------
        # Title
        # -----------------------------------
        title = Text("Volume Factoring: 2x³ + 5x² + 3x", font_size=36).to_edge(UP)
        self.play(Write(title))

        # -----------------------------------
        # Axes Setup
        # -----------------------------------
        axes = ThreeDAxes(
            x_range=[0, 5],
            y_range=[0, 5],
            z_range=[0, 8],
            )
        self.play(Create(axes))
        self.set_camera_orientation(phi=65 * DEGREES, theta=45 * DEGREES)
        self.wait(1)

        # -----------------------------------
        # Base cube (2x³)
        # -----------------------------------
        base_cube = Cube(side_length=1, fill_opacity=0.6, fill_color=BLUE, stroke_width=1)
        base_cube.scale([1, 1, 2])
        base_cube.move_to([0.5, 0.5, 1])
        label_base = Text("2x³", font_size=28, color=WHITE).move_to(base_cube.get_center() + UP*1.2)
        self.play(FadeIn(base_cube), Write(label_base))
        self.wait(0.5)

        # -----------------------------------
        # Prism for 5x²
        # -----------------------------------
        prism_5x2 = Prism(dimensions=[1, 1, 1], fill_opacity=0.6, fill_color=ORANGE)
        prism_5x2.scale([1, 1, 2.5])
        prism_5x2.move_to([1.5, 0.5, 1.25])
        label_5x2 = Text("5x²", font_size=28, color=WHITE).move_to(prism_5x2.get_center() + UP*1.2)
        self.play(FadeIn(prism_5x2), Write(label_5x2))
        self.wait(0.5)

        # -----------------------------------
        # Prism for 3x
        # -----------------------------------
        prism_3x = Prism(dimensions=[1, 1, 1], fill_opacity=0.6, fill_color=GREEN)
        prism_3x.scale([1, 1, 1.5])
        prism_3x.move_to([0.5, 1.5, 0.75])
        label_3x = Text("3x", font_size=28, color=WHITE).move_to(prism_3x.get_center() + UP*1.0)
        self.play(FadeIn(prism_3x), Write(label_3x))
        self.wait(1)

        # -----------------------------------
        # Dimension Labels
        # -----------------------------------
        label_x = Text("x", font_size=26, color=YELLOW).next_to(axes.x_axis, DOWN)
        label_y = Text("x + 1", font_size=26, color=YELLOW).next_to(axes.y_axis, LEFT)
        label_z = Text("2x + 3", font_size=26, color=YELLOW).next_to(axes.z_axis, UP)
        self.play(Write(label_x), Write(label_y), Write(label_z))
        self.wait(1)

        # -----------------------------------
        # Display factored form
        # -----------------------------------
        factored_text = Text("Factored Form: x(x + 1)(2x + 3)", font_size=30, color=YELLOW).to_edge(DOWN)
        self.play(Write(factored_text))
        self.wait(1)

        # -----------------------------------
        # Rotate for 3D perspective
        # -----------------------------------
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(5)
        self.stop_ambient_camera_rotation()

        # Fade out
        self.play(FadeOut(VGroup(base_cube, prism_5x2, prism_3x, label_base, label_5x2, label_3x, label_x, label_y, label_z, factored_text, axes, title)))
