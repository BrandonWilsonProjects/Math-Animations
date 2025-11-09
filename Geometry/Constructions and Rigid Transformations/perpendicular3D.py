from manim import *

class PerpendicularBisector3DRotation(ThreeDScene):
    def construct(self):
        # Title (fixed in frame, doesn’t rotate with camera)
        title = Text("Perpendicular Bisector in 3D", font_size=40, color=YELLOW).to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))

        # Initial camera angle
        self.set_camera_orientation(phi=60 * DEGREES, theta=30 * DEGREES)

        # Define two points A and B in 3D
        A = np.array([-2, 0, 0])
        B = np.array([2, 0, 0])

        dot_A = Dot3D(A, color=RED)
        label_A = Text("A", font_size=28, color=RED).move_to(A + DOWN*0.5)
        self.add_fixed_orientation_mobjects(label_A)

        dot_B = Dot3D(B, color=RED)
        label_B = Text("B", font_size=28, color=RED).move_to(B + DOWN*0.5)
        self.add_fixed_orientation_mobjects(label_B)

        segment = Line3D(A, B, color=WHITE)

        self.play(Create(dot_A), Write(label_A), Create(dot_B), Write(label_B))
        self.play(Create(segment))

        # Midpoint
        midpoint = (A + B) / 2
        dot_M = Dot3D(midpoint, color=BLUE)
        label_M = Text("M", font_size=28, color=BLUE).move_to(midpoint + UP*0.5)
        self.add_fixed_orientation_mobjects(label_M)
        self.play(FadeIn(dot_M), Write(label_M))

        # Perpendicular bisector plane
        bisector_plane = Rectangle(color=GREEN, fill_opacity=0.3, stroke_opacity=0.6)
        bisector_plane.set_width(2).set_height(2)
        bisector_plane.rotate(PI/2, axis=UP)  # vertical plane in yz-plane
        bisector_plane.move_to(midpoint)
        self.play(FadeIn(bisector_plane))

        # Equidistant points with dashed lines
        points = [
            np.array([0, 2, 0]),
            np.array([0, -2, 1]),
            np.array([0, 1, -2])
        ]
        for p in points:
            dot = Dot3D(p, color=YELLOW)
            line_to_A = DashedLine(p, A, color=YELLOW)
            line_to_B = DashedLine(p, B, color=YELLOW)
            self.play(FadeIn(dot), Create(line_to_A), Create(line_to_B))

        # --- Continuous rotation ---
        self.begin_3dillusion_camera_rotation(rate=0.2)  # slow constant rotation
        self.wait(12)  # adjust for length of animation
        self.stop_3dillusion_camera_rotation()
