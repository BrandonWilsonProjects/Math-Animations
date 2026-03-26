from manim import *
import numpy as np

# ── Palette (plain hex — avoids interpolate_color on raw strings) ───────────
C_BLUE        = "#4A90D9"
C_BLUE_LIGHT  = "#8FBDE8"   # ~blue blended 30% toward white
C_ORANGE      = "#E8A030"
C_ORANGE_LIGHT= "#F0C070"   # ~orange blended 20% toward white
C_ORANGE_PALE = "#F5D498"   # ~orange blended 50% toward white
C_GREEN       = "#5DBF82"
C_PINK        = "#D45A7A"
C_GRAY        = "#8A8A8A"
C_CREAM       = "#F5F0E8"
C_WHITE       = "#FFFFFF"


# ══════════════════════════════════════════════════════════════════════════
# Scene 1 — Coin Stack Intuition
# ══════════════════════════════════════════════════════════════════════════
class CoinStackIntuition(Scene):
    N_COINS = 12
    COIN_H  = 0.22
    COIN_W  = 1.8
    GAP     = 0.02

    def build_coin(self, cx, cy):
        body = Rectangle(
            width=self.COIN_W, height=self.COIN_H,
            fill_color=C_ORANGE, fill_opacity=0.95,
            stroke_color=C_ORANGE_LIGHT, stroke_width=1,
        ).move_to([cx, cy, 0])
        top = Ellipse(
            width=self.COIN_W, height=self.COIN_H * 0.55,
            fill_color=C_ORANGE_LIGHT, fill_opacity=0.95,
            stroke_color=C_ORANGE_PALE, stroke_width=1,
        ).move_to([cx, cy + self.COIN_H / 2, 0])
        return VGroup(body, top)

    def straight_positions(self):
        step   = self.COIN_H + self.GAP
        base_y = -(self.N_COINS * step) / 2
        return [(0.0, base_y + i * step) for i in range(self.N_COINS)]

    def shear_positions(self, shear=2.2):
        step   = self.COIN_H + self.GAP
        base_y = -(self.N_COINS * step) / 2
        return [
            (shear * i / (self.N_COINS - 1), base_y + i * step)
            for i in range(self.N_COINS)
        ]

    def construct(self):
        title = Text("Cavalieri's Principle", font_size=42, color=C_WHITE)
        sub   = Text(
            "Same cross-section at every height  \u2192  Same volume",
            font_size=21, color=C_GRAY,
        ).next_to(title, DOWN, buff=0.28)
        VGroup(title, sub).to_edge(UP, buff=0.35)
        self.play(FadeIn(title, shift=UP * 0.3), run_time=0.7)
        self.play(FadeIn(sub), run_time=0.5)
        self.wait(0.4)

        positions = self.straight_positions()
        coins = VGroup(*[self.build_coin(cx, cy) for cx, cy in positions])
        stack_lbl = Text("A stack of coins", font_size=23, color=C_CREAM)\
            .next_to(coins, RIGHT, buff=0.55)

        self.play(
            LaggedStart(*[FadeIn(c, shift=DOWN * 0.08) for c in coins], lag_ratio=0.06),
            run_time=1.5,
        )
        self.play(FadeIn(stack_lbl), run_time=0.4)
        self.wait(6)

        vol_lbl = VGroup(
            Text("Volume  \u221d  ", font_size=25, color=C_GRAY),
            Text(f"{self.N_COINS} coins", font_size=25, color=C_ORANGE),
        ).arrange(RIGHT, buff=0.08).next_to(coins, LEFT, buff=0.55)
        self.play(FadeIn(vol_lbl), run_time=0.4)
        self.wait(0.5)

        self.play(FadeOut(stack_lbl), run_time=0.25)
        shear_lbl = Text("Now slide each coin sideways\u2026", font_size=22, color=C_CREAM)\
            .next_to(coins, DOWN * 4, buff=0.45)
        self.play(FadeIn(shear_lbl), run_time=0.35)

        sheared = self.shear_positions()
        self.play(
            LaggedStart(
                *[coin.animate.move_to([sx, sy, 0])
                  for coin, (sx, sy) in zip(coins, sheared)],
                lag_ratio=0.04,
            ),
            run_time=1.8,
        )
        self.wait(0.35)

        still_lbl = VGroup(
            Text("Still  ", font_size=25, color=C_GRAY),
            Text(f"{self.N_COINS} coins", font_size=25, color=C_ORANGE),
            Text("  \u2014 same volume!", font_size=25, color=C_GREEN),
        ).arrange(RIGHT, buff=0.08).next_to(coins, LEFT, buff=0.15)
        self.play(FadeOut(vol_lbl), FadeOut(shear_lbl), FadeIn(still_lbl), run_time=0.55)
        self.wait(0.9)

        top_y   = sheared[-1][1] + self.COIN_H / 2 + 0.05
        bot_y   = sheared[0][1]  - self.COIN_H / 2 - 0.05
        arr_x   = 3.5
        h_arrow = DoubleArrow([arr_x, bot_y, 0], [arr_x, top_y, 0],
                              color=C_BLUE, stroke_width=2, buff=0)
        h_lbl   = Text("h", font_size=27, color=C_BLUE).next_to(h_arrow, RIGHT, buff=0.14)
        self.play(GrowArrow(h_arrow), FadeIn(h_lbl), run_time=0.65)

        mid_y      = (top_y + bot_y) / 2
        slice_line = DashedLine([-3.3, mid_y, 0], [arr_x - 0.12, mid_y, 0],
                                color=BLUE, stroke_width=2, dash_length=0.17)
        slice_txt  = Text("cross-section \u2192 same area at every height",
                          font_size=28, color=C_PINK)\
            .next_to(slice_line, DOWN * 30, buff=0.11).shift(LEFT * 0.4)
        self.play(Create(slice_line), run_time=0.65)
        self.play(FadeIn(slice_txt), run_time=0.4)
        self.wait(1.4)
        self.play(FadeOut(Group(*self.mobjects)), run_time=0.9)


