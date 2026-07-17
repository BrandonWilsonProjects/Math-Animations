from manim import *

class SolveEquationTextOnly(Scene):
    def construct(self):
        # Step 1: Show original equation
        eq1 = Text("5x + 15 = 50", font_size=40).to_edge(UP)
        self.play(Write(eq1))
        self.wait(1)

        # Step 2: Subtract 3 from both sides
        step1_text = Text("Subtract 15 from both sides", font_size=28).next_to(eq1, DOWN)
        eq2 = Text("5x = 35", font_size=40).next_to(step1_text, DOWN, buff=0.5)

        self.play(Write(step1_text))
        self.wait(1)
        self.play(Transform(eq1, eq2))  # Reuse eq1 for transition
        self.wait(1)

        # Step 3: Divide both sides by 2
        step2_text = Text("Divide both sides by 5", font_size=28).next_to(eq1, DOWN)
        eq3 = Text("x = 7", font_size=40).next_to(step2_text, DOWN, buff=0.5)

        self.play(Transform(step1_text, step2_text))
        self.wait(1)
        self.play(Transform(eq1, eq3))  # Reuse eq1 again
        self.wait(1)

        # Step 4: Final answer highlight
        box = SurroundingRectangle(eq1, color=YELLOW)
        self.play(Create(box))
        self.wait(2)
