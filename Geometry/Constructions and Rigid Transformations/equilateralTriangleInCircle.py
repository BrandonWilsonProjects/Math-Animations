from manim import *

class EquilateralTriangleInCircle(Scene):
    def construct(self):
        # Title
        title = Text("Equilateral Triangle Inscribed in a Circle", font_size=40, color=YELLOW).to_edge(UP)
        self.play(Write(title))

        # Circle (shifted down so it doesn't block the title)
        circle = Circle(radius=3, color=BLUE).shift(DOWN * 0.6)
        self.play(Create(circle))

        # Define vertices of equilateral triangle inscribed in circle
        A = circle.point_at_angle(PI/2)           # Top
        B = circle.point_at_angle(PI/2 + 2*PI/3)  # Bottom left
        C = circle.point_at_angle(PI/2 + 4*PI/3)  # Bottom right

        # Dots and labels
        dot_A = Dot(A, color=RED)
        label_A = Text("A", font_size=28, color=RED).next_to(dot_A, UP)

        dot_B = Dot(B, color=RED)
        label_B = Text("B", font_size=28, color=RED).next_to(dot_B, LEFT)

        dot_C = Dot(C, color=RED)
        label_C = Text("C", font_size=28, color=RED).next_to(dot_C, RIGHT)

        self.play(FadeIn(dot_A), Write(label_A))
        self.play(FadeIn(dot_B), Write(label_B))
        self.play(FadeIn(dot_C), Write(label_C))

        # Draw equilateral triangle
        triangle = Polygon(A, B, C, color=WHITE)
        self.play(Create(triangle))

        # Side labels (approx equal)
        side_label1 = Text("r", font_size=24, color=BLUE).move_to((A+B)/2 + LEFT*0.3)
        side_label2 = Text("r", font_size=24, color=BLUE).move_to((B+C)/2 + DOWN*0.3)
        side_label3 = Text("r", font_size=24, color=BLUE).move_to((A+C)/2 + RIGHT*0.3)
        self.play(Write(side_label1), Write(side_label2), Write(side_label3))

        # ---- Correct INTERIOR angle arcs ----
        # At A: between sides AC and AB
        angle_A = Angle(Line(A, B), Line(A, C), radius=0.5, other_angle=False, color=GREEN)
        angle_A_label = Text("60°", font_size=20, color=GREEN).move_to(A + DOWN*0.7)

        # At B: between sides BA and BC
        angle_B = Angle(Line(B, C), Line(B, A), radius=0.5, other_angle=False, color=GREEN)
        angle_B_label = Text("60°", font_size=20, color=GREEN).move_to(B + UP*0.5 + RIGHT*0.6)

        # At C: between sides CB and CA
        angle_C = Angle(Line(C, A), Line(C, B), radius=0.5, other_angle=False, color=GREEN)
        angle_C_label = Text("60°", font_size=20, color=GREEN).move_to(C + UP*0.5 + LEFT*0.6)

        self.play(Create(angle_A), Write(angle_A_label))
        self.play(Create(angle_B), Write(angle_B_label))
        self.play(Create(angle_C), Write(angle_C_label))
