from manim import *

class PerfectSquareCorrectRightAngles(Scene):
    def construct(self):
        # Side length and bottom-left corner
        side = 3
        A = np.array([-2, -1, 0])         
        B = A + RIGHT * side              
        C = B + UP * side                 
        D = A + UP * side                 

        # Create square
        square = Polygon(A, B, C, D, color=WHITE)

        # Add points
        dot_A = Dot(A); label_A = Text("A").scale(0.5).next_to(dot_A, DOWN)
        dot_B = Dot(B); label_B = Text("B").scale(0.5).next_to(dot_B, DOWN)
        dot_C = Dot(C); label_C = Text("C").scale(0.5).next_to(dot_C, UP)
        dot_D = Dot(D); label_D = Text("D").scale(0.5).next_to(dot_D, UP)

        # Right angles at each corner (rotate and orient them perfectly)
        ra_A = RightAngle(Line(A, B), Line(A, D), length=0.3, quadrant=(1, -1), color=BLUE)
        # ra_B = RightAngle(Line(B, C), Line(B, A), length=0.3, quadrant=(1, -1), color=BLUE)
        ra_C = RightAngle(Line(C, D), Line(C, B), length=0.3, quadrant=(1, 1), color=BLUE)
        ra_D = RightAngle(Line(D, A), Line(D, C), length=0.3, quadrant=(-1, 1), color=BLUE)

        # Animate
        self.play(Create(square))
        self.play(FadeIn(dot_A), Write(label_A))
        self.play(FadeIn(dot_B), Write(label_B))
        self.play(FadeIn(dot_C), Write(label_C))
        self.play(FadeIn(dot_D), Write(label_D))
        
        self.play(Create(ra_A), Create(ra_C), Create(ra_D))
        self.wait(2)
