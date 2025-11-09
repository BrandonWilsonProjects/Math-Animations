from manim import *

class GeometricSequenceProblem(Scene):
    def construct(self):
        # Define the geometric sequence: 2, 4, 8, 16, 32
        sequence = ["2", "4", "8", "?", "32"]
        common_ratio = 2  # Not displayed, but used for the sequence logic

        # Create text objects for each term
        terms = VGroup()
        boxes = VGroup()  # To put boxes around each term
        for i, term in enumerate(sequence):
            text = Text(term, font_size=48)
            box = SurroundingRectangle(text, color=BLUE, buff=0.2)
            terms.add(text)
            boxes.add(box)

        # Arrange terms horizontally
        terms.arrange(RIGHT, buff=1.0)
        boxes.arrange(RIGHT, buff=1.0)

        # Position each box around its corresponding term
        for i, box in enumerate(boxes):
            box.move_to(terms[i].get_center())

        # Create the sequence group (terms and boxes)
        sequence_group = VGroup(terms, boxes)
        sequence_group.move_to(ORIGIN).shift(UP * 1.5)

        # Create the problem prompt
        prompt = Text("What is the missing number?", font_size=36, color=YELLOW)
        prompt.shift(DOWN * 1.5)

        # Animate the sequence appearing one term at a time
        for i in range(len(terms)):
            self.play(Write(terms[i]), Create(boxes[i]), run_time=1)
            self.wait(0.5)

        # Show the prompt
        self.play(Write(prompt))
        self.wait(2)

        # Keep the scene visible for a moment
        self.wait(3)