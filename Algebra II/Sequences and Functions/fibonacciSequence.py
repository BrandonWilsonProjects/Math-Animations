from manim import *

class FibonacciSequence(Scene):
    def construct(self):
        title = Text("Fibonacci Sequence", font_size=36, color=YELLOW).to_edge(UP)
        self.play(Write(title))

        # Sequence: 1, 1, 2, 3, ?, 8
        numbers = ["1", "1", "2", "3", "?", "8"]
        seq = VGroup(*[Text(num, font_size=40).shift(RIGHT * i * 1.2) for i, num in enumerate(numbers)])
        seq.move_to(DOWN * 0.5)

        self.play(Write(seq))
        self.wait(2)

        closing = Text("Fill in the missing Fibonacci number!", font_size=28, color=ORANGE).next_to(seq, DOWN, buff=1)
        self.play(Write(closing))
        self.wait(3)
