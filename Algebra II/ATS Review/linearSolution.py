from manim import *
import numpy as np

class GraphicalIntersection(Scene):
    def construct(self):
        # Axes
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

        label1 = Text("2x + 3y = 8", font="Consolas").scale(0.5).set_color(BLUE_D)
        label2 = Text("5x - 6y = -7", font="Consolas").scale(0.5).set_color(GREEN_D)
        label1.next_to(line1.get_center(), UP)
        label2.next_to(line2.get_center(), DOWN)

        self.play(Create(line1))
        self.play(Write(label1))
        self.play(Create(line2))
        self.play(Write(label2))
        self.wait(0.3)

        # Compute and show the intersection (unique solution)
        # (This system solves to (x, y) = (1, 2))
        x_sol, y_sol = 1, 2
        P = axes.coords_to_point(x_sol, y_sol)
        dot = Dot(P, color=YELLOW).scale(1.1)
        pulse = SurroundingRectangle(dot, color=YELLOW, buff=0.08).set_stroke(width=2)

        # Guidelines to axes (to "read off" coordinates)
        vx = DashedLine(P, axes.coords_to_point(x_sol, 0), stroke_opacity=0.6)
        vy = DashedLine(P, axes.coords_to_point(0, y_sol), stroke_opacity=0.6)
        x_tick = Text("1", font="Consolas").scale(0.5).next_to(axes.coords_to_point(x_sol, 0), DOWN)
        y_tick = Text("2", font="Consolas").scale(0.5).next_to(axes.coords_to_point(0, y_sol), LEFT)

        # Caption: what it means
        caption = Text("Unique solution = intersection point", weight=BOLD).scale(0.6)
        caption.to_edge(UP)

        self.play(FadeIn(caption, shift=DOWN*0.2))
        self.play(FadeIn(dot), Create(pulse))
        self.play(Create(vx), Create(vy), FadeIn(x_tick), FadeIn(y_tick))
        self.wait(0.4)

        # Emphasize that both line equations are satisfied at this point
        callout = VGroup(
            Text("Point lies on both lines", weight=BOLD).scale(0.5),
            Text("→ satisfies both equations simultaneously", slant=ITALIC).scale(0.45),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        callout_bg = RoundedRectangle(corner_radius=0.2, height=callout.height+0.5, width=callout.width+0.6)\
            .set_stroke(width=1).set_fill(color=BLACK, opacity=0.2)
        callout_group = VGroup(callout_bg, callout)
        callout_group.next_to(dot, RIGHT, buff=1.5).shift(RIGHT * 1.2)
        self.play(FadeIn(callout_group, shift=RIGHT*0.2))

        # Final highlight on the point (x, y) = (1, 2)
        sol_text = Text("Solution: (1, 2)", font="Consolas").scale(0.4).set_color(YELLOW)
        sol_text.next_to(dot, UP, buff=0.6).shift(UP*0.3)
        self.play(Write(sol_text), Flash(dot, color=YELLOW))
        self.wait(0.8)
