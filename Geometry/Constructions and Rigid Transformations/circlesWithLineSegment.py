from manim import *

class TwoCirclesSharedRadius(Scene):
    def construct(self):
        title = Text("Two Circles Sharing a Radius", font_size=36, color=YELLOW).to_edge(UP)
        self.play(Write(title))

        # Circle radius
        radius = 2

        # Define centers
        center1 = LEFT * 2
        center2 = RIGHT * 2

        # Circles with same radius
        circle1 = Circle(radius=radius, color=BLUE).move_to(center1)
        circle2 = Circle(radius=radius, color=GREEN).move_to(center2)

        # Shared radius line (center1 to circumference of circle1, which is center2)
        shared_radius = Line(center1, center2, color=WHITE)

        # Points and labels
        dot1 = Dot(center1, color=BLUE)
        dot2 = Dot(center2, color=GREEN)
        label1 = Text("Center A", font_size=24, color=BLUE).next_to(dot1, DOWN)
        label2 = Text("Center B", font_size=24, color=GREEN).next_to(dot2, DOWN)

        self.play(Create(circle1), FadeIn(dot1), Write(label1))
        self.play(Create(circle2), FadeIn(dot2), Write(label2))
        self.wait(0.5)

        # Highlight the shared radius
        self.play(Create(shared_radius))
        shared_label = Text("Shared Radius", font_size=24, color=WHITE).next_to(shared_radius, UP)
        self.play(Write(shared_label))

        self.wait(3)
