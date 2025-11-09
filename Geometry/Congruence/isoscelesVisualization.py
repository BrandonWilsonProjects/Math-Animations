from manim import *

class IsoscelesTriangles(Scene):
    def construct(self):
        # Title
        title = Text("Isosceles Triangles", font_size=42)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Isosceles triangle (upright)
        triangle = Polygon(
            [-2, -1, 0], [0, 2, 0], [2, -1, 0],
            color=BLUE, fill_opacity=0.5
        )
        self.play(Create(triangle))
        self.wait(1)

        label = Text("Two equal sides", font_size=28).next_to(triangle, DOWN)
        self.play(Write(label))
        self.wait(1)

        # Vertices
        v_left, v_top, v_right = triangle.get_vertices()

        # Equal sides + base
        left_side = Line(v_left, v_top, color=YELLOW)
        right_side = Line(v_right, v_top, color=YELLOW)
        base = Line(v_left, v_right, color=WHITE)
        self.play(Create(left_side), Create(right_side), Create(base))
        self.wait(1)
        
        r = 0.3  # arc radius
        eps = 0.08  # tiny offset to prevent overlap

        # ✅ Base angles: Smaller radius, removed quadrant, adjusted stroke_width
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

        self.play(Create(left_angle), Create(right_angle))
        self.wait(1)

        # Label congruent base angles
        congruent_label = Text("Base angles are congruent", font_size=28).next_to(label, DOWN)
        self.play(Write(congruent_label))
        self.wait(2)

        # Final summary
        summary = Text(
            "Isosceles triangles have at least two equal sides and equal base angles.",
            font_size=32
        ).to_edge(DOWN)
        self.play(Write(summary))
        self.wait(3)