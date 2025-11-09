from manim import *

class SelfCongruence(Scene):
    def construct(self):
        # Title
        title = Text("A Shape is Congruent to Itself", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Triangle vertices
        A = [-2, -1, 0]
        B = [0, 2, 0]
        C = [2, -1, 0]

        # Triangle
        tri = Polygon(A, B, C, color=BLUE, fill_opacity=0.6)
        self.play(Create(tri))
        self.wait(1)

        # Label sides with tick marks
        side1 = Line(A, B)
        side2 = Line(B, C)
        side3 = Line(C, A)

        tick1 = Text("‖", font_size=30, color=YELLOW).move_to(side1.get_center())
        tick2 = Text("‖", font_size=30, color=YELLOW).move_to(side2.get_center())
        tick3 = Text("‖", font_size=30, color=YELLOW).move_to(side3.get_center())

        self.play(Write(tick1), Write(tick2), Write(tick3))
        self.wait(1)

        # Congruence statement
        statement = Text("All sides ≅, All angles ≅ → Shape ≅ itself",
                         font_size=28, color=YELLOW).to_edge(DOWN)
        self.play(Write(statement))
        self.wait(3)
