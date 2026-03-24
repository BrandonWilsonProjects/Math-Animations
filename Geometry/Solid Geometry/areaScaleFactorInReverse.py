"""
Manim animation: Area Scale Factor → Linear Scale Factor
Shows that √(new area / old area) = k (the linear scale factor).

Run with:
    manim -pql area_scale_factor.py AreaScaleFactor
    # or for high quality:
    manim -pqh area_scale_factor.py AreaScaleFactor
"""

from manim import *


class AreaScaleFactor(Scene):
    def construct(self):
        # ── Title ─────────────────────────────────────────────────────
        title    = Text("Area Scale Factor & Scale Factor", font_size=42, color=BLUE)
        subtitle = Text(r"√(new area ÷ old area)  =  k", font_size=28, color=YELLOW)
        subtitle.next_to(title, DOWN, buff=0.4)

        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle, shift=UP * 0.3))
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(subtitle))

        # ── Scene 1: Algebraic derivation ─────────────────────────────
        self.show_derivation()

        # ── Scene 2: Visual square comparison ─────────────────────────
        self.show_squares()

        # ── Scene 3: Numeric worked example ───────────────────────────
        self.show_numeric_example()

        # ── Scene 4: General rectangle (not just squares) ─────────────
        self.show_general_shape()

        # ── Outro ─────────────────────────────────────────────────────
        outro = Text("√(Area SF)  =  Linear Scale Factor", font_size=36, color=GREEN)
        self.play(Write(outro))
        self.wait(2.5)
        self.play(FadeOut(outro))

    # ──────────────────────────────────────────────────────────────────
    def show_derivation(self):
        """Step-by-step algebra from A_new/A_old → k."""
        header = Text("The Algebra", font_size=36, color=BLUE_B).to_edge(UP)
        self.play(FadeIn(header))

        steps = [
            MathTex(r"\text{Original side: } s", r"\quad\Rightarrow\quad",
                    r"\text{Original area: } A_{\text{old}} = s^2"),
            MathTex(r"\text{Scale by } k:", r"\quad\Rightarrow\quad",
                    r"\text{New area: } A_{\text{new}} = (ks)^2 = k^2 s^2"),
            MathTex(r"\frac{A_{\text{new}}}{A_{\text{old}}}",
                    r"= \frac{k^2 s^2}{s^2} = k^2"),
            MathTex(r"\sqrt{\frac{A_{\text{new}}}{A_{\text{old}}}}",
                    r"= \sqrt{k^2} = k"),
        ]

        colors = [WHITE, WHITE, WHITE, YELLOW]
        group  = VGroup(*steps).arrange(DOWN, aligned_edge=LEFT, buff=0.55).center()

        for step, col in zip(steps, colors):
            step.set_color(col)
            self.play(Write(step), run_time=1.3)
            self.wait(0.5)

        # Box the final result
        box = SurroundingRectangle(steps[-1], color=YELLOW, buff=0.2,
                                   corner_radius=0.1)
        self.play(Create(box))
        self.wait(2)
        self.play(FadeOut(VGroup(header, group, box)))

    # ──────────────────────────────────────────────────────────────────
    def show_squares(self):
        """Animate two squares side-by-side with area labels, then show the ratio."""
        header = Text("Visualising the Rule", font_size=36, color=BLUE_B).to_edge(UP)
        self.play(FadeIn(header))

        # ── Original square (side = 2 units → area = 4) ───────────────
        s_orig = 1.8          # screen size for side = 2
        sq_orig = Square(side_length=s_orig, color=BLUE,
                         fill_color=BLUE, fill_opacity=0.35,
                         stroke_width=2)
        sq_orig.shift(LEFT * 3.2)

        lbl_orig_side = MathTex(r"s = 2", font_size=26, color=WHITE)
        lbl_orig_side.next_to(sq_orig, DOWN, buff=0.25)
        lbl_orig_area = MathTex(r"A_{\text{old}} = 4", font_size=26, color=BLUE_B)
        lbl_orig_area.next_to(lbl_orig_side, DOWN, buff=0.15)

        # ── Scaled square (k = 3, side = 6 → area = 36) ───────────────
        k = 3
        s_new = s_orig * k / 2.2   # keep it on-screen (visual scale factor)
        sq_new = Square(side_length=s_new, color=RED,
                        fill_color=RED, fill_opacity=0.25,
                        stroke_width=2)
        sq_new.shift(RIGHT * 1.5)

        lbl_new_side = MathTex(rf"ks = {k}\times 2 = 6", font_size=26, color=WHITE)
        lbl_new_side.next_to(sq_new, DOWN, buff=0.25)
        lbl_new_area = MathTex(r"A_{\text{new}} = 36", font_size=26, color=RED_B)
        lbl_new_area.next_to(lbl_new_side, DOWN, buff=0.15)

        self.play(
            FadeIn(sq_orig), Write(lbl_orig_side), Write(lbl_orig_area),
            run_time=1.0
        )
        self.wait(0.4)
        self.play(
            FadeIn(sq_new), Write(lbl_new_side), Write(lbl_new_area),
            run_time=1.0
        )
        self.wait(0.8)

        # ── Show the ratio computation ─────────────────────────────────
        ratio = MathTex(
            r"\sqrt{\frac{A_{\text{new}}}{A_{\text{old}}}}",
            r"= \sqrt{\frac{36}{4}}",
            r"= \sqrt{9}",
            r"= 3 = k",
            font_size=34, color=YELLOW,
        )
        ratio.to_edge(DOWN, buff=0.7)

        for part in ratio:
            self.play(Write(part), run_time=0.9)
            self.wait(0.3)

        self.wait(1.5)
        self.play(FadeOut(VGroup(header, sq_orig, sq_new,
                                  lbl_orig_side, lbl_orig_area,
                                  lbl_new_side,  lbl_new_area,
                                  ratio)))

    # ──────────────────────────────────────────────────────────────────
    def show_numeric_example(self):
        """Walk through a worked numeric example with animated substitution."""
        header = Text("Worked Example", font_size=36, color=BLUE_B).to_edge(UP)
        self.play(FadeIn(header))

        problem = MathTex(
            r"\text{A rectangle has area } 12\ \text{cm}^2.",
            r"\quad\text{Its image has area } 108\ \text{cm}^2.",
            font_size=30, color=WHITE,
        ).arrange(DOWN, aligned_edge=LEFT).shift(UP * 1.8)

        self.play(Write(problem), run_time=1.5)
        self.wait(0.6)

        steps = VGroup(
            MathTex(r"\text{Step 1:}\quad \frac{A_{\text{new}}}{A_{\text{old}}} = \frac{108}{12} = 9",
                    font_size=32),
            MathTex(r"\text{Step 2:}\quad \sqrt{9} = 3",
                    font_size=32),
            MathTex(r"\therefore\quad k = 3", font_size=38, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.55).center().shift(DOWN * 0.3)

        for step in steps:
            self.play(Write(step), run_time=1.1)
            self.wait(0.7)

        box = SurroundingRectangle(steps[-1], color=YELLOW, buff=0.2,
                                   corner_radius=0.1)
        self.play(Create(box))
        self.wait(2)
        self.play(FadeOut(VGroup(header, problem, steps, box)))

    # ──────────────────────────────────────────────────────────────────
    def show_general_shape(self):
        """Show the rule works for ANY shape, not just squares."""
        header = Text("Works for ANY Shape", font_size=36, color=BLUE_B).to_edge(UP)
        self.play(FadeIn(header))

        note = Text(
            "The formula √(A_new / A_old) = k holds for any\n"
            "similar shape — triangles, circles, irregular polygons…",
            font_size=28, color=WHITE, line_spacing=1.4,
        ).center().shift(UP * 1.2)
        self.play(Write(note), run_time=1.8)
        self.wait(0.6)

        # Draw a small and large triangle
        tri_small = Triangle(color=GREEN, fill_color=GREEN, fill_opacity=0.35,
                             stroke_width=2).scale(0.7).shift(LEFT * 3 + DOWN * 0.8)
        tri_large = Triangle(color=ORANGE, fill_color=ORANGE, fill_opacity=0.25,
                             stroke_width=2).scale(0.7 * 2).shift(RIGHT * 1.2 + DOWN * 0.6)

        lbl_s = MathTex(r"A = a", font_size=26, color=GREEN_B)
        lbl_s.next_to(tri_small, DOWN, buff=0.2)
        lbl_l = MathTex(r"A = k^2 a", font_size=26, color=ORANGE_B)
        lbl_l.next_to(tri_large, DOWN, buff=0.2)

        self.play(FadeIn(tri_small), Write(lbl_s))
        self.wait(0.3)
        self.play(FadeIn(tri_large), Write(lbl_l))
        self.wait(0.5)

        formula = MathTex(
            r"\sqrt{\frac{k^2 a}{a}} = \sqrt{k^2} = k",
            font_size=36, color=YELLOW,
        ).to_edge(DOWN, buff=0.8)
        self.play(Write(formula))
        self.wait(2)

        self.play(FadeOut(VGroup(header, note, tri_small, tri_large,
                                  lbl_s, lbl_l, formula)))