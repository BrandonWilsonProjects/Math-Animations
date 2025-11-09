from manim import *

class TransversalsAnimation(Scene):
    def construct(self):
        # Create two parallel lines
        line_a = Line(start=LEFT * 5 + UP * 2, end=RIGHT * 5 + UP * 2, color=BLUE)
        line_b = Line(start=LEFT * 5 + DOWN * 2, end=RIGHT * 5 + DOWN * 2, color=BLUE)

        # Create the transversal (diagonal line crossing both)
        transversal = Line(start=LEFT * 3 + UP * 4, end=RIGHT * 3 + DOWN * 4, color=YELLOW)

        # Create labels for the lines
        label_a = Text("Line A", font_size=36, color=BLUE).next_to(line_a, UP)
        label_b = Text("Line B", font_size=36, color=BLUE).next_to(line_b, DOWN)
        label_t = Text("Transversal T", font_size=36, color=YELLOW).next_to(transversal, RIGHT)

        # Create explanation text
        explanation = Text("A transversal crosses two or more lines.", font_size=32, color=WHITE)
        explanation.to_edge(DOWN)

        # Animate the parallel lines
        self.play(Create(line_a), Write(label_a), run_time=1)
        self.play(Create(line_b), Write(label_b), run_time=1)
        self.wait(1)

        # Animate the transversal
        self.play(Create(transversal), Write(label_t), run_time=1.5)
        self.wait(1)

        # Show the explanation
        self.play(Write(explanation))
        self.wait(3)