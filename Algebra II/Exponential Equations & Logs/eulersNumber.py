from manim import *
import numpy as np

E_COLOR = "#1d9e75"
RED_C   = "#e24b4a"
BLUE_C  = "#378add"
AMBER   = "#EF9F27"
LGREY   = "#aaaaaa"


def bullet_list(*items, font_size=28, color=WHITE, spacing=0.45):
    rows = []
    for item in items:
        dot  = Text("•", font_size=font_size, color=AMBER)
        text = Text(item, font_size=font_size, color=color)
        text.next_to(dot, RIGHT, buff=0.2)
        rows.append(VGroup(dot, text))
    return VGroup(*rows).arrange(DOWN, aligned_edge=LEFT, buff=spacing)


# ══════════════════════════════════════════════════════════════════════════════
#  SCENE 1 — Euler's Number mechanics
# ══════════════════════════════════════════════════════════════════════════════
class EulersNumber(Scene):
    def construct(self):

        # Title
        title  = Text("Euler's Number", font_size=56, color=E_COLOR)
        approx = Text("e  ≈  2.71828 18284 59045…", font_size=30, color=LGREY)
        approx.next_to(title, DOWN, buff=0.3)
        self.play(Write(title), run_time=1.2)
        self.play(FadeIn(approx, shift=UP * 0.3))
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(approx))

        # ── 1. Compound-interest limit ──────────────────────────────────────
        sec1 = Text("1 — The Compound-Interest Limit", font_size=34, color=AMBER)
        sec1.to_edge(UP)
        self.play(Write(sec1))

        formula = Text(
            r"e \;=\; \lim_{n \to \infty}\!\left(1 + \frac{1}{n}\right)^{\!n}",
            font_size=54,
        )
        self.play(Write(formula))
        self.wait(0.6)

        header = Text("n               (1 + 1/n)^n", font_size=24, color=LGREY)
        header.next_to(formula, DOWN, buff=0.45)
        self.play(FadeIn(header))

        data = [
            ("1",         1.00000),
            ("2",         2.25000),
            ("5",         2.48832),
            ("10",        2.59374),
            ("100",       2.70481),
            ("1,000",     2.71692),
            ("1,000,000", 2.71828),
        ]
        rows, prev = [], header
        for lbl, val in data:
            row = Text(f"{lbl:<16}  {val:.5f}", font_size=24)
            row.next_to(prev, DOWN, buff=0.18)
            self.play(FadeIn(row, shift=RIGHT * 0.15), run_time=0.38)
            rows.append(row)
            prev = row

        arrow = Text("→  e ≈ 2.71828", font_size=28, color=E_COLOR)
        arrow.next_to(prev, DOWN, buff=0.28)
        self.play(Write(arrow))
        self.wait(2)
        self.play(*[FadeOut(m) for m in [sec1, formula, header, arrow] + rows])

        # ── 2. Power series ─────────────────────────────────────────────────
        sec2 = Text("2 — Infinite Series Definition", font_size=34, color=AMBER)
        sec2.to_edge(UP)
        self.play(Write(sec2))

        series = Text(
            r"e^x = \sum_{n=0}^{\infty}\frac{x^n}{n!}"
            r"= 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots",
            font_size=40,
        )
        self.play(Write(series))
        self.wait(0.8)

        note = Text("Partial sums at  x = 1:", font_size=26, color=LGREY)
        note.next_to(series, DOWN, buff=0.45)
        self.play(FadeIn(note))

        partial_data = [
            ("S0 = 1",              "1.000000"),
            ("S1 = 1 + 1",         "2.000000"),
            ("S2 = ... + 1/2",     "2.500000"),
            ("S3 = ... + 1/6",     "2.666667"),
            ("S4 = ... + 1/24",    "2.708333"),
            ("S5 = ... + 1/120",   "2.716667"),
            ("S10 = ...",           "2.718282  ->  e"),
        ]
        prows, prev = [], note
        for lhs, rhs in partial_data:
            color = E_COLOR if "->" in rhs else WHITE
            row = Text(f"{lhs:<22}  {rhs}", font_size=24, color=color)
            row.next_to(prev, DOWN, buff=0.18)
            self.play(FadeIn(row, shift=RIGHT * 0.15), run_time=0.35)
            prows.append(row)
            prev = row

        self.wait(2)
        self.play(*[FadeOut(m) for m in [sec2, series, note] + prows])

        # ── 3. Self-derivative graph ─────────────────────────────────────────
        sec3 = Text("3 — The Self-Derivative Curve", font_size=34, color=AMBER)
        sec3.to_edge(UP)
        self.play(Write(sec3))

        prop = Text(r"\frac{d}{dx}\,e^x \;=\; e^x", font_size=48, color=E_COLOR)
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

        curve = axes.plot(lambda x: np.e ** x, color=E_COLOR, stroke_width=3)
        c_lbl = axes.get_graph_label(curve, label=Text("e^x"),
                                     x_val=2.6, direction=UP, color=E_COLOR)
        self.play(Create(axes), Create(curve), Write(c_lbl))

        x0, y0 = 1.0, np.e
        tangent = axes.plot(lambda x: y0 + y0 * (x - x0),
                            x_range=[x0 - 0.7, x0 + 0.7],
                            color=AMBER, stroke_width=2.5)
        dot   = Dot(axes.c2p(x0, y0), color=AMBER)
        t_lbl = Text("slope = e", font_size=22, color=AMBER)
        t_lbl.next_to(dot, UR, buff=0.15)

        self.play(Create(tangent), FadeIn(dot), Write(t_lbl))
        self.wait(2.5)
        self.play(*[FadeOut(m) for m in
                    [sec3, prop, axes, curve, c_lbl, tangent, dot, t_lbl]])

        # ── 4. Key properties ────────────────────────────────────────────────
        sec4 = Text("4 — Key Properties of e", font_size=34, color=AMBER)
        sec4.to_edge(UP)
        self.play(Write(sec4))

        props = bullet_list(
            "e ~ 2.71828  —  irrational & transcendental",
            "d/dx of e^x = e^x  —  its own derivative",
            "Integral of e^x dx = e^x + C",
            "e^(i*pi) + 1 = 0  —  Euler's Identity",
            "Natural log:  ln(e) = 1",
            font_size=28,
        )
        props.next_to(sec4, DOWN, buff=0.5)
        self.play(FadeIn(props, shift=UP * 0.3))
        self.wait(3)
        self.play(FadeOut(sec4), FadeOut(props))

        end = Text("e  =  2.71828…", font_size=64, color=E_COLOR)
        self.play(Write(end))
        self.wait(2)
        self.play(FadeOut(end))


