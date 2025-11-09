from manim import *

class AASCongruency(Scene):
    def construct(self):
        title = Text("AAS Congruency: Angle-Angle-Side", font_size=36).to_edge(UP)
        self.play(Write(title))

        tri1 = Polygon([-3,-2,0],[1,-2,0],[-1,3,0], color=BLUE)
        tri1.shift(LEFT*2, DOWN*1)
        tri2 = Polygon([3,-2,0],[7,-2,0],[5,3,0], color=GREEN)
        tri2.shift(LEFT*2, DOWN*1)
        self.play(Create(tri1), Create(tri2))

        # Highlight non-included side
        side1 = Line(tri1.get_vertices()[1], tri1.get_vertices()[2], color=YELLOW)
        side2 = Line(tri2.get_vertices()[1], tri2.get_vertices()[2], color=YELLOW)
        self.play(Create(side1), Create(side2))

        # Two highlighted angles
        arc1 = Arc(radius=0.6, start_angle=0, angle=PI/3).move_arc_center_to(tri1.get_vertices()[0])
        arc2 = Arc(radius=0.6, start_angle=0, angle=PI/3).move_arc_center_to(tri2.get_vertices()[0])
        arc3 = Arc(radius=0.6, start_angle=PI, angle=-PI/3).move_arc_center_to(tri1.get_vertices()[1])
        arc4 = Arc(radius=0.6, start_angle=PI, angle=-PI/3).move_arc_center_to(tri2.get_vertices()[1])
        self.play(Create(arc1), Create(arc2), Create(arc3), Create(arc4))
        self.wait(3)
