from manim import *

class LineSegment(Scene):
    def construct(self):
        title = Text("A Line Segment", font_size=36, color=YELLOW).to_edge(UP)
        self.play(Write(title))

        # Define points
        A = Dot([-3, 0, 0], color=RED)
        B = Dot([3, 0, 0], color=RED)

        line = Line(A.get_center(), B.get_center(), color=WHITE)

        # Labels
        label_A = Text("A", font_size=28, color=RED).next_to(A, DOWN)
        label_B = Text("B", font_size=28, color=RED).next_to(B, DOWN)

        self.play(FadeIn(A), FadeIn(B))
        self.play(Create(line))
        self.play(Write(label_A), Write(label_B))
        self.wait(2)
