from manim import *

class CongruentShapes(Scene):
    def construct(self):
        # Title
        title = Text("Congruent Shapes", font_size=36).to_edge(UP)
        self.play(Write(title))

        # First triangle
        tri1 = Polygon([-2, -1, 0], [-1, 1, 0], [0, -1, 0],
                       color=BLUE, fill_opacity=0.6)
        tri1_label = Text("Triangle A", font_size=24, color=BLUE).next_to(tri1, DOWN)

        # Second triangle (same size/shape, shifted right)
        tri2 = Polygon([2, -1, 0], [3, 1, 0], [4, -1, 0],
                       color=GREEN, fill_opacity=0.6)
        tri2_label = Text("Triangle B", font_size=24, color=GREEN).next_to(tri2, DOWN)

        self.play(FadeIn(tri1), Write(tri1_label))
        self.play(FadeIn(tri2), Write(tri2_label))
        self.wait(1)

        # Arrow + congruence statement
        arrow = Arrow(start=tri1.get_right(), end=tri2.get_left(), buff=0.2, color=YELLOW)
        congruent_text = Text("≅", font_size=48, color=YELLOW).next_to(arrow, UP)

        self.play(GrowArrow(arrow), Write(congruent_text))
        self.wait(2)

        # Transform one triangle onto the other (show congruence)
        self.play(Rotate(tri1, angle=PI, about_point=[-1, 0, 0]), run_time=1.5)
        self.play(tri1.animate.move_to(tri2.get_center()), run_time=1.5)
        self.wait(2)

        # Highlight message
        closing = Text("Triangle A ≅ Triangle B", font_size=32, color=YELLOW).to_edge(DOWN)
        self.play(Write(closing))
        self.wait(3)
