from manim import *

class TwoCirclesDiameters(Scene):
    def construct(self):
        title = Text("Two Circles with Diameters EA and EB", font_size=36, color=YELLOW).to_edge(UP)
        self.play(Write(title))

        # Shared point E
        E = Dot(ORIGIN, color=ORANGE)
        labelE = Text("E", font_size=24, color=ORANGE).next_to(E, DOWN)

        # Circle 1 (left) centered at (-2,0) with E on its circumference
        circle1 = Circle(radius=2, color=BLUE).move_to(LEFT*2)
        # Find point A opposite E on circle1 (diameter EA)
        A = Dot(circle1.point_at_angle(PI), color=BLUE)  # opposite E direction
        labelA = Text("A", font_size=24, color=BLUE).next_to(A, LEFT)
        EA = Line(E.get_center(), A.get_center(), color=WHITE)

        # Circle 2 (right) centered at (2,0) with E on its circumference
        circle2 = Circle(radius=2, color=GREEN).move_to(RIGHT*2)
        # Find point B opposite E on circle2 (diameter EB)
        B = Dot(circle2.point_at_angle(0), color=GREEN)  # opposite E direction
        labelB = Text("B", font_size=24, color=GREEN).next_to(B, RIGHT)
        EB = Line(E.get_center(), B.get_center(), color=WHITE)

        # Animate circles and diameters
        self.play(Create(circle1), Create(circle2))
        self.play(FadeIn(E), Write(labelE))
        self.play(Create(EA), FadeIn(A), Write(labelA))
        self.play(Create(EB), FadeIn(B), Write(labelB))

        # Closing text
        relation = Text("EA and EB are diameters of their circles, sharing E", 
                        font_size=28, color=YELLOW).to_edge(DOWN)
        self.play(Write(relation))
        self.wait(3)
