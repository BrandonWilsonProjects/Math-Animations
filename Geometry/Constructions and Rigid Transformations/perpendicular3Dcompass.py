from manim import *

class GeometricSequenceCompass3D(ThreeDScene):
    def construct(self):
        # Title
        title = Text("3D Geometric Sequence as Directions", font_size=36, color=YELLOW).to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)

        # Camera orientation
        self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES)

        # Center point
        origin = np.array([0, 0, 0])
        dot_O = Dot3D(origin, color=WHITE)
        self.play(FadeIn(dot_O))

        # Compass directions (unit vectors)
        directions = {
            "N": np.array([0, 1, 0]),
            "S": np.array([0, -1, 0]),
            "E": np.array([1, 0, 0]),
            "W": np.array([-1, 0, 0]),
            "Up": np.array([0, 0, 1]),
            "Down": np.array([0, 0, -1]),
        }

        # Labels for directions (fixed to camera orientation)
        for label, vec in directions.items():
            text = Text(label, font_size=28, color=BLUE).move_to(vec * 2)
            self.add_fixed_orientation_mobjects(text)
            self.play(Write(text), run_time=0.3)

        # Sequence parameters
        a1, r, terms = 0.5, 1.5, 4  # first term, ratio, number of terms

        # Draw arrows for sequence in each direction
        for n in range(terms):
            scale = a1 * (r ** n)
            arrows = VGroup()
            for vec in directions.values():
                arrow = Arrow(start=origin, end=scale * vec, color=RED, buff=0)  # standard Arrow works in 3D
                arrows.add(arrow)
            self.play(LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.15))
            self.wait(0.5)

        # Rotate the camera to show the 3D structure
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(10)
        self.stop_ambient_camera_rotation()
 