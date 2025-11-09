from manim import *

class Transversals3DAnimation(ThreeDScene):
    def construct(self):
        # Set up the 3D camera for a nice view
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # Create two cubes
        cube_a = Cube(side_length=2, fill_opacity=0.3, fill_color=BLUE).shift(LEFT * 3)
        cube_b = Cube(side_length=2, fill_opacity=0.3, fill_color=BLUE).shift(RIGHT * 3)

        # Create the transversal line (passing through both cubes)
        transversal = Line(start=LEFT * 5 + UP * 2 + OUT * 1, end=RIGHT * 5 + DOWN * 2 + IN * 1, color=YELLOW)

        # Create dots for intersection points (approximate for visual effect)
        # For simplicity, place dots where the transversal intersects the cubes' faces
        dot_a1 = Dot(point=LEFT * 3 + UP * 1, color=RED, radius=0.1)
        dot_a2 = Dot(point=LEFT * 3 + DOWN * 1, color=RED, radius=0.1)
        dot_b1 = Dot(point=RIGHT * 3 + UP * 1, color=RED, radius=0.1)
        dot_b2 = Dot(point=RIGHT * 3 + DOWN * 1, color=RED, radius=0.1)

        # Animate the cubes
        self.play(Create(cube_a), run_time=1.5)
        self.play(Create(cube_b), run_time=1.5)
        self.wait(1)

        # Animate the transversal and intersection points
        self.play(Create(transversal), run_time=1.5)
        self.play(FadeIn(dot_a1, dot_a2, dot_b1, dot_b2), run_time=1)
        self.wait(1)

        # Rotate the camera to show 3D perspective
        self.move_camera(phi=180 * DEGREES, theta=60 * DEGREES, run_time=7)
        self.wait(1)