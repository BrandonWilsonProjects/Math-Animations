"""
Euler's Number & Day Trading — Manim Script (NO LaTeX version)
==============================================================
Zero LaTeX required. Uses only Text() with Unicode math symbols.

Render commands:
    manim -pql eulers_number.py EulersNumber
    manim -pql eulers_number.py DayTradingExample
    manim -pqh eulers_number.py FullPresentation
"""

from manim import *
import numpy as np

E_COLOR = "#1d9e75"
RED_C   = "#e24b4a"
BLUE_C  = "#378add"
AMBER   = "#EF9F27"
LGREY   = "#aaaaaa"


def bullet_list(*items, font_size=28, color=WHITE, spacing=0.42):
    rows = []
    for item in items:
        dot  = Text("•", font_size=font_size, color=AMBER)
        txt  = Text(item, font_size=font_size, color=color)
        txt.next_to(dot, RIGHT, buff=0.2)
        rows.append(VGroup(dot, txt))
    return VGroup(*rows).arrange(DOWN, aligned_edge=LEFT, buff=spacing)


def math_text(s, font_size=40, color=WHITE):
    return Text(s, font_size=font_size, color=color)


# ══════════════════════════════════════════════════════════════════════════════
#  SCENE 1 — Euler's Number
# ══════════════════════════════════════════════════════════════════════════════
class EulersNumber(Scene):
    def construct(self):

        # ── Title ─────────────────────────────────────────────────────────
        title  = Text("Euler's Number", font_size=56, color=E_COLOR)
        approx = Text("e  \u2248  2.71828 18284 59045\u2026", font_size=28, color=LGREY)
        approx.next_to(title, DOWN, buff=0.3)
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(approx, shift=UP * 0.3))
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(approx))

        # ── 1. Compound-interest limit ────────────────────────────────────
        sec1 = Text("1 \u2014 The Compound-Interest Limit", font_size=34, color=AMBER)
        sec1.to_edge(UP)
        self.play(Write(sec1))

        formula = math_text("e  =  lim (1 + 1/n)^n   as n \u2192 \u221e", font_size=44)
        self.play(Write(formula))
        self.wait(0.6)

        header = Text("n                  (1 + 1/n)^n", font_size=24, color=LGREY)
        header.next_to(formula, DOWN, buff=0.45)
        self.play(FadeIn(header))

        data = [
            ("1",          1.00000),
            ("2",          2.25000),
            ("5",          2.48832),
            ("10",         2.59374),
            ("100",        2.70481),
            ("1,000",      2.71692),
            ("1,000,000",  2.71828),
        ]
        rows, prev = [], header
        for lbl, val in data:
            row = Text(f"{lbl:<18}  {val:.5f}", font_size=24)
            row.next_to(prev, DOWN, buff=0.17)
            self.play(FadeIn(row, shift=RIGHT * 0.15), run_time=0.35)
            rows.append(row)
            prev = row

        arrow = Text("\u2192  e \u2248 2.71828", font_size=28, color=E_COLOR)
        arrow.next_to(prev, DOWN, buff=0.28)
        self.play(Write(arrow))
        self.wait(6)
        self.play(*[FadeOut(m) for m in [sec1, formula, header, arrow] + rows])

        # ── 2. Power series ───────────────────────────────────────────────
        sec2 = Text("2 \u2014 Infinite Series Definition", font_size=34, color=AMBER)
        sec2.to_edge(UP)
        self.play(Write(sec2))

        line1 = math_text("e^x  =  sum( x^n / n! )   for n = 0 to \u221e", font_size=36)
        line2 = math_text("     =  1 + x + x^2/2! + x^3/3! + x^4/4! + \u2026", font_size=34, color=LGREY)
        line2.next_to(line1, DOWN, buff=0.3)
        self.play(Write(line1))
        self.play(FadeIn(line2))
        self.wait(0.8)

        note = Text("Partial sums at  x = 1 :", font_size=26, color=LGREY)
        note.next_to(line2, DOWN, buff=0.45)
        self.play(FadeIn(note))

        partial_data = [
            ("S0  =  1",              "1.000000"),
            ("S1  =  1 + 1",          "2.000000"),
            ("S2  =  ... + 1/2",      "2.500000"),
            ("S3  =  ... + 1/6",      "2.666667"),
            ("S4  =  ... + 1/24",     "2.708333"),
            ("S5  =  ... + 1/120",    "2.716667"),
            ("S10 =  ...",             "2.718282  \u2192  e"),
        ]
        prows, prev = [], note
        for lhs, rhs in partial_data:
            color = E_COLOR if "\u2192" in rhs else WHITE
            row = Text(f"{lhs:<24}  {rhs}", font_size=23, color=color)
            row.next_to(prev, DOWN, buff=0.17)
            self.play(FadeIn(row, shift=RIGHT * 0.15), run_time=0.33)
            prows.append(row)
            prev = row

        self.wait(6)
        self.play(*[FadeOut(m) for m in [sec2, line1, line2, note] + prows])

        # ── 3. Self-derivative graph ──────────────────────────────────────
        sec3 = Text("3 \u2014 The Self-Derivative Curve", font_size=34, color=AMBER)
        sec3.to_edge(UP)
        self.play(Write(sec3))
        self.wait(2)
        self.play(FadeOut(sec3))

        prop = math_text("d/dx ( e^x )  =  e^x", font_size=46, color=E_COLOR)
        prop.next_to(sec3, DOWN, buff=0.4)
        self.play(Write(prop))
        self.wait(0.6)

        axes = Axes(
            x_range=[-1, 3.2, 1],
            y_range=[0, 12, 2],
            x_length=7, y_length=4,
            axis_config={"color": GREY_B},
            tips=False,
        ).next_to(prop, DOWN, buff=0.3)

        curve  = axes.plot(lambda x: np.e ** x, color=E_COLOR, stroke_width=3)
        c_lbl  = Text("e^x", font_size=24, color=E_COLOR)
        c_lbl.next_to(axes.c2p(2.8, np.e ** 2.8), UR, buff=0.1)

        self.play(Create(axes), Create(curve), FadeIn(c_lbl))

        x0, y0 = 1.0, np.e
        tangent = axes.plot(lambda x: y0 + y0 * (x - x0),
                            x_range=[x0 - 0.7, x0 + 0.7],
                            color=AMBER, stroke_width=2.5)
        dot   = Dot(axes.c2p(x0, y0), color=AMBER)
        t_lbl = Text("slope = e  (equals the function!)", font_size=20, color=AMBER)
        t_lbl.next_to(dot, UR, buff=0.7)

        self.play(Create(tangent), FadeIn(dot), Write(t_lbl))
        self.wait(2.5)
        self.play(*[FadeOut(m) for m in
                    [sec3, prop, axes, curve, c_lbl, tangent, dot, t_lbl]])

        # ── 4. Key properties ─────────────────────────────────────────────
        sec4 = Text("4 \u2014 Key Properties of e", font_size=34, color=AMBER)
        sec4.to_edge(UP)
        self.play(Write(sec4))

        props = bullet_list(
            "e \u2248 2.71828  \u2014  irrational & transcendental",
            "d/dx e^x = e^x  \u2014  its own derivative",
            "Integral of e^x dx = e^x + C",
            "e^(i*pi) + 1 = 0  \u2014  Euler's Identity",
            "Natural log:  ln(e) = 1",
            font_size=28,
        )
        props.next_to(sec4, DOWN, buff=0.5)
        self.play(FadeIn(props, shift=UP * 0.3))
        self.wait(3)
        self.play(FadeOut(sec4), FadeOut(props))

        end = Text("e  =  2.71828\u2026", font_size=64, color=E_COLOR)
        self.play(Write(end))
        self.wait(2)
        self.play(FadeOut(end))


# ══════════════════════════════════════════════════════════════════════════════
#  SCENE 2 — Day Trading
# ══════════════════════════════════════════════════════════════════════════════
class DayTradingExample(Scene):
    def construct(self):

        # ── Title ─────────────────────────────────────────────────────────
        title    = Text("e in Day Trading", font_size=50, color=AMBER)
        subtitle = Text("EMA  \u2022  Continuous Compounding  \u2022  Log Returns",
                        font_size=26, color=LGREY)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(Write(title), FadeIn(subtitle, shift=UP * 0.3))
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(subtitle))

        # ── A. EMA ────────────────────────────────────────────────────────
        secA = Text("A \u2014 Exponential Moving Average (EMA)", font_size=30, color=AMBER)
        secA.to_edge(UP)
        self.play(Write(secA))

        ema_f = math_text("EMA(t) = a * P(t)  +  (1 - a) * EMA(t-1)", font_size=36)
        ema_f.next_to(secA, DOWN, buff=0.45)
        self.play(Write(ema_f))

        alpha_d = math_text("a = 2 / (N + 1),   N = period  (e.g. 9 candles)",
                            font_size=28, color=LGREY)
        alpha_d.next_to(ema_f, DOWN, buff=0.35)
        self.play(FadeIn(alpha_d))
        self.wait(0.8)

        ema_note = Text(
            "The (1 - a) decay factor is e in disguise:\n"
            "as N \u2192 inf,   (1 - a)^N  \u2192  e^(-2)  \u2248  0.135",
            font_size=24, color=E_COLOR, line_spacing=1.4,
        )
        ema_note.next_to(alpha_d, DOWN, buff=0.4)
        self.play(FadeIn(ema_note, shift=UP * 0.2))
        self.wait(1.2)

        # Simulated price + EMA chart
        np.random.seed(42)
        n      = 30
        prices = np.cumsum(np.random.randn(n) * 1.2) + 100
        a      = 2 / (9 + 1)
        ema    = [prices[0]]
        for p in prices[1:]:
            ema.append(a * p + (1 - a) * ema[-1])

        axes = Axes(
            x_range=[0, n - 1, 5],
            y_range=[min(prices) - 3, max(prices) + 3, 5],
            x_length=8, y_length=3,
            axis_config={"color": GREY_B, "include_numbers": False},
            tips=False,
        ).next_to(ema_note, DOWN, buff=0.35)

        price_segs = VGroup(*[
            Line(axes.c2p(i, prices[i]), axes.c2p(i + 1, prices[i + 1]),
                 color=BLUE_C, stroke_width=1.8)
            for i in range(n - 1)
        ])
        ema_segs = VGroup(*[
            Line(axes.c2p(i, ema[i]), axes.c2p(i + 1, ema[i + 1]),
                 color=E_COLOR, stroke_width=2.8)
            for i in range(n - 1)
        ])
        p_lbl = Text("Price",   font_size=18, color=BLUE_C).next_to(axes, RIGHT).shift(UP * 0.4)
        e_lbl = Text("EMA(9)", font_size=18, color=E_COLOR).next_to(axes, RIGHT).shift(DOWN * 0.2)

        self.play(Create(axes))
        self.play(Create(price_segs), run_time=1)
        self.play(Create(ema_segs),   run_time=1)
        self.play(FadeIn(p_lbl), FadeIn(e_lbl))
        self.wait(15)
        self.play(*[FadeOut(m) for m in
                    [secA, ema_f, alpha_d, ema_note,
                     axes, price_segs, ema_segs, p_lbl, e_lbl]])

        # ── B. Continuous Compounding ──────────────────────────────────────
        secB = Text("B \u2014 Continuous Compounding of P&L", font_size=30, color=AMBER)
        secB.to_edge(UP)
        self.play(Write(secB))

        cc = math_text("A  =  P * e^(r * t)", font_size=58)
        cc.next_to(secB, DOWN, buff=0.5)
        self.play(Write(cc))

        legend = VGroup(
            Text("P  =  starting capital",             font_size=28, color=LGREY),
            Text("r  =  continuous daily return rate", font_size=28, color=LGREY),
            Text("t  =  number of trading days",       font_size=28, color=LGREY),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        legend.next_to(cc, DOWN, buff=0.4)
        self.play(FadeIn(legend))
        self.wait(0.8)

        ex_title = Text("Worked Example", font_size=26, color=E_COLOR)
        ex_title.next_to(legend, DOWN, buff=0.4)
        self.play(FadeIn(ex_title))

        steps = VGroup(
            Text("P = $10,000   r = 0.5%/day   t = 252 days", font_size=26),
            math_text("A = 10,000 * e^(0.005 x 252)", font_size=28),
            math_text("A = 10,000 * e^(1.26)", font_size=28),
            Text("A  \u2248  $35,254   (252% return in one trading year)",
                 font_size=27, color=E_COLOR),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        steps.next_to(ex_title, DOWN, buff=0.3)

        for line in steps:
            self.play(FadeIn(line, shift=RIGHT * 0.2), run_time=0.55)
        self.wait(7)
        self.play(*[FadeOut(m) for m in [secB, cc, legend, ex_title, steps]])

        # ── C. Log Returns ─────────────────────────────────────────────────
        secC = Text("C \u2014 Log Returns (The Trader's e)", font_size=30, color=AMBER)
        secC.to_edge(UP)
        self.play(Write(secC))

        log_r = math_text("r_log  =  ln( P(t) / P(t-1) )", font_size=42)
        log_r.next_to(secC, DOWN, buff=0.5)
        self.play(Write(log_r))

        blist = bullet_list(
            "Additive over time  \u2014  sum daily log returns for any period",
            "Symmetric  \u2014  a +10% and -10% move cancel exactly",
            "Converts exponential growth into linear arithmetic",
            "Core input: Sharpe ratio, volatility & Black-Scholes",
            font_size=27,
        )
        blist.next_to(log_r, DOWN, buff=0.45)
        self.play(FadeIn(blist, shift=UP * 0.2))
        self.wait(7)
        self.play(FadeOut(secC), FadeOut(log_r), FadeOut(blist))

        # End card
        end1 = Text("e powers every exponential edge in trading.",
                    font_size=30, color=E_COLOR)
        end2 = Text("e  =  2.71828\u2026", font_size=48, color=AMBER)
        end2.next_to(end1, DOWN, buff=0.5)
        self.play(Write(end1), Write(end2))
        self.wait(2.5)
        self.play(FadeOut(end1), FadeOut(end2))


# ══════════════════════════════════════════════════════════════════════════════
#  FULL PRESENTATION
# ══════════════════════════════════════════════════════════════════════════════
class FullPresentation(Scene):
    def construct(self):
        EulersNumber.construct(self)
        DayTradingExample.construct(self)