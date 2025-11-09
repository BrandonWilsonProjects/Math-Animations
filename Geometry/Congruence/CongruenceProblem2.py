from manim import *

class CongruenceProblem2(Scene):
    def construct(self):
        title = Text("Practice Problem 2: Congruent Quadrilaterals?", font_size=32).to_edge(UP)
        self.play(Write(title))

        # Square A (blue, will grow)
        squareA = Square(side_length=2, color=BLUE, fill_opacity=0.5).shift(LEFT*3)
        self.play(Create(squareA))

        # Square B (green, stays the same, rotated)
        squareB = Square(side_length=2, color=GREEN, fill_opacity=0.5).shift(RIGHT*3).rotate(PI/6)
        self.play(Create(squareB))

        # Congruence symbol
        congruence_text = Text("≅ ?", font_size=48, color=YELLOW).move_to([0,0,0])
        self.play(Write(congruence_text))
        self.wait(1)

        # Gradually scale blue square bigger
        self.play(squareA.animate.scale(1.5), run_time=2)
        self.wait(1)
        self.play(squareA.animate.scale(1.5), run_time=2)
        self.wait(1)

        # Question text
        q = Text("Do they stay congruent as one grows larger?", font_size=28, color=YELLOW).to_edge(DOWN)
        self.play(Write(q))
        self.wait(3)
