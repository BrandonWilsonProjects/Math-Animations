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

        # Show the distance formula with proper mathematical layout
        # Create the main parts
        d_equals = Text("d =", font_size=40, color=YELLOW)
        sqrt_symbol = Text("√", font_size=50, color=YELLOW)

        # The radicand (what's under the square root)
        # Using separate parts for the exponents
        x_part = Text("(x₂ - x₁)", font_size=32, color=YELLOW)
        squared_1 = Text("²", font_size=24, color=YELLOW)
        plus = Text(" + ", font_size=32, color=YELLOW)
        y_part = Text("(y₂ - y₁)", font_size=32, color=YELLOW)
        squared_2 = Text("²", font_size=24, color=YELLOW)

        # Position the radicand parts
        radicand = VGroup(x_part, squared_1, plus, y_part, squared_2).arrange(RIGHT, buff=0.05)
        squared_1.shift(UP * 0.3)
        squared_2.shift(UP * 0.3)

        # Add overline for radicand
        overline = Line(
            radicand.get_left() + UP * 0.35 + LEFT * 0.1,
            radicand.get_right() + UP * 0.35 + RIGHT * 0.1,
            color=YELLOW,
            stroke_width=2
        )
        overline.next_to(sqrt_symbol.get_top(), RIGHT, buff=0.01, aligned_edge=UP).shift(DOWN * 0.03)

        # Position sqrt and radicand
        sqrt_group = VGroup(sqrt_symbol, radicand, overline)
        radicand.next_to(sqrt_symbol, RIGHT, buff=0.1).shift(DOWN * 0.1)

        # Position everything
        d_equals.next_to(panel.get_top(), DOWN, buff=0.3).align_to(panel, LEFT).shift(RIGHT * 0.3)
        sqrt_group.next_to(d_equals, RIGHT, buff=0.3)

        # Animate formula
        self.play(FadeIn(panel))
        self.play(Write(d_equals))
        self.play(Write(sqrt_symbol), Create(overline))
        self.play(Write(x_part), Write(squared_1))
        self.play(Write(plus))
        self.play(Write(y_part), Write(squared_2))
        self.wait(1)

        # Transform to plugged-in values
        x_part_plugged = Text(f"({B[0]} - {A[0]})", font_size=32, color=YELLOW)
        squared_1_plugged = Text("²", font_size=24, color=YELLOW)
        plus_plugged = Text(" + ", font_size=32, color=YELLOW)
        y_part_plugged = Text(f"({B[1]} - {A[1]})", font_size=32, color=YELLOW)
        squared_2_plugged = Text("²", font_size=24, color=YELLOW)
        
        radicand_plugged = VGroup(x_part_plugged, squared_1_plugged, plus_plugged, y_part_plugged, squared_2_plugged).arrange(RIGHT, buff=0.05)
        squared_1_plugged.shift(UP * 0.3)
        squared_2_plugged.shift(UP * 0.3)
        radicand_plugged.next_to(sqrt_symbol, RIGHT, buff=0.1).shift(DOWN * 0.1)
        
        overline_plugged = Line(
            radicand_plugged.get_left() + UP * 0.35 + LEFT * 0.1,
            radicand_plugged.get_right() + UP * 0.35 + RIGHT * 0.1,
            color=YELLOW,
            stroke_width=2
        )
        overline_plugged.next_to(sqrt_symbol.get_top(), RIGHT, buff=0.01, aligned_edge=UP).shift(DOWN * 0.03)
        
        self.play(
            Transform(x_part, x_part_plugged),
            Transform(squared_1, squared_1_plugged),
            Transform(plus, plus_plugged),
            Transform(y_part, y_part_plugged),
            Transform(squared_2, squared_2_plugged),
            Transform(overline, overline_plugged)
        )
        self.wait(1)

        # Show final answer below
        solution = Text(f"d = {d:.2f}", font_size=40, color=GREEN)
        solution.next_to(radicand_plugged, DOWN, buff=0.8)
        self.play(FadeIn(solution))
        self.wait(5)

        # Fade out everything
        self.play(
            FadeOut(axes),
            FadeOut(x_lbl),
            FadeOut(y_lbl),
            FadeOut(A_dot),
            FadeOut(B_dot),
            FadeOut(A_text),
            FadeOut(B_text),
            FadeOut(seg_AB),
            FadeOut(leg_dx),
            FadeOut(leg_dy),
            FadeOut(brace_dx),
            FadeOut(brace_dy),
            FadeOut(dx_label),
            FadeOut(dy_label),
            FadeOut(panel),
            FadeOut(d_equals),
            FadeOut(sqrt_symbol),
            FadeOut(x_part),
            FadeOut(squared_1),
            FadeOut(plus),
            FadeOut(y_part),
            FadeOut(squared_2),
            FadeOut(overline),
            FadeOut(solution)
        )
        self.wait(0.5)
        
        final_text = Text("Distance Formula calculates the shortest distance between 2 points.", color=BLUE, font_size=30)
        self.play(FadeIn(final_text))
        self.wait(2)
        
        final_text2 = Text("What does this formula remind you of?").next_to(final_text, DOWN*1.1)
        self.play(FadeIn(final_text2))
        self.wait(1)
        
        dot1 = Text(".").next_to(final_text2)
        self.play(FadeIn(dot1))
        self.wait(2)
        
        dot2 = Text(".").next_to(dot1)
        self.play(FadeIn(dot2))
        self.wait(2)
        
        final_text3 = Text("Pythagorean Theorem!!").next_to(final_text2, DOWN*1.1)
        self.play(FadeIn(final_text3))
        self.wait(4)
        