from manim import *
import numpy as np


# ============================================================
# TITLE
# ============================================================
class PolyTitle(Scene):
    def construct(self):
        title = Text("Exploring Polynomial Functions", weight=BOLD).scale(0.9)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))


# ============================================================
# LINEAR FUNCTIONS
# ============================================================
class LinearFunctions(Scene):
    def construct(self):
        linear_title = Text("Linear Functions: f(x) = mx + b", weight=BOLD).scale(0.7)
        self.play(Write(linear_title))
        self.wait(3)
        self.play(FadeOut(linear_title))

        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=8,
            y_length=6,
            axis_config={"include_tip": True, "stroke_width": 2},
        ).shift(DOWN * 0.5)

        self.play(Create(axes))

        linear_func = axes.plot(lambda x: 2*x + 1, x_range=[-5, 5], color=BLUE)
        linear_eq = Text("f(x) = 2x + 1").scale(0.7).to_corner(UR)

        self.play(Create(linear_func), Write(linear_eq))

        explanation = Text(
            "No change in direction — constant rate of change",
            font_size=26
        ).to_corner(UL)

        self.play(Write(explanation))
        self.wait(2)
        self.play(FadeOut(axes, linear_func, linear_eq, explanation))


# ============================================================
# QUADRATICS – BASIC a>1 AND a<1
# ============================================================
class QuadraticBasics(Scene):
    def construct(self):
        quad_title = Text("Quadratic Functions: f(x) = ax² + bx + c", weight=BOLD).scale(0.7)
        self.play(Write(quad_title))
        self.wait(3)
        self.play(FadeOut(quad_title))

        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=8,
            y_length=6,
        ).shift(DOWN * 0.5)

        self.play(Create(axes))

        # a > 1
        quad1 = axes.plot(lambda x: 2*x**2, x_range=[-2.5, 2.5], color=GREEN)
        quad1_eq = Text("f(x) = 2x^2", color=GREEN).scale(0.7).to_corner(UR)

        self.play(Create(quad1), Write(quad1_eq))

        quad_note1 = Text("a > 1: Opens upward, narrow", font_size=28).to_corner(UL)
        self.play(Write(quad_note1))
        self.wait(1.5)

        # a < 1
        quad2 = axes.plot(lambda x: 0.3*x**2, x_range=[-4, 4], color=YELLOW)
        quad2_eq = Text("f(x) = 0.3x^2", color=YELLOW).scale(0.7).next_to(quad1_eq, DOWN)

        self.play(FadeOut(quad_note1))
        self.play(Create(quad2), Write(quad2_eq))

        quad_note2 = Text("0 < a < 1: Opens upward, wider", font_size=26).to_corner(UL)
        self.play(Write(quad_note2))
        self.wait(2)

        self.play(FadeOut(axes, quad2, quad2_eq, quad_note2, quad1, quad1_eq))

# ============================================================
# QUADRATICS — DYNAMIC A-VALUE
# ============================================================
class QuadraticAValue(Scene):
    def construct(self):

        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=8,
            y_length=6,
        ).shift(DOWN * 0.5)

        changing_label = Text("Increasing 'a' value:", font_size=32, weight=BOLD).to_corner(UL)
        self.play(Create(axes))
        self.play(Write(changing_label))

        a_tracker = ValueTracker(0.5)

        quad_changing = always_redraw(
            lambda: axes.plot(lambda x: a_tracker.get_value()*x**2, x_range=[-3, 3], color=BLUE)
        )
        a_label = always_redraw(
            lambda: Text(f"a = {a_tracker.get_value():.1f}").scale(0.7).to_corner(UR)
        )

        self.play(Create(quad_changing), Write(a_label))
        self.wait(0.5)

        self.play(a_tracker.animate.set_value(3), run_time=3)
        self.wait(1)


