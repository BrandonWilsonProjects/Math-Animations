from manim import *
import math

class DistanceFormulaDemo(Scene):
    def construct(self):
        # Axes (no auto-number labels to avoid LaTeX)
        axes = Axes(
            x_range=[-1, 7, 1],
            y_range=[-1, 6, 1],
            x_length=7,
            y_length=5,
            axis_config={"include_numbers": False, "include_ticks": True, "stroke_width": 2},
        ).to_edge(LEFT, buff=0.8)
        self.play(Create(axes))

        # Axis labels (plain text)
        x_lbl = Text("x", font_size=22).next_to(axes.x_axis.get_right(), DOWN)
        y_lbl = Text("y", font_size=22).next_to(axes.y_axis.get_top(), LEFT)
        self.play(FadeIn(x_lbl), FadeIn(y_lbl))

        # Two points
        A = (1, 1)
        B = (5, 4)
        A_dot = Dot(axes.c2p(*A), color=YELLOW)
        B_dot = Dot(axes.c2p(*B), color=YELLOW)

        # Move A label to the LEFT so it doesn't sit near/over the y-axis
        A_text = Text(f"A{A}", font_size=26).next_to(A_dot, LEFT * 3, buff=0.25).shift(LEFT * 0.2)
        B_text = Text(f"B{B}", font_size=26).next_to(B_dot, UP + RIGHT, buff=0.15)

        self.play(FadeIn(A_dot), FadeIn(B_dot), FadeIn(A_text), FadeIn(B_text))

        # Segment AB
        seg_AB = Line(axes.c2p(*A), axes.c2p(*B), color=WHITE).set_stroke(width=3)
        self.play(Create(seg_AB))

        # Right-triangle legs (dx and dy)
        H_proj = axes.c2p(B[0], A[1])  # horizontal projection
        leg_dx = Line(axes.c2p(*A), H_proj, color=RED).set_stroke(width=4)
        leg_dy = Line(H_proj, axes.c2p(*B), color=GREEN).set_stroke(width=4)
        self.play(Create(leg_dx), Create(leg_dy))

        # Braces and labels for dx, dy
        brace_dx = BraceBetweenPoints(axes.c2p(*A), H_proj, direction=DOWN)
        brace_dy = BraceBetweenPoints(H_proj, axes.c2p(*B), direction=RIGHT)

        dx_val = B[0] - A[0]
        dy_val = B[1] - A[1]

        # Move dx label further DOWN so it's not in the way of the x-axis
        dx_label = Text(f"dx = {B[0]} - {A[0]} = {dx_val}", font_size=24).next_to(brace_dx, DOWN * 2, buff=0.3).shift(DOWN * 0.2)
        dy_label = Text(f"dy = {B[1]} - {A[1]} = {dy_val}", font_size=24).next_to(brace_dy, RIGHT, buff=0.15)

        self.play(GrowFromCenter(brace_dx), FadeIn(dx_label))
        self.play(GrowFromCenter(brace_dy), FadeIn(dy_label))

        # Distance computation panel — move UP to the upper-right so it's out of the way
        d = math.sqrt(dx_val**2 + dy_val**2)
        panel = RoundedRectangle(corner_radius=0.2, width=5.8, height=2.3)\
            .set_fill(BLACK, 0.2).set_stroke(WHITE, 1)
        panel.to_corner(UR).shift(LEFT * 0.4 + DOWN * 0.2)

        line1 = Text("Distance between A and B:", font_size=26, weight=BOLD)
        line2 = Text("d = sqrt( (dx)^2 + (dy)^2 )", font_size=24)
        line3 = Text(f"d = sqrt( ({dx_val})^2 + ({dy_val})^2 ) = sqrt({dx_val**2 + dy_val**2})", font_size=22)
        line4 = Text(f"d ≈ {d:.3f}", font_size=28, weight=BOLD, color=YELLOW)
        text_group = VGroup(line1, line2, line3, line4).arrange(UP * 2, aligned_edge=LEFT, buff=0.15)
        text_group.move_to(panel.get_center())

        self.play(FadeIn(panel), FadeIn(text_group))
        self.wait(1.5)
