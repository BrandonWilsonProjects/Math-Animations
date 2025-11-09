from manim import *

class GeometricSequence(Scene):
    def construct(self):
        title = Text("Geometric Sequence", font_size=36, color=YELLOW).to_edge(UP)
        self.play(Write(title))

        # Sequence: 1, 2, 4, ?, 16
        numbers = ["1", "2", "4", "?", "16"]
        seq = VGroup(*[Text(num, font_size=40).shift(RIGHT * i * 1.2) for i, num in enumerate(numbers)])
        seq.move_to(DOWN * 0.5)

        self.play(Write(seq))
        self.wait(2)

        closing = Text("What number goes in the blank?", font_size=28, color=GREEN).next_to(seq, DOWN, buff=1)
        self.play(Write(closing))
        self.wait(3)
