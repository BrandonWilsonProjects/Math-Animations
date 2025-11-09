from manim import *

class GeometricSequenceNoLatex(Scene):
    def construct(self):
        # Title
        title = Text("Geometric Sequence", font_size=48, color=YELLOW).to_edge(UP)
        self.play(Write(title))

        # Formula in plain text
        formula = Text("General Formula: an = a1 * r^(n - 1)", font_size=32, color=BLUE)
        formula.next_to(title, DOWN)
        self.play(Write(formula))

        # Example values
        a1 = 2   # first term
        r = 3    # common ratio
        example = Text(f"Example: a1 = {a1}, r = {r}", font_size=28, color=WHITE).next_to(formula, DOWN)
        self.play(Write(example))

        # Custom number line
        line_start = LEFT * 5
        line_end = RIGHT * 5
        line = Line(line_start, line_end, color=WHITE)
        self.play(Create(line))

        # Manual ticks and labels (plain Text)
        num_ticks = 11
        for i in range(num_ticks):
            pos = line_start + (i / (num_ticks - 1)) * (line_end - line_start)
            tick = Line(pos + UP*0.1, pos + DOWN*0.1, color=WHITE)
            value = int(i * 20)  # spacing of 20 units
            label = Text(str(value), font_size=20, color=WHITE).next_to(tick, DOWN)
            self.play(Create(tick), Write(label))

        # Sequence points (first 5 terms)
        sequence_points = []
        for n in range(1, 6):
            an = a1 * (r ** (n - 1))  # geometric term
            # map values 0–200 into the line
            x_pos = line_start + (an / 200) * (line_end - line_start)
            dot = Dot(x_pos, color=RED)
            label_text = f"a{n}={an}"
            # Alternate above/below placement
            if n % 2 == 0:
                label = Text(label_text, font_size=20, color=RED).next_to(dot, UP)
            else:
                label = Text(label_text, font_size=20, color=RED).next_to(dot, DOWN*4)
            sequence_points.append((dot, label))

        # Animate points one by one
        for dot, label in sequence_points:
            self.play(FadeIn(dot, scale=0.5))
            self.play(Write(label))
            self.wait(0.3)

        # Closing remark
        conclusion = Text(
            "Each term is found by multiplying the previous term by r",
            font_size=28, color=YELLOW
        ).next_to(line, DOWN*6)
        self.play(Write(conclusion))
        self.wait(2)
