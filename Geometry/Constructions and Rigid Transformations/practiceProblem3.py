from manim import *
import numpy as np

class AngleBisectorTwoTriangles(Scene):
    def construct(self):
        # Title
        title = Text("Practice Problem: Angle Bisector with Two Triangles", 
                     font_size=32, color=YELLOW).to_edge(UP)
        self.play(Write(title))

        # Vertex O at bottom
        O = ORIGIN + DOWN*2

        # Rays forming angle
        left_ray = Line(O, O + UP*2.5 + LEFT*3, color=WHITE)
        right_ray = Line(O, O + UP*2.5 + RIGHT*3, color=WHITE)
        self.play(Create(left_ray), Create(right_ray))

        # Angle bisector ray (splits angle)
        bisector = Line(O, O + UP*3, color=YELLOW)
        self.play(Create(bisector))

        # Build two 30-60-90 triangles
        # Triangle 1 (left)
        A = O + UP*2.5 + LEFT*3
        D = O + UP*3  # intersection with bisector
        tri1 = Polygon(O, A, D, color=WHITE)
        self.play(Create(tri1))

        # Triangle 2 (right)
        B = O + UP*2.5 + RIGHT*3
        tri2 = Polygon(O, B, D, color=WHITE)
        self.play(Create(tri2))

        # Side labels
        side1_label = Text("3x + 6", font_size=24, color=BLUE).move_to((A + D)/2 + LEFT*0.4 + UP*0.3)
        side2_label = Text("4x + 8", font_size=24, color=BLUE).move_to((B + D)/2 + RIGHT*0.4 + UP*0.3)
        self.play(Write(side1_label), Write(side2_label))

        # Prompt
        prompt = Text("Given both are 30-60-90 triangles,\nfind the value of x.", 
                      font_size=28, color=YELLOW).to_edge(DOWN)
        self.play(Write(prompt))

        self.wait(3)
