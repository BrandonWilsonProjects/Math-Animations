from manim import *

class PerfectSquareRightAngles(Scene):
    def construct(self):
        # Side length and bottom-left corner
        side = 3
        A = np.array([-2, -1, 0])         
        B = A + RIGHT * side              
        C = B + UP * side                 
        D = A + UP * side                 

        # Create square and lines
        square = Polygon(A, B, C, D, color=WHITE)
        line_AB = Line(A, B)
        line_BC = Line(B, C)
        line_CD = Line(C, D)
        line_DA = Line(D, A)

        # Dots and labels
        dot_A = Dot(A); label_A = Text("A").scale(0.5).next_to(dot_A, DOWN)
        dot_B = Dot(B); label_B = Text("B").scale(0.5).next_to(dot_B, DOWN)
        dot_C = Dot(C); label_C = Text("C").scale(0.5).next_to(dot_C, UP)
        dot_D = Dot(D); label_D = Text("D").scale(0.5).next_to(dot_D, UP)
        

        ra_A = RightAngle(Line(A, B), Line(A, D), length=0.3, quadrant=(1, 1), color=BLUE)
        ra_C = RightAngle(Line(C, D), Line(C, B), length=0.3, quadrant=(1, 1), color=BLUE)

        def add_slashes(line, count=1, spacing=0.25, length=0.2):
            slashes = VGroup()
            for i in range(count):
                alpha = (i + 1) / (count + 1)
                point = line.point_from_proportion(alpha)
                direction = line.get_unit_vector()
                perp = np.array([-direction[1], direction[0], 0])
                start = point - (length / 2) * perp
                end = point + (length / 2) * perp
                slash = Line(start, end, color=WHITE)
                slashes.add(slash)
            return slashes
        
                # Add 1 slash to AB and CD
        slashes_AB = add_slashes(line_AB, count=1)
        slashes_CD = add_slashes(line_CD, count=1)

        # Add 2 slashes to AD and BC
        slashes_AD = add_slashes(line_DA, count=1)
        slashes_BC = add_slashes(line_BC, count=1)

        self.play(Create(square))
        self.play(FadeIn(dot_A), Write(label_A))
        self.play(FadeIn(dot_B), Write(label_B))
        self.play(FadeIn(dot_C), Write(label_C))
        self.play(FadeIn(dot_D), Write(label_D))
        self.play(Create(ra_A), Create(ra_C))
        self.play(Create(slashes_AB), Create(slashes_CD), Create(slashes_AD), Create(slashes_BC))
        self.wait(2)