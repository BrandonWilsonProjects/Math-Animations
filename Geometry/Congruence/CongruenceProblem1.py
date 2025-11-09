from manim import *

class CongruenceProblem1(Scene):
    def construct(self):
        title = Text("Practice Problem 1: Are the triangles congruent?", font_size=32).to_edge(UP)
        self.play(Write(title))

        # Triangle A (left)
        A1 = Polygon([-3, -1, 0], [-2, 1, 0], [-1, -1, 0], color=BLUE, fill_opacity=0.5)
        self.play(Create(A1))
        tick1 = Text("‖", font_size=24, color=YELLOW).move_to(Line([-3,-1,0],[-2,1,0]).get_center())
        tick2 = Text("‖", font_size=24, color=YELLOW).move_to(Line([-2,1,0],[-1,-1,0]).get_center())
        tick3 = Text("‖", font_size=24, color=YELLOW).move_to(Line([-1,-1,0],[-3,-1,0]).get_center())
        self.play(Write(tick1), Write(tick2), Write(tick3))

        # Triangle B (right)
        B1 = Polygon([1, -1, 0], [2, 1, 0], [3, -1, 0], color=GREEN, fill_opacity=0.5)
        self.play(Create(B1))
        tick4 = Text("‖", font_size=24, color=YELLOW).move_to(Line([1,-1,0],[2,1,0]).get_center())
        tick5 = Text("‖", font_size=24, color=YELLOW).move_to(Line([2,1,0],[3,-1,0]).get_center())
        tick6 = Text("‖", font_size=24, color=YELLOW).move_to(Line([3,-1,0],[1,-1,0]).get_center())
        self.play(Write(tick4), Write(tick5), Write(tick6))

        # Question text
        q = Text("Are ΔA and ΔB congruent? How do you know...", font_size=28, color=YELLOW).to_edge(DOWN)
        self.play(Write(q))
        self.wait(3)
