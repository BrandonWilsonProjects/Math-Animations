from manim import *
import numpy as np

# this file intends to emphasize the importance of linear solutions. 
class GraphicalIntersection(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-1, 6, 1],
            y_range=[-1, 6, 1],
            x_length=7,
            y_length=7,
            axis_config={"include_tip": True, "stroke_width": 2},
        ).to_edge(LEFT, buff=0.7).shift(DOWN*0.2)
        x_label = Text("x").scale(0.5).next_to(axes.x_axis.get_end(), DOWN)
        y_label = Text("y").scale(0.5).next_to(axes.y_axis.get_end(), LEFT)
        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label))

        def f1(x): return (8 - 2*x) / 3
        def f2(x): return (7 + 5*x) / 6

        line1 = axes.plot(f1, x_range=[-1, 6], color=BLUE_D)
        line2 = axes.plot(f2, x_range=[-1, 6], color=GREEN_D)
        self.play(FadeIn(line1, line2))
        self.wait(2)
        
        # Create text first
        text1 = Text("2x + 3y = 8", font="Consolas").scale(0.5).set_color(BLUE_D)
        
        # Create background box sized to the text
        box_bg = RoundedRectangle(
            corner_radius=0.1, 
            height=text1.height + 0.3, 
            width=text1.width + 0.4
        ).set_stroke(width=1).set_fill(color=BLUE, opacity=0.2)
        
        # Group them together with text on top
        box_group1 = VGroup(box_bg, text1)
        text1.move_to(box_bg.get_center())  # Center text in box
        # Position at a specific point on line1 (left side, away from intersection)
        box_group1.move_to(axes.coords_to_point(3.5, f1(3.5))).shift(UP*0.5, RIGHT*1.2)
        self.play(FadeIn(box_group1))
        self.wait(0.3)
        
        # Second box
        text2 = Text("5x - 6y = -7", font="Consolas").scale(0.5).set_color(GREEN_D)
        
        box_bp = RoundedRectangle(
            corner_radius=0.1, 
            height=text2.height + 0.3, 
            width=text2.width + 0.4
        ).set_stroke(width=1).set_fill(color=GREEN, opacity=0.2)
        
        box_group2 = VGroup(box_bp, text2)
        text2.move_to(box_bp.get_center())  # Center text in box
        # Position at a specific point on line2 (right side, away from intersection)
        box_group2.move_to(axes.coords_to_point(4, f2(4))).shift(DOWN*0.5, RIGHT*1.2)
        self.play(FadeIn(box_group2))        
        self.wait(0.3)
        
        x_sol, y_sol = 1, 2
        P = axes.coords_to_point(x_sol, y_sol)
        dot = Dot(P, color=YELLOW).scale(1.1)
        pulse = SurroundingRectangle(dot, color=YELLOW, buff=0.08).set_stroke(width=2)

        vx = DashedLine(P, axes.coords_to_point(x_sol, 0), stroke_opacity=0.6)
        vy = DashedLine(P, axes.coords_to_point(0, y_sol), stroke_opacity=0.6)
        x_tick = Text("1", font="Consolas").scale(0.5).next_to(axes.coords_to_point(x_sol, 0), DOWN)
        y_tick = Text("2", font="Consolas").scale(0.5).next_to(axes.coords_to_point(0, y_sol), LEFT)

        caption = Text("Unique solution = intersection point", weight=BOLD).scale(0.6)
        caption.to_edge(UP)

        self.play(FadeIn(caption, shift=DOWN*0.2))
        self.play(FadeIn(dot), Create(pulse))
        self.play(Create(vx), Create(vy), FadeIn(x_tick), FadeIn(y_tick))
        self.wait(0.4)

        callout = VGroup(
            Text("Point lies on both lines", weight=BOLD).scale(0.5),
            Text("→ satisfies both equations simultaneously", slant=ITALIC).scale(0.45),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        callout_bg = RoundedRectangle(corner_radius=0.2, height=callout.height+0.5, width=callout.width+0.6)\
            .set_stroke(width=1).set_fill(color=BLACK, opacity=0.2)
        callout_group = VGroup(callout_bg, callout)
        callout_group.next_to(dot, RIGHT, buff=1.5).shift(RIGHT * 1.2)
        self.play(FadeIn(callout_group, shift=RIGHT*2.5))

        sol_text = Text("Solution: (1, 2)", font="Consolas").scale(0.32).set_color(YELLOW)
        sol_text.next_to(dot, UP, buff=0.3).shift(UP*0.3)
        self.play(Write(sol_text), Flash(dot, color=YELLOW))
        self.wait(2)
        
        self.play(FadeOut(axes, x_label, y_label, line1, line2, box_group1, box_group2, caption, dot, pulse, vx, vy, x_tick, y_tick, callout_group, sol_text, dot))
        
        summary = VGroup(
            Text("Linear Solutions - The values that satisfy a linear equation or system of equations", font_size=24, weight=BOLD).set_color(ORANGE),
            Text("\nSimplify both sides: Combine any like terms on each side of the equal sign.", font_size=22).shift(DOWN * 0.6),
            Text("\nIsolate the variable term: Use inverse operations (adding or subtracting) to move all \nconstant terms to one side and the variable terms to the other.\n", font_size=22).shift(DOWN * 1.1),
            Text("\nSolve for the variable: Use multiplication or division to get the variable by itself", font_size=22).shift(DOWN * 1.6),
            Text("\nCheck your answer: Substitute the solution back into the\n original equation to ensure it holds true", font_size=22, weight=BOLD).shift(DOWN * 2.1).set_color(ORANGE)
        )
        
        self.play(FadeIn(summary))
        self.wait(7)
        