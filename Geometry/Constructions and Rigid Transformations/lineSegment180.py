from manim import *

class LineSegmentAlways180(Scene):
    def construct(self):
        # -----------------------------------
        # Line segment setup
        # -----------------------------------
        start = LEFT * 2
        end = RIGHT * 2
        line = Line(start, end, color=BLUE)
        self.play(Create(line))

        # Label points
        A = Dot(start, color=YELLOW)
        B = Dot(end, color=YELLOW)
        label_A = Text("A", font_size=28).next_to(A, LEFT)
        label_B = Text("B", font_size=28).next_to(B, RIGHT)

        self.play(FadeIn(A, B), Write(label_A), Write(label_B))
        self.wait(1)

        # -----------------------------------
        # Angle marker (visual 180° arc)
        # -----------------------------------
        vertex = ORIGIN
        line_left = Line(vertex, LEFT * 2, color=BLUE)
        line_right = Line(vertex, RIGHT * 2, color=BLUE)
        arc = Arc(radius=0.8, start_angle=PI, angle=PI, color=RED)
        arc.move_to(vertex)
        label_180 = Text("180°", font_size=28, color=RED).next_to(arc, UP, buff=0.3)

        self.play(Create(arc), Write(label_180))
        self.wait(2)

        # -----------------------------------
        # Rotate line to show orientation doesn’t matter
        # -----------------------------------
        rotation_group = VGroup(line, A, B, label_A, label_B, arc, label_180)
        self.play(Rotate(rotation_group, angle=PI/4, about_point=ORIGIN))
        self.play(Rotate(rotation_group, angle=-PI/2, about_point=ORIGIN))
        self