# ══════════════════════════════════════════════════════════════════════════
# Scene 2 — Cross-Section Sweep
# ══════════════════════════════════════════════════════════════════════════
class CrossSectionScene(Scene):
    HEIGHT = 3.8
    R      = 1.0

    def construct(self):
        title = Text("Equal cross-sections at every height", font_size=33, color=C_WHITE)
        title.to_edge(UP, buff=0.32)
        self.play(FadeIn(title, shift=UP * 0.2), run_time=0.65)

        cyl_x   = -2.9
        cyl_top =  self.HEIGHT / 2
        cyl_bot = -self.HEIGHT / 2

        cyl_body = Rectangle(
            width=self.R * 2, height=self.HEIGHT,
            fill_color=C_BLUE, fill_opacity=0.22,
            stroke_color=C_BLUE, stroke_width=2,
        ).move_to([cyl_x, 0, 0])
        cyl_top_el = Ellipse(
            width=self.R * 2, height=self.R * 0.48,
            fill_color=C_BLUE_LIGHT, fill_opacity=0.45,
            stroke_color=C_BLUE, stroke_width=2,
        ).move_to([cyl_x, cyl_top, 0])
        cyl_bot_el = Ellipse(
            width=self.R * 2, height=self.R * 0.48,
            fill_color=C_BLUE, fill_opacity=0.12,
            stroke_color=C_BLUE, stroke_width=1.5,
        ).move_to([cyl_x, cyl_bot, 0])
        cyl_lbl = Text("Cylinder", font_size=21, color=C_BLUE)\
            .next_to(cyl_body, DOWN, buff=0.22)

        blob_x = 2.9
        blob = Polygon(
            [blob_x - 0.85, cyl_top,       0],
            [blob_x + 1.05, cyl_top * 0.9, 0],
            [blob_x + 1.18, 0.35,           0],
            [blob_x + 0.78, -0.45,          0],
            [blob_x + 1.25, cyl_bot * 0.8, 0],
            [blob_x + 0.55, cyl_bot,        0],
            [blob_x - 0.95, cyl_bot * 0.9, 0],
            [blob_x - 1.15, -0.18,          0],
            [blob_x - 0.65, 0.58,           0],
            [blob_x - 1.05, cyl_top * 0.8, 0],
            fill_color=C_ORANGE, fill_opacity=0.20,
            stroke_color=C_ORANGE, stroke_width=2,
        )
        blob_lbl = Text("Another solid", font_size=20, color=C_ORANGE)\
            .next_to(blob, DOWN, buff=0.18)

        self.play(
            LaggedStart(
                AnimationGroup(Create(cyl_body), Create(cyl_top_el), Create(cyl_bot_el)),
                Create(blob),
                lag_ratio=0.3,
            ),
            run_time=1.3,
        )
        self.play(FadeIn(cyl_lbl), FadeIn(blob_lbl), run_time=0.4)
        self.wait(0.45)

        sweep_y = ValueTracker(cyl_top - 0.02)
        line_xl = cyl_x - self.R - 0.08
        line_xr = blob_x + 1.38

        sweep_line = always_redraw(lambda: DashedLine(
            [line_xl, sweep_y.get_value(), 0],
            [line_xr, sweep_y.get_value(), 0],
            color=C_PINK, stroke_width=2.5, dash_length=0.19,
        ))

        def cyl_slice():
            return Rectangle(
                width=self.R * 2, height=0.17,
                fill_color=C_BLUE, fill_opacity=0.75, stroke_width=0,
            ).move_to([cyl_x, sweep_y.get_value(), 0])

        def blob_width_at(y):
            t = (y - cyl_bot) / self.HEIGHT
            return 1.05 + 0.62 * np.sin(np.pi * t) + 0.14 * np.sin(2.6 * np.pi * t)

        def blob_slice():
            return Rectangle(
                width=blob_width_at(sweep_y.get_value()) * 2,
                height=0.17,
                fill_color=C_ORANGE, fill_opacity=0.75, stroke_width=0,
            ).move_to([blob_x, sweep_y.get_value(), 0])

        cyl_sl  = always_redraw(cyl_slice)
        blob_sl = always_redraw(blob_slice)
        eq_sign = always_redraw(
            lambda: MathTex("=", font_size=30, color=C_GREEN)
                .move_to([0, sweep_y.get_value(), 0])
        )

        self.play(Create(sweep_line), FadeIn(cyl_sl), FadeIn(blob_sl), FadeIn(eq_sign),
                  run_time=0.5)

        area_cyl  = MathTex(r"A(y) = \pi r^2", font_size=22, color=C_BLUE)\
            .move_to([cyl_x, cyl_bot - 0.85, 0])
        area_blob = MathTex(r"A(y)", font_size=22, color=C_ORANGE)\
            .move_to([blob_x, cyl_bot - 0.85, 0])
        area_eq   = Text("equal at every y", font_size=40, color=RED)\
            .move_to([0, cyl_bot - 1.2, 0])
        self.play(FadeIn(area_cyl), FadeIn(area_blob), FadeIn(area_eq), run_time=0.4)

        self.play(
            sweep_y.animate.set_value(cyl_bot + 0.02),
            run_time=3.4, rate_func=linear,
        )
        self.wait(0.45)

