from manim import *

class SSSCongruency(Scene):
    def construct(self):
        title = Text("SSS Congruency: Side-Side-Side", font_size=36).to_edge(UP)
        self.play(Write(title))

        # Larger, centered triangles
        tri1 = Polygon([-3,-2,0],[1,-2,0],[-1,3,0], color=BLUE)
        tri1.shift(LEFT*2, DOWN*1)
        tri2 = Polygon([3,-2,0],[7,-2,0],[5,3,0], color=GREEN)
        tri2.shift(LEFT*2, DOWN*1)
        self.play(Create(tri1), Create(tri2))

        # Highlight all three pairs of sides
        sides = VGroup(
            *[Line(tri1.get_vertices()[i], tri1.get_vertices()[(i+1)%3], color=YELLOW) for i in range(3)],
            *[Line(tri2.get_vertices()[i], tri2.get_vertices()[(i+1)%3], color=YELLOW) for i in range(3)]
        )
        self.play(Create(sides))
        self.wait(3)
