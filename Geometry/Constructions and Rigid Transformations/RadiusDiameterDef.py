from manim import *

class DiameterAndRadius(Scene):
    def construct(self):
        # ------------------------------------------------
        # STEP 1: Show the first circle with diameter
        # ------------------------------------------------
        title = Text("Diameter and Radius", font_size=36).to_edge(UP)
        self.play(Write(title))

        circle1 = Circle(radius=1.5, color=BLUE)
        diameter_line = Line(circle1.point_from_proportion(0.25), circle1.point_from_proportion(0.75), color=YELLOW)
        label_diameter = Text("Diameter", font_size=28, color=YELLOW).next_to(diameter_line, UP)

        self.play(Create(circle1))
        self.play(Create(diameter_line))
        self.play(Write(label_diameter))
        self.wait(2)

        # ------------------------------------------------
        # STEP 2: Remove circle and show diameter definition
        # ------------------------------------------------
        self.play(FadeOut(circle1), FadeOut(diameter_line), FadeOut(label_diameter))
        def_diameter = Text(
            "Diameter: A line that passes through the center\nand touches the circle at two points.",
            font_size=30
        ).move_to(ORIGIN)
        self.play(Write(def_diameter))
        self.wait(3)
        self.play(FadeOut(def_diameter))

        # ------------------------------------------------
        # STEP 3: Show the second circle with radius
        # ------------------------------------------------
        circle2 = Circle(radius=1.5, color=BLUE)
        radius_line = Line(circle2.get_center(), circle2.point_from_proportion(0.1), color=GREEN)
        label_radius = Text("Radius", font_size=28, color=GREEN).next_to(radius_line, UP*3)

        self.play(Create(circle2))
        self.play(Create(radius_line))
        self.play(Write(label_radius))
        self.wait(2)

        # ------------------------------------------------
        # STEP 4: Remove circle and show radius definition
        # ------------------------------------------------
        self.play(FadeOut(circle2), FadeOut(radius_line), FadeOut(label_radius))
        def_radius = Text(
            "Radius: A line from the center to any point\non the edge of the circle.",
            font_size=30
        ).move_to(ORIGIN)
        self.play(Write(def_radius))
        self.wait(3)
        self.play(FadeOut(def_radius))

        # ------------------------------------------------
        # End Text
        # ------------------------------------------------
        summary = Text("Both diameter and radius describe distance in a circle.", font_size=30, color=YELLOW)
        summary.to_edge(DOWN)
        self.play(Write(summary))
        self.wait(3)