# ══════════════════════════════════════════════════════════════════════════════
#  SCENE 2 — Day Trading applications
# ══════════════════════════════════════════════════════════════════════════════
class DayTradingExample(Scene):
    def construct(self):

        # Title
        title    = Text("e in Day Trading", font_size=50, color=AMBER)
        subtitle = Text("EMA  •  Continuous Compounding  •  Log Returns",
                        font_size=26, color=LGREY)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(Write(title), FadeIn(subtitle, shift=UP * 0.3))
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(subtitle))

        # ── A. EMA ──────────────────────────────────────────────────────────
        secA = Text("A — Exponential Moving Average (EMA)", font_size=30, color=AMBER)
        secA.to_edge(UP)
        self.play(Write(secA))

        ema_f = Text(
            r"\text{EMA}_t = \alpha \cdot P_t + (1-\alpha)\cdot\text{EMA}_{t-1}",
            font_size=40,
        )
        ema_f.next_to(secA, DOWN, buff=0.45)
        self.play(Write(ema_f))

        alpha_d = Text(
            r"\alpha = \frac{2}{N+1}, \quad N = \text{period (e.g. 9 candles)}",
            font_size=32, color=LGREY,
        )
        alpha_d.next_to(ema_f, DOWN, buff=0.35)
        self.play(FadeIn(alpha_d))
        self.wait(0.8)

        ema_note = Text(
            "The (1-a) decay factor is e in disguise:\n"
            "as N->inf,  (1-a)^N  ->  e^(-2)  ~  0.135",
            font_size=24, color=E_COLOR, line_spacing=1.4,
        )
        ema_note.next_to(alpha_d, DOWN, buff=0.4)
        self.play(FadeIn(ema_note, shift=UP * 0.2))
        self.wait(1.2)

        # Simulated chart
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
        p_lbl = Text("Price",    font_size=18, color=BLUE_C).next_to(axes, RIGHT).shift(UP * 0.4)
        e_lbl = Text("EMA(9)", font_size=18, color=E_COLOR).next_to(axes, RIGHT).shift(DOWN * 0.2)

        self.play(Create(axes))
        self.play(Create(price_segs), run_time=1)
        self.play(Create(ema_segs),   run_time=1)
        self.play(FadeIn(p_lbl), FadeIn(e_lbl))
        self.wait(2)
        self.play(*[FadeOut(m) for m in
                    [secA, ema_f, alpha_d, ema_note, axes,
                     price_segs, ema_segs, p_lbl, e_lbl]])

        # ── B. Continuous Compounding ────────────────────────────────────────
        secB = Text("B — Continuous Compounding of P&L", font_size=30, color=AMBER)
        secB.to_edge(UP)
        self.play(Write(secB))

        cc = Text(r"A \;=\; P \cdot e^{\,r \cdot t}", font_size=58)
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
            Text(r"A = 10{,}000 \cdot e^{0.005 \,\times\, 252}", font_size=30),
            Text(r"A = 10{,}000 \cdot e^{1.26}", font_size=30),
            Text("A  ~  $35,254   (252% return in one trading year)",
                 font_size=28, color=E_COLOR),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        steps.next_to(ex_title, DOWN, buff=0.3)

        for line in steps:
            self.play(FadeIn(line, shift=RIGHT * 0.2), run_time=0.55)
        self.wait(2)
        self.play(*[FadeOut(m) for m in [secB, cc, legend, ex_title, steps]])

        # ── C. Log Returns ───────────────────────────────────────────────────
        secC = Text("C — Log Returns (The Trader's e)", font_size=30, color=AMBER)
        secC.to_edge(UP)
        self.play(Write(secC))

        log_r = Text(
            r"r_{\log} = \ln\!\left(\frac{P_t}{P_{t-1}}\right)",
            font_size=44,
        )
        log_r.next_to(secC, DOWN, buff=0.5)
        self.play(Write(log_r))

        blist = bullet_list(
            "Additive over time  —  sum daily log returns for any period",
            "Symmetric  —  a +10% and -10% move cancel exactly",
            "Converts exponential growth into linear arithmetic",
            "Core input: Sharpe ratio, volatility, Black-Scholes pricing",
            font_size=27,
        )
        blist.next_to(log_r, DOWN, buff=0.45)
        self.play(FadeIn(blist, shift=UP * 0.2))
        self.wait(2.5)
        self.play(FadeOut(secC), FadeOut(log_r), FadeOut(blist))

        # End card
        end1 = Text("e powers every exponential edge in trading.",
                    font_size=30, color=E_COLOR)
        end2 = Text("e  =  2.71828…", font_size=48, color=AMBER)
        end2.next_to(end1, DOWN, buff=0.5)
        self.play(Write(end1), Write(end2))
        self.wait(2.5)
        self.play(FadeOut(end1), FadeOut(end2))


# ══════════════════════════════════════════════════════════════════════════════
#  FULL PRESENTATION — both scenes combined
# ══════════════════════════════════════════════════════════════════════════════
class FullPresentation(Scene):
    def construct(self):
        EulersNumber.construct(self)
        DayTradingExample.construct(self)