from manim import *

class HLCongruency(Scene):
    def construct(self):
        title = Text("HL Congruency: Hypotenuse-Leg Theorem", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Right triangles - larger and centered
        tri1 = Polygon([-4,-2,0],[0,-2,0],[-4,2,0], color=BLUE)   # left triangle
        tri2 = Polygon([2,-2,0],[6,-2,0],[2,2,0], color=GREEN)   # right triangle
        self.play(Create(tri1), Create(tri2))

        # Highlight hypotenuses
        hypo1 = Line([0,-2,0],[-4,2,0], color=YELLOW, stroke_width=8)
        hypo2 = Line([6,-2,0],[2,2,0], color=YELLOW, stroke_width=8)
        self.play(Create(hypo1), Create(hypo2))

        # Hypotenuse labels
        hypo_label1 = Text("Hypotenuse", font_size=24).next_to(hypo1, UP)
        hypo_label2 = Text("Hypotenuse", font_size=24).next_to(hypo2, UP)
        self.play(Write(hypo_label1), Write(hypo_label2))

        # Highlight one leg
        leg1 = Line([-4,-2,0],[0,-2,0], color=ORANGE, stroke_width=8)
        leg2 = Line([2,-2,0],[6,-2,0], color=ORANGE, stroke_width=8)
        self.play(Create(leg1), Create(leg2))

        # Leg labels
        leg_label1 = Text("Leg", font_size=24).next_to(leg1, DOWN)
        leg_label2 = Text("Leg", font_size=24).next_to(leg2, DOWN)
        self.play(Write(leg_label1), Write(leg_label2))

        # Right angle markers
        right_mark1 = Square(side_length=0.4, stroke_color=WHITE, fill_opacity=0).move_to([-3.8,-1.8,0])
        right_mark2 = Square(side_length=0.4, stroke_color=WHITE, fill_opacity=0).move_to([2.2,-1.8,0])
        self.play(Create(right_mark1), Create(right_mark2))

        # Emphasize congruency
        congruent_text = Text("Hypotenuse and one leg are congruent → Triangles are Congruent!", font_size=28).to_edge(DOWN)
        self.play(Write(congruent_text))

        self.wait(3)