# ============================================================
# QUADRATICS — SHIFTING
# ============================================================
class QuadraticShifts(Scene):
    def construct(self):

        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=8,
            y_length=6,
        ).shift(DOWN * 0.5)

        shift_label = Text("Shifting the parabola:", font_size=32, weight=BOLD).to_corner(UL)
        self.play(Create(axes))
        self.play(Write(shift_label))

        h_tracker = ValueTracker(0)
        k_tracker = ValueTracker(0)

        quad_shift = always_redraw(
            lambda: axes.plot(
                lambda x: (x - h_tracker.get_value())**2 + k_tracker.get_value(),
                x_range=[-5, 5],
                color=RED
            )
        )

        shift_eq = always_redraw(
            lambda: Text(
                f"f(x) = (x {'-' if h_tracker.get_value()>=0 else '+'} {abs(h_tracker.get_value()):.1f})²"
                f" {'+' if k_tracker.get_value()>=0 else '-'} {abs(k_tracker.get_value()):.1f}"
            ).scale(0.6).to_corner(UR)
        )

        self.play(Create(quad_shift), Write(shift_eq))

        # Animate shifts
        self.play(h_tracker.animate.set_value(2), run_time=2)
        self.play(h_tracker.animate.set_value(-2), run_time=2)
        self.play(h_tracker.animate.set_value(0), run_time=1)
        self.play(k_tracker.animate.set_value(2), run_time=2)
        self.play(k_tracker.animate.set_value(-2), run_time=2)
        self.play(k_tracker.animate.set_value(0), run_time=1)

        note = Text(
            "h shifts horizontally (inside parentheses)\nk shifts vertically",
            font_size=24
        ).to_corner(UL)

        self.play(FadeOut(shift_label), Write(note))
        self.wait(2)


# ============================================================
# CUBICS
# ============================================================
class CubicFunctions(Scene):
    def construct(self):
        title = Text("Exploring Polynomial Functions", weight=BOLD).scale(0.9)
        cubic_title = Text("Cubic Functions: f(x) = ax³ + bx² + cx + d", weight=BOLD).scale(0.7)
        cubic_title.next_to(title, DOWN, buff=0.5)

        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=8,
            y_length=6,
        ).shift(DOWN * 0.5)

        self.play(Write(title))
        self.play(Write(cubic_title))
        self.play(Create(axes))

        cubic1 = axes.plot(lambda x: 0.5*x**3, x_range=[-2.5, 2.5], color=PURPLE)
        cubic1_eq = Text("f(x) = 0.5x^3", color=PURPLE).scale(0.7).to_corner(UR)

        self.play(Create(cubic1), Write(cubic1_eq))
        note1 = Text("a > 0: Rises to the right", font_size=28).next_to(axes, DOWN)
        self.play(Write(note1))
        self.wait(1.5)

        cubic2 = axes.plot(lambda x: -0.5*x**3, x_range=[-2.5, 2.5], color=ORANGE)
        cubic2_eq = Text("f(x) = -0.5x^3", color=ORANGE).scale(0.7).next_to(cubic1_eq, DOWN)

        self.play(FadeOut(note1))
        self.play(Create(cubic2), Write(cubic2_eq))

        note2 = Text("a < 0: Falls to the right (reflected)", font_size=28).next_to(axes, DOWN)
        self.play(Write(note2))
        self.wait(2)


# ============================================================
# QUARTICS
# ============================================================
class QuarticFunctions(Scene):
    def construct(self):
        title = Text("Exploring Polynomial Functions", weight=BOLD).scale(0.9)
        quartic_title = Text("Quartic Functions: f(x) = ax⁴ + ...", weight=BOLD).scale(0.7)
        quartic_title.next_to(title, DOWN, buff=0.5)

        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=8,
            y_length=6,
        ).shift(DOWN * 0.5)

        self.play(Write(title))
        self.play(Write(quartic_title))
        self.play(Create(axes))

        quartic1 = axes.plot(lambda x: 0.2*x**4, x_range=[-2.5, 2.5], color=MAROON)
        eq1 = Text("f(x) = 0.2x^4", color=MAROON).scale(0.7).to_corner(UR)

        self.play(Create(quartic1), Write(eq1))
        note1 = Text("a > 0: Opens upward (W-shape)", font_size=28).next_to(axes, DOWN)
        self.play(Write(note1))
        self.wait(2)

        quartic2 = axes.plot(lambda x: -0.2*x**4, x_range=[-2.5, 2.5], color=PINK)
        eq2 = Text("f(x) = -0.2x^4", color=PINK).scale(0.7).next_to(eq1, DOWN)

        self.play(FadeOut(note1))
        self.play(Create(quartic2), Write(eq2))

        note2 = Text("a < 0: Opens downward (M-shape)", font_size=28).next_to(axes, DOWN)
        self.play(Write(note2))
        self.wait(2)
