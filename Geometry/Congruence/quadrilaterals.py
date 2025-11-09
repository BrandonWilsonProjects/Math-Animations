from manim import *

class QuadrilateralCongruence(Scene):
    def construct(self):
        # ----------------------------------------
        # Title
        # ----------------------------------------
        title = Text("Quadrilateral Congruence", font_size=38).to_edge(UP)
        self.play(Write(title))

        # ----------------------------------------
        # Create first quadrilateral (blue)
        # ----------------------------------------
        quad1_points = [
            LEFT*1.8 + DOWN*0.8,
            LEFT*0.8 + UP*0.8,
            RIGHT*0.8 + UP*0.9,
            RIGHT*1.8 + DOWN*0.8
        ]
        quad1 = Polygon(*quad1_points, color=BLUE, fill_color=BLUE, fill_opacity=0.4)
        quad1.move_to(LEFT*2)  # shift slightly left to center both together
        label1 = Text("Quadrilateral ABCD", font_size=28, color=BLUE).next_to(quad1, DOWN)
        self.play(Create(quad1), Write(label1))
        self.wait(1)

        # ----------------------------------------
        # Create second quadrilateral (green)
        # ----------------------------------------
        quad2_points = [
            LEFT*1.8 + DOWN*0.8,
            LEFT*0.8 + UP*0.8,
            RIGHT*0.8 + UP*0.9,
            RIGHT*1.8 + DOWN*0.8
        ]
        quad2 = Polygon(*quad2_points, color=GREEN, fill_color=GREEN, fill_opacity=0.4)
        quad2.move_to(RIGHT*2)  # shift to the right, mirroring the first one
        label2 = Text("Quadrilateral WXYZ", font_size=28, color=GREEN).next_to(quad2, DOWN)
        self.play(Create(quad2), Write(label2))
        self.wait(1)

        # ----------------------------------------
        # Highlight corresponding sides
        # ----------------------------------------
        side_text = Text("All corresponding sides and angles are equal.", font_size=26).next_to(title, DOWN)
        self.play(Write(side_text))
        self.wait(1)

        # ----------------------------------------
        # Rotate and translate one over the other
        # ----------------------------------------
        congruence_text = Text("Quadrilateral ABCD ≅ Quadrilateral WXYZ", font_size=28).next_to(side_text, DOWN)
        self.play(Write(congruence_text))
        self.wait(1)

        self.play(
            quad2.animate.move_to(quad1.get_center()),
            run_time=3
        )
        self.wait(1)

        # ----------------------------------------
        # Fade out to summary
        # ----------------------------------------
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        conclusion = Text(
            "Quadrilaterals are congruent when all corresponding sides and angles match.\n"
            "Rigid motion (rotation, translation, or reflection) shows their equality.",
            font_size=28
        )
        self.play(Write(conclusion))
        self.wait(4)
