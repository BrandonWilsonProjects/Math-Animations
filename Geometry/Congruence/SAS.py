from manim import *

class SASCongruency(Scene):
    def construct(self):
        title = Text("SAS Congruency: Side-Angle-Side", font_size=36).to_edge(UP)
        self.play(Write(title))

        tri1 = Polygon([-3,-2,0],[1,-2,0],[-1,3,0], color=BLUE)
        tri1.shift(LEFT*2, DOWN*1)
        tri2 = Polygon([3,-2,0],[7,-2,0],[5,3,0], color=GREEN)
        tri2.shift(LEFT*2, DOWN*1)
        self.play(Create(tri1), Create(tri2))

        # Highlight two sides and included angle
        sides = VGroup(
            Line(tri1.get_vertices()[0], tri1.get_vertices()[1], color=YELLOW),
            Line(tri1.get_vertices()[0], tri1.get_vertices()[2], color=YELLOW),
            Line(tri2.get_vertices()[0], tri2.get_vertices()[1], color=YELLOW),
            Line(tri2.get_vertices()[0], tri2.get_vertices()[2], color=YELLOW)
        )
        self.play(Create(sides))

        # Included angle arcs (larger radius)
        arc1 = Arc(radius=0.6, start_angle=0, angle=PI/3).move_arc_center_to(tri1.get_vertices()[0])
        arc2 = Arc(radius=0.6, start_angle=0, angle=PI/3).move_arc_center_to(tri2.get_vertices()[0])
        self.play(Create(arc1), Create(arc2))
        self.wait(3)
