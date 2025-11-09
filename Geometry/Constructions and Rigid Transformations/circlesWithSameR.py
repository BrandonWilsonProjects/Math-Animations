from manim import *

class TwoCircles(Scene):
    def construct(self):
        title = Text("Two Circles with Equal Radius", font_size=36, color=YELLOW).to_edge(UP)
        self.play(Write(title))

        # Circle parameters
        radius = 2
        circle1 = Circle(radius=radius, color=BLUE).shift(LEFT * 3)
        circle2 = Circle(radius=radius, color=GREEN).shift(RIGHT * 3)

        # Labels
        label1 = Text("Circle A", font_size=28, color=BLUE).next_to(circle1, DOWN)
        label2 = Text("Circle B", font_size=28, color=GREEN).next_to(circle2, DOWN)

        self.play(Create(circle1), Write(label1))
        self.play(Create(circle2), Write(label2))
        self.wait(2)
