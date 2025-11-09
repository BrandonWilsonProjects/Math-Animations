from manim import *

class PerpendicularBisectorProblem(Scene):
    def construct(self):
        # Title
        title = Text("Practice Problem: Perpendicular Bisector in a Circle", 
                     font_size=32, color=YELLOW).to_edge(UP)
        self.play(Write(title))

        # Circle with smaller radius (2.5 instead of 5)
        circle = Circle(radius=2.5, color=BLUE).shift(DOWN*1)
        self.play(Create(circle))

        # Center O
        O = circle.get_center()
        dot_O = Dot(O, color=WHITE)
        label_O = Text("O", font_size=20, color=WHITE).next_to(dot_O, DOWN)
        self.play(FadeIn(dot_O), Write(label_O))

        # Points on circle (ends of diameter)
        A = O + LEFT*2.5
        B = O + RIGHT*2.5
        dot_A = Dot(A, color=RED)
        dot_B = Dot(B, color=RED)
        label_A = Text("A", font_size=20, color=RED).next_to(dot_A, LEFT)
        label_B = Text("B", font_size=20, color=RED).next_to(dot_B, RIGHT)
        self.play(FadeIn(dot_A), Write(label_A))
        self.play(FadeIn(dot_B), Write(label_B))

        # Diameter AB
        diameter = Line(A, B, color=WHITE)
        self.play(Create(diameter))

        # Mark the given diameter length
        diameter_label = Text("10", font_size=20, color=BLUE).move_to(O + UP*0.3, RIGHT*0.8)
        self.play(Write(diameter_label))

        # Pick a point C on circle (top)
        C = O + UP*2.5
        dot_C = Dot(C, color=RED)
        label_C = Text("C", font_size=20, color=RED).next_to(dot_C, UP)
        self.play(FadeIn(dot_C), Write(label_C))

        # Radius OC (missing length = x)
        radius_OC = Line(O, C, color=WHITE)
        self.play(Create(radius_OC))

        # Label radius as x
        x_label = Text("x", font_size=20, color=GREEN).move_to(radius_OC.get_center() + RIGHT*0.3)
        self.play(Write(x_label))

        # Perpendicular bisector from O to AB
        perp = Line(O, O + UP*2.5, color=YELLOW, stroke_width=3)
        self.play(Create(perp))

        # Right angle marker at O
        right_angle = Square(side_length=0.2, color=YELLOW, fill_opacity=1)
        right_angle.move_to(O + RIGHT*0.1 + UP*0.1)
        self.play(FadeIn(right_angle))