from manim import *

class AngleBisectorPractice(Scene):
    def construct(self):
        # Title
        title = Text("Practice Problem: Angle Bisector", font_size=36, color=YELLOW).to_edge(UP)
        self.play(Write(title))

        # Vertex point
        O = ORIGIN + DOWN*1  # shift down so text fits
        dot_O = Dot(O, color=WHITE)
        label_O = Text("O", font_size=24, color=WHITE).next_to(dot_O, DOWN)

        # Rays forming the angle (66 degrees total)
        ray1 = Line(O, O + RIGHT*3, color=WHITE)  # base
        ray2 = Line(O, O + UP*2.5 + LEFT*2, color=WHITE)  # other side
        self.play(Create(ray1), Create(ray2))
        self.play(FadeIn(dot_O), Write(label_O))

        # Angle bisector line (splits angle in half)
        bisector = Line(O, O + UP*3 + RIGHT*0.5, color=YELLOW)
        self.play(Create(bisector))

        # Arcs for the angle and its parts
        big_angle = Angle(ray1, ray2, radius=1, other_angle=False, color=BLUE)
        self.play(Create(big_angle))

        arc1 = Angle(ray1, bisector, radius=0.6, other_angle=False, color=GREEN)
        arc2 = Angle(bisector, ray2, radius=0.8, other_angle=False, color=GREEN)
        self.play(Create(arc1), Create(arc2))

        # Labels for the parts
        label_33 = Text("33°", font_size=24, color=GREEN).move_to(arc1.get_center() + UP*0.2 + RIGHT*1)
        label_expr = Text("4x + 1°", font_size=24, color=GREEN).move_to(arc2.get_center() + DOWN*0.1 + LEFT*1)
        self.play(Write(label_33), Write(label_expr))

        # Total angle label
        total_label = Text("∠ = 66°", font_size=26, color=BLUE).move_to(big_angle.get_center() + LEFT*0.5 + DOWN*2)
        self.play(Write(total_label))
        self.wait(3)
