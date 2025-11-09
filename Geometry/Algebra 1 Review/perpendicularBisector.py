from manim import *

class PerpendicularBisectorScene(Scene):
    def construct(self):
        # Create two points
        point_A = Dot([-3, -1, 0], color=BLUE)
        point_B = Dot([3, 2, 0], color=RED)
        label_A = Text("A").next_to(point_A, DOWN)
        label_B = Text("B").next_to(point_B, UP)

        # Line segment between A and B
        line_AB = Line(point_A.get_center(), point_B.get_center(), color=WHITE)

        # Midpoint of AB
        midpoint = (point_A.get_center() + point_B.get_center()) / 2
        mid_dot = Dot(midpoint, color=YELLOW)
        label_M = Text("M").next_to(mid_dot, RIGHT)

        # Get vector AB
        vec = point_B.get_center() - point_A.get_center()

        # Get perpendicular direction by rotating 90 degrees
        perp_direction = rotate_vector(vec, angle=PI/2)
        perp_unit = perp_direction / np.linalg.norm(perp_direction)

        # Create the perpendicular bisector line centered at midpoint
        length = 4  # Length of the bisector
        start = midpoint - length/2 * perp_unit
        end = midpoint + length/2 * perp_unit
        perp_bisector = Line(start, end, color=GREEN)
        
        right_angle = RightAngle(line_AB, perp_bisector, length=0.4, quadrant=(1, 1), color=ORANGE)


        # Add all elements to the scene
        self.play(Create(point_A), Write(label_A),
                  Create(point_B), Write(label_B))
        self.play(Create(line_AB))
        self.play(Create(mid_dot), Write(label_M))
        self.play(Create(perp_bisector))
        self.play(Create(right_angle))

        # Hold the scene
        self.wait(2)