# ══════════════════════════════════════════════════════════════════════════
# Scene 3 — Archimedes Hat-Box
# ══════════════════════════════════════════════════════════════════════════
class CylinderVsConeScene(Scene):
    R = 1.1
    H = 2.2

    def construct(self):
        title = Text("Classic example \u2014 Archimedes' Hat-Box theorem",
                     font_size=27, color=C_WHITE)
        title.to_edge(UP, buff=0.32)
        self.play(FadeIn(title), run_time=0.65)

        cyl_x  = -4.0
        sph_x  =  0.15
        cone_x =  3.8

        cyl = VGroup(
            Rectangle(width=self.R * 2, height=self.H,
                      fill_color=C_BLUE, fill_opacity=0.20,
                      stroke_color=C_BLUE, stroke_width=2)
                .move_to([cyl_x, 0, 0]),
            Ellipse(width=self.R * 2, height=self.R * 0.46,
                    fill_color=C_BLUE_LIGHT, fill_opacity=0.42,
                    stroke_color=C_BLUE, stroke_width=2)
                .move_to([cyl_x, self.H / 2, 0]),
            Ellipse(width=self.R * 2, height=self.R * 0.46,
                    fill_color=C_BLUE, fill_opacity=0.11,
                    stroke_color=C_BLUE, stroke_width=1.5)
                .move_to([cyl_x, -self.H / 2, 0]),
        )
        cyl_lbl = Text("Cylinder", font_size=19, color=C_BLUE)\
            .next_to(cyl, DOWN, buff=0.25)

        sphere = Circle(radius=self.R,
                        fill_color=C_GREEN, fill_opacity=0.18,
                        stroke_color=C_GREEN, stroke_width=2)\
            .move_to([sph_x, 0, 0])
        sph_eq = Ellipse(width=self.R * 2, height=self.R * 0.36,
                         fill_opacity=0, stroke_color=C_GREEN,
                         stroke_width=1.5, stroke_opacity=0.45)\
            .move_to([sph_x, 0, 0])
        sph_lbl = Text("Sphere", font_size=19, color=C_GREEN)\
            .next_to(sphere, DOWN, buff=0.25)

        cone = VGroup(
            Polygon(
                [cone_x,          self.H / 2,  0],
                [cone_x - self.R, -self.H / 2, 0],
                [cone_x + self.R, -self.H / 2, 0],
                fill_color=C_PINK, fill_opacity=0.20,
                stroke_color=C_PINK, stroke_width=2,
            ),
            Ellipse(width=self.R * 2, height=self.R * 0.46,
                    fill_color=C_PINK, fill_opacity=0.11,
                    stroke_color=C_PINK, stroke_width=1.5)
                .move_to([cone_x, -self.H / 2, 0]),
        )
        cone_lbl = Text("Cone", font_size=19, color=C_PINK)\
            .next_to(cone, DOWN, buff=0.25)

        plus = Text("+", font_size=34, color=C_GRAY).move_to([sph_x - 1.8, 0, 0])
        eq_s = Text("=", font_size=34, color=C_GRAY).move_to([cyl_x + 2.2, 0, 0])

        self.play(
            LaggedStart(Create(cyl), Create(sphere), Create(sph_eq), Create(cone),
                        lag_ratio=0.22),
            run_time=1.5,
        )
        self.play(FadeIn(cyl_lbl), FadeIn(sph_lbl), FadeIn(cone_lbl),
                  FadeIn(plus), FadeIn(eq_s), run_time=0.45)
        self.wait(0.45)

        sub = Text("At height y from the centre:", font_size=21, color=C_GRAY)\
            .move_to([0, -1.95, 0])
        self.play(FadeIn(sub), run_time=0.38)

        e1 = MathTex(r"A_{\mathrm{cyl}} = \pi r^2",
                     font_size=28, color=C_BLUE).move_to([cyl_x, -2.45, 0])
        e2 = MathTex(r"A_{\mathrm{sph}} = \pi(r^2 - y^2)",
                     font_size=28, color=C_GREEN).move_to([sph_x + 0.2, -2.45, 0])
        e3 = MathTex(r"A_{\mathrm{cone}} = \pi y^2",
                     font_size=28, color=C_PINK).move_to([cone_x, -2.45, 0])
        self.play(Write(e1), Write(e2), Write(e3), run_time=1.15)
        self.wait(0.38)

        check = MathTex(
            r"\pi(r^2-y^2)+\pi y^2 = \pi r^2 \checkmark",
            font_size=29, color=C_GREEN,
        ).move_to([0, -3.12, 0])
        self.play(Write(check), run_time=0.95)
        self.wait(7)


