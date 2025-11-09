from manim import *

circle = Circle()

circle.set_fill(PINK, opacity=0.5) # Sets the fill color to pink with 50% opacity
circle.set_stroke(color=BLUE, width=4) # Sets the stroke color to blue and width to 

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)
        self.play(Create(circle)) # Animates the creation of the circle
        self.wait(1) # Pauses for 1 second
        self.play(circle.animate.shift(RIGHT * 2)) # Animates shifting the circle to the right