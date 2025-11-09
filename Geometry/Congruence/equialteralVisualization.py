from manim import *

class EquilateralTriangle(Scene):
    def construct(self):
        # Title
        title = Text("Equilateral Triangle", font_size=42)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Triangle
        triangle = Polygon(
            [-2, -1, 0], [0, 2, 0], [2, -1, 0],
            color=TEAL, fill_opacity=0.5
        )
        self.play(Create(triangle))
        self.wait(1)

        label = Text("All sides and angles are equal", font_size=28).next_to(triangle, DOWN)
        self.play(Write(label))
        self.wait(1)

        # Vertices
        v_left, v_top, v_right = triangle.get_vertices()

        # Highlight equal sides
        left_side = Line(v_left, v_top, color=YELLOW)
        right_side = Line(v_right, v_top, color=YELLOW)
        base = Line(v_left, v_right, color=WHITE)
        self.play(Create(left_side), Create(right_side), Create(base))
        self.wait(1)

        # === Clean interior arcs using from_three_points ===
        # Slight offsets keep them visually inside
        r = 0.3  # arc radius
        eps = 0.08  # tiny offset to prevent overlap

        # Left base angle ∠top-left-right
        left_angle = Angle.from_three_points(
            v_right + DOWN * 0.05,
            v_left,
            v_top + LEFT * 0.05,
            radius=0.3,
            color=RED,
            stroke_width=5,
        )

        # Right base angle ∠top-right-left (NOTE reversed order fixes orientation)
        right_angle = Angle.from_three_points(
            v_top + RIGHT * eps,
            v_right,
            v_left + DOWN * eps,
            radius=r,
            color=RED,
            stroke_width=5,
        )

        # Top angle ∠left-top-right
        top_angle = Angle.from_three_points(
            v_left + UP * eps,
            v_top,
            v_right + UP * eps,
            radius=r,
            color=RED,
            stroke_width=5,
        )

        self.play(Create(left_angle), Create(right_angle), Create(top_angle))
        self.wait(1)

        # Summary
        summary = Text(
            "An equilateral triangle has all sides and all angles congruent (each 60°).",
            font_size=30
        ).to_edge(DOWN)
        self.play(Write(summary))
        self.wait(3)
