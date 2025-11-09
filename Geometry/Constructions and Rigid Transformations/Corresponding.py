from manim import *

class CorrespondingAnglesCorrect(Scene):
    def construct(self):
        # Title and definition
        title = Text("Corresponding Angles", font_size=36, color=YELLOW).to_edge(UP)
        definition = Text(
            "Angles in matching corners when a transversal crosses parallel lines.",
            font_size=26
        ).next_to(title, DOWN)
        self.play(Write(title), FadeIn(definition))
        self.wait(1)

        # Parallel lines
        top_line = Line(LEFT*5, RIGHT*5).shift(UP*1.5)
        bottom_line = Line(LEFT*5, RIGHT*5).shift(DOWN*1.5)
        self.play(Create(top_line), Create(bottom_line))

        # Transversal (intersecting both lines)
        trans = Line(LEFT*5, RIGHT*5).rotate(PI/4)
        self.play(Create(trans))
        self.wait(0.5)

        # Find intersection points
        top_intersection = Line.intersection(top_line, trans)
        bottom_intersection = Line.intersection(bottom_line, trans)

        # Place small dots at intersections for clarity
        dot_top = Dot(top_intersection, color=WHITE)
        dot_bottom = Dot(bottom_intersection, color=WHITE)
        self.play(FadeIn(dot_top), FadeIn(dot_bottom))

        # Angles at intersections (same orientation)
        # Upper intersection - below top line, right side of transversal
        upper_angle = Angle(trans, top_line, radius=0.6, quadrant=(1), color=BLUE)
        # Lower intersection - above bottom line, right side of transversal
        lower_angle = Angle(trans, bottom_line, radius=0.6, quadrant=(-1), color=BLUE)
        self.play(Create(upper_angle), Create(lower_angle))

        # Labels
        label1 = Text("∠1", font_size=28, color=BLUE).next_to(upper_angle, RIGHT*0.4+DOWN*0.2)
        label2 = Text("∠2", font_size=28, color=BLUE).next_to(lower_angle, RIGHT*0.4+UP*0.2)
        self.play(Write(label1), Write(label2))

        # Explanation text
        explain = Text("∠1 and ∠2 are corresponding angles", font_size=28, color=WHITE).to_edge(DOWN)
        self.play(Write(explain))
        self.wait(2)