# ══════════════════════════════════════════════════════════════════════════
# Scene 4 — Formal Statement
# ══════════════════════════════════════════════════════════════════════════
class FormalStatement(Scene):
    def show_parameter_effect(self):

        # ── 1. Title ──────────────────────────────────────────────────────────
        header = Text("How r and h affect Volume", font_size=34, color=RED_B)\
            .to_edge(UP)
        self.play(FadeIn(header))
        self.wait(0.5)

        # ── 2. Axes ───────────────────────────────────────────────────────────
        ax = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 80, 10],
            x_length=7,
            y_length=4.2,
            axis_config={"color": GREY_B, "include_numbers": True},
        ).center().shift(DOWN * 0.6)

        x_lbl = ax.get_x_axis_label(MathTex(r"r\ \text{or}\ h"), direction=RIGHT)
        y_lbl = ax.get_y_axis_label(MathTex("V"), direction=UP)
        self.play(Create(ax), Write(x_lbl), Write(y_lbl))
        self.wait(0.4)

        # ── 3. Quadratic curve (V vs r, h fixed = 2) ─────────────────────────
        h_fixed = 2
        curve_r = ax.plot(
            lambda r: (1/3) * PI * r**2 * h_fixed,
            color=GREEN, x_range=[0, 3.8],
        )
        lbl_r = MathTex(
            r"V = \tfrac{1}{3}\pi r^2 \cdot 2\quad(h=2)",
            font_size=22, color=GREEN,
        ).next_to(ax.i2gp(3.8, curve_r), RIGHT, buff=0.3)

        self.play(Create(curve_r), run_time=1.2)
        self.play(Write(lbl_r))
        self.wait(0.5)

        # ── 4. Linear curve (V vs h, r fixed = 2) ────────────────────────────
        r_fixed = 2
        curve_h = ax.plot(
            lambda h: (1/3) * PI * r_fixed**2 * h,
            color=ORANGE, x_range=[0, 4.8],
        )
        lbl_h = MathTex(
            r"V = \tfrac{1}{3}\pi \cdot 4 \cdot h\quad(r=2)",
            font_size=22, color=ORANGE,
        ).next_to(ax.i2gp(4.8, curve_h), RIGHT, buff=0.3).shift(UP * 0.35)

        self.play(Create(curve_h), run_time=1.2)
        self.play(Write(lbl_h))
        self.wait(0.5)

        # ── 5. Doubling-r highlight ───────────────────────────────────────────
        dot1 = Dot(ax.c2p(1, (1/3) * PI * 1**2 * 2), color=YELLOW, radius=0.1)
        dot2 = Dot(ax.c2p(2, (1/3) * PI * 2**2 * 2), color=YELLOW, radius=0.1)
        arrow = Arrow(
            dot1.get_center(), dot2.get_center(),
            buff=0.1, color=YELLOW, stroke_width=2,
        )
        double_lbl = MathTex(
            r"r \times 2 \Rightarrow V \times 4",
            font_size=24, color=YELLOW,
        ).next_to(arrow, RIGHT, buff=0.15)

        self.play(FadeIn(dot1))
        self.play(FadeIn(dot2))
        self.play(Create(arrow))
        self.play(Write(double_lbl))
        self.wait(0.5)

        # ── Fade everything out before showing intuition ──────────────────────
        self.play(FadeOut(Group(
            header, ax, x_lbl, y_lbl,
            curve_r, lbl_r, curve_h, lbl_h,
            dot1, dot2, arrow, double_lbl,
        )))

        # ── 6. Intuition — centred, held for 10 s ────────────────────────────
        note = VGroup(
            MathTex(
                r"V \propto r^2 \quad \text{(doubling}\ r\ \text{quadruples}\ V\text{)}",
                font_size=32, color=WHITE,
            ),
            MathTex(
                r"V \propto h \quad \text{(doubling}\ h\ \text{doubles}\ V\text{)}",
                font_size=32, color=WHITE,
            ),
        ).arrange(DOWN, buff=0.5).center()

        self.play(Write(note), run_time=1.4)
        self.wait(10)

        self.play(FadeOut(note))