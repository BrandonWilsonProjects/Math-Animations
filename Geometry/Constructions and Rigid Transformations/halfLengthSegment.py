from manim import *

class OverlappingCircles(Scene):
    def construct(self):
        title = Text("Overlapping Circles: AB is Center-to-Center", font_size=36, color=YELLOW).to_edge(UP)
        self.play(Write(title))

        # Circle radius
        radius = 2.5

        # Define circle centers (slightly overlapping)
        centerA = LEFT * 1.5
        centerB = RIGHT * 1.5

        # Circles
        circle1 = Circle(radius=radius, color=BLUE).move_to(centerA)
        circle2 = Circle(radius=radius, color=GREEN).move_to(centerB)

        self.play(Create(circle1), Create(circle2))

        # --- Line AB (center to center) ---
        A = Dot(centerA, color=BLUE)
        B = Dot(centerB, color=GREEN)
        segAB = Line(A.get_center(), B.get_center(), color=WHITE)

        labelA = Text("A", font_size=24, color=BLUE).next_to(A, DOWN)
        labelB = Text("B", font_size=24, color=GREEN).next_to(B, DOWN)

        self.play(FadeIn(A), FadeIn(B), Create(segAB), Write(labelA), Write(labelB))

        # --- Diameters CD of each circle ---
        # For circle1
        C1 = Dot(centerA + LEFT*radius, color=RED)
        D1 = Dot(centerA + RIGHT*radius, color=RED)
        segCD1 = Line(C1.get_center(), D1.get_center(), color=RED)
        labelC1 = Text("C", font_size=24, color=RED).next_to(C1, DOWN)
        labelD1 = Text("D", font_size=24, color=RED).next_to(D1, DOWN)

        # For circle2
        C2 = Dot(centerB + LEFT*radius, color=ORANGE)
        D2 = Dot(centerB + RIGHT*radius, color=ORANGE)
        segCD2 = Line(C2.get_center(), D2.get_center(), color=ORANGE)
        labelC2 = Text("C", font_size=24, color=ORANGE).next_to(C2, DOWN)
        labelD2 = Text("D", font_size=24, color=ORANGE).next_to(D2, DOWN)

        # Animate diameters
        self.play(Create(segCD1), FadeIn(C1), FadeIn(D1), Write(labelC1), Write(labelD1))
        self.play(Create(segCD2), FadeIn(C2), FadeIn(D2), Write(labelC2), Write(labelD2))

        # Closing text
        relation = Text("AB lies in the overlap, CD is the diameter of both circles", font_size=28, color=YELLOW).to_edge(DOWN)
        self.play(Write(relation))
        self.wait(3)
