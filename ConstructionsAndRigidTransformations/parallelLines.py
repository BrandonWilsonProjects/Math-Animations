from manim import *

class ParallelLinesScene(Scene):
    def construct(self):
        # Set up the parallel lines (horizontal)
        line1 = Line(start=[-6, 2, 0], end=[6, 2, 0], color=WHITE)
        line2 = Line(start=[-6, -2, 0], end=[6, -2, 0], color=WHITE)

        def add_chevron_arrows(line, positions=[0.25, 0.75], symbol=">"):
            arrows = VGroup()
            for alpha in positions:
                pos = line.point_from_proportion(alpha)
                arrow = Text(symbol, font="Arial").scale(0.5)
                arrow.rotate(line.get_angle())  # align with the line
                arrow.move_to(pos)  # slight offset for clarity
                arrows.add(arrow)
            return arrows
        
        # Add arrowheads to indicate parallelism
        arrows1 = add_chevron_arrows(line1)
        arrows2 = add_chevron_arrows(line2)

        # Add labels
        label1 = Text("A").scale(0.5).next_to(line1, RIGHT)
        label2 = Text("B").scale(0.5).next_to(line2, RIGHT)

        # Add to the scene
        self.play(Create(line1), Create(line2))
        self.play(Write(label1), Write(label2))
        self.play(Write(arrows1), Write(arrows2))
        self.wait(3)
