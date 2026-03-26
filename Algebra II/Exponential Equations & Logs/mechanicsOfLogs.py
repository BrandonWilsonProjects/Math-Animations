"""
Log Transform Educational Animation
=====================================
A comprehensive Manim animation explaining logarithmic data transformation
for students — covers intuition, mechanics, visual demos, and real-world use.

Run with:
    manim -pql log_transform.py LogTransformFull        # low quality preview
    manim -pqh log_transform.py LogTransformFull        # high quality
    manim -pqh log_transform.py Scene01_Intro           # individual scene

Requirements:
    pip install manim
"""

from manim import *
import numpy as np

# ─── Shared colour palette ────────────────────────────────────────────────────
C_BLUE   = "#4A90D9"
C_ORANGE = "#E8834A"
C_GREEN  = "#50C878"
C_RED    = "#E05C5C"
C_PURPLE = "#9B59B6"
C_YELLOW = "#F4D03F"
C_DARK   = "#1C2833"
C_LIGHT  = "#ECF0F1"
C_TEAL   = "#1ABC9C"

# ─── Helpers ──────────────────────────────────────────────────────────────────

def section_title(text: str, color=C_YELLOW) -> VGroup:
    bar  = Line(LEFT * 6, RIGHT * 6, color=color, stroke_width=2)
    label = Text(text, font_size=36, color=color, weight=BOLD)
    label.next_to(bar, UP, buff=0.15)
    return VGroup(label, bar)


def info_box(text: str, width=10, color=C_BLUE) -> VGroup:
    rect = RoundedRectangle(corner_radius=0.2, width=width, height=1.0,
                            color=color, fill_color=color, fill_opacity=0.12,
                            stroke_width=1.5)
    t = Text(text, font_size=22, color=C_LIGHT).move_to(rect)
    return VGroup(rect, t)


# ══════════════════════════════════════════════════════════════════════════════
# Scene 01 – Title & Motivation
# ══════════════════════════════════════════════════════════════════════════════
class Scene01_Intro(Scene):
    def construct(self):
        # ── Title ──
        title = Text("The Log Transform", font_size=64, color=C_YELLOW, weight=BOLD)
        sub   = Text("Taming Skewed & Explosive Data", font_size=30, color=C_LIGHT)
        sub.next_to(title, DOWN, buff=0.4)

        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(sub, shift=UP * 0.3))
        self.wait(1)

        # ── Motivation bullets ──
        bullets = VGroup(
            Text("• Data spanning many orders of magnitude", font_size=26, color=C_LIGHT),
            Text("• Heavy right-skewed distributions", font_size=26, color=C_LIGHT),
            Text("• Multiplicative relationships become additive", font_size=26, color=C_LIGHT),
            Text("• Stabilise variance  →  better models", font_size=26, color=C_LIGHT),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        bullets.next_to(sub, DOWN, buff=0.6)

        self.play(
            title.animate.scale(0.6).to_corner(UL),
            FadeOut(sub),
        )
        for b in bullets:
            self.play(FadeIn(b, shift=RIGHT * 0.4), run_time=0.5)
        self.wait(2)
        self.play(FadeOut(VGroup(bullets)))


# ══════════════════════════════════════════════════════════════════════════════
# Scene 02 – What IS a logarithm?
# ══════════════════════════════════════════════════════════════════════════════
class Scene02_WhatIsLog(Scene):
    def construct(self):
        title = section_title("What is a Logarithm?").to_edge(UP, buff=0.3)
        self.play(FadeIn(title))

        # Core definition
        defn = MathTex(
            r"\log_b(x) = y", r"\quad\Longleftrightarrow\quad", r"b^y = x",
            font_size=52
        )
        defn[0].set_color(C_ORANGE)
        defn[2].set_color(C_BLUE)
        defn.move_to(UP * 1.5)
        self.play(Write(defn), run_time=2)
        self.wait(0.5)

        # Concrete example
        ex = MathTex(r"\log_{10}(1000) = 3", r"\quad\Longleftrightarrow\quad",
                     r"10^3 = 1000", font_size=42)
        ex[0].set_color(C_ORANGE)
        ex[2].set_color(C_BLUE)
        ex.next_to(defn, DOWN, buff=0.6)
        self.play(Write(ex))
        self.wait(0.5)

        # "Asks the question" annotation
        q = Text('"How many times must I multiply b by itself to get x?"',
                 font_size=24, color=C_TEAL, slant=ITALIC)
        q.next_to(ex, DOWN, buff=0.5)
        self.play(FadeIn(q, shift=UP * 0.2))
        self.wait(1.5)

        # Powers-of-10 ladder
        ladder_title = Text("Powers-of-10 ladder:", font_size=28, color=C_YELLOW)
        ladder_title.next_to(q, DOWN, buff=0.5)
        self.play(Write(ladder_title))

        steps = [
            (r"10^0 = 1",       r"\;\Rightarrow\;\log_{10}(1)=0"),
            (r"10^1 = 10",      r"\;\Rightarrow\;\log_{10}(10)=1"),
            (r"10^2 = 100",     r"\;\Rightarrow\;\log_{10}(100)=2"),
            (r"10^3 = 1\,000",  r"\;\Rightarrow\;\log_{10}(1000)=3"),
            (r"10^6 = 1\,000\,000", r"\;\Rightarrow\;\log_{10}(1\,000\,000)=6"),
        ]
        ladder = VGroup()
        for a, b in steps:
            row = MathTex(a + b, font_size=28)
            row[0][:len(a)].set_color(C_BLUE)
            ladder.add(row)
        ladder.arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        ladder.next_to(ladder_title, DOWN, buff=0.2)
        self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.3) for r in ladder],
                              lag_ratio=0.25))
        self.wait(2)
        self.play(FadeOut(VGroup(title, defn, ex, q, ladder_title, ladder)))


# ══════════════════════════════════════════════════════════════════════════════
# Scene 03 – Graph of log(x)
# ══════════════════════════════════════════════════════════════════════════════
class Scene03_LogGraph(Scene):
    def construct(self):
        title = section_title("Graph of  log₁₀(x)").to_edge(UP, buff=0.3)
        self.play(FadeIn(title))

        axes = Axes(
            x_range=[0.01, 120, 20],
            y_range=[-2.5, 2.5, 0.5],
            x_length=9,
            y_length=5,
            axis_config={"color": C_LIGHT, "include_tip": True},
        ).shift(DOWN * 0.3)
        x_label = axes.get_x_axis_label("x", direction=RIGHT)
        y_label = axes.get_y_axis_label(r"\log_{10}(x)", direction=UP)

        self.play(Create(axes), Write(x_label), Write(y_label))

        log_curve = axes.plot(lambda x: np.log10(x), x_range=[0.01, 120],
                              color=C_ORANGE, stroke_width=3)
        self.play(Create(log_curve), run_time=2)

        # Annotate key points
        key_pts = [(1, 0), (10, 1), (100, 2), (0.1, -1)]
        dots = VGroup()
        labels_g = VGroup()
        for xv, yv in key_pts:
            if 0.01 <= xv <= 120 and -2.5 <= yv <= 2.5:
                dot = Dot(axes.c2p(xv, yv), color=C_YELLOW, radius=0.08)
                lbl = MathTex(rf"({xv},\,{yv})", font_size=22, color=C_YELLOW)
                lbl.next_to(dot, UR, buff=0.1)
                dots.add(dot)
                labels_g.add(lbl)

        self.play(LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.3))
        self.play(LaggedStart(*[Write(l) for l in labels_g], lag_ratio=0.3))
        self.wait(0.5)

        # Highlight compression behaviour
        arr1 = Arrow(axes.c2p(1,0), axes.c2p(10,1), color=C_GREEN, buff=0)
        arr2 = Arrow(axes.c2p(10,1), axes.c2p(100,2), color=C_GREEN, buff=0)
        note1 = Text("×10 → +1", font_size=22, color=C_GREEN).next_to(arr1, RIGHT, buff=0.1)
        note2 = Text("×10 → +1", font_size=22, color=C_GREEN).next_to(arr2, RIGHT, buff=0.1)

        self.play(GrowArrow(arr1), Write(note1))
        self.play(GrowArrow(arr2), Write(note2))

        insight = info_box("Multiplying x by 10 always adds exactly 1 to log(x)  →  compression!",
                           color=C_TEAL).to_edge(DOWN, buff=0.2)
        self.play(FadeIn(insight))
        self.wait(2.5)
        self.play(FadeOut(VGroup(title, axes, x_label, y_label, log_curve,
                                  dots, labels_g, arr1, arr2, note1, note2, insight)))


# ══════════════════════════════════════════════════════════════════════════════
# Scene 04 – Key Log Rules (animated derivation)
# ══════════════════════════════════════════════════════════════════════════════
class Scene04_LogRules(Scene):
    def construct(self):
        title = section_title("Key Logarithm Rules").to_edge(UP, buff=0.3)
        self.play(FadeIn(title))

        rules = VGroup(
            MathTex(r"\log(a \cdot b) = \log(a) + \log(b)",
                    font_size=42, color=C_ORANGE),
            MathTex(r"\log\!\left(\frac{a}{b}\right) = \log(a) - \log(b)",
                    font_size=42, color=C_BLUE),
            MathTex(r"\log(a^n) = n\cdot\log(a)",
                    font_size=42, color=C_GREEN),
            MathTex(r"\log_b(x) = \frac{\ln(x)}{\ln(b)}\quad\text{(change of base)}",
                    font_size=36, color=C_PURPLE),
        ).arrange(DOWN, buff=0.55, aligned_edge=LEFT)
        rules.move_to(ORIGIN + LEFT * 0.5)

        tags = VGroup(
            Text("Product rule",      font_size=22, color=C_ORANGE),
            Text("Quotient rule",     font_size=22, color=C_BLUE),
            Text("Power rule",        font_size=22, color=C_GREEN),
            Text("Change-of-base",    font_size=22, color=C_PURPLE),
        )
        for tag, rule in zip(tags, rules):
            tag.next_to(rule, RIGHT, buff=0.4)

        for rule, tag in zip(rules, tags):
            self.play(Write(rule), FadeIn(tag, shift=LEFT * 0.2), run_time=0.9)
            self.wait(0.3)

        # Numeric demo for product rule
        demo_bg = SurroundingRectangle(rules[0], color=C_ORANGE, buff=0.15,
                                       corner_radius=0.1)
        demo = MathTex(
            r"\log_{10}(2 \times 5) = \log_{10}(2)+\log_{10}(5)"
            r"\approx 0.301+0.699 = 1",
            font_size=30, color=C_LIGHT
        ).next_to(rules[-1], DOWN, buff=0.5)

        self.play(Create(demo_bg))
        self.play(Write(demo), run_time=1.5)
        self.wait(2.5)
        self.play(FadeOut(VGroup(title, rules, tags, demo_bg, demo)))


# ══════════════════════════════════════════════════════════════════════════════
# Scene 05 – Skewed vs Log-Transformed Distribution (bar charts)
# ══════════════════════════════════════════════════════════════════════════════
class Scene05_DistributionTransform(Scene):
    def construct(self):
        title = section_title("Skewed Data  →  Log Transform").to_edge(UP, buff=0.25)
        self.play(FadeIn(title))

        # --- Raw exponential-like data (income simulation) ---
        np.random.seed(42)
        raw  = np.concatenate([
            np.random.exponential(scale=5, size=120),
            np.random.exponential(scale=50, size=10),
        ])
        raw = np.sort(raw)
        log_raw = np.log10(raw + 1)

        def make_histogram(data, x_range, n_bins, axes_kw, label_str, color):
            axes = Axes(x_range=x_range, y_range=[0, 1.1], **axes_kw,
                        axis_config={"color": C_LIGHT})
            counts, edges = np.histogram(data, bins=n_bins,
                                         range=(x_range[0], x_range[1]))
            counts = counts / counts.max()
            bars = VGroup()
            for i, (cnt, left, right) in enumerate(
                    zip(counts, edges[:-1], edges[1:])):
                if cnt == 0:
                    continue
                bl = axes.c2p(left, 0)
                tr = axes.c2p(right, cnt)
                rect = Rectangle(
                    width=abs(tr[0]-bl[0]),
                    height=abs(tr[1]-bl[1]),
                    fill_color=color,
                    fill_opacity=0.75,
                    stroke_width=0.5,
                    stroke_color=WHITE,
                )
                rect.move_to((bl+tr)/2)
                bars.add(rect)
            lbl = Text(label_str, font_size=24, color=color).next_to(axes, UP, buff=0.15)
            return VGroup(axes, bars, lbl)

        raw_hist = make_histogram(
            raw, [0, 160, 40], 20,
            dict(x_length=5.5, y_length=3.5),
            "Raw Income Data  (right-skewed)", C_RED
        ).shift(LEFT * 3.5 + DOWN * 0.5)

        log_hist = make_histogram(
            log_raw, [0, 2.5, 0.5], 20,
            dict(x_length=5.5, y_length=3.5),
            "After log₁₀ transform  (near-normal)", C_GREEN
        ).shift(RIGHT * 3.5 + DOWN * 0.5)

        self.play(FadeIn(raw_hist[0]))
        self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in raw_hist[1]],
                               lag_ratio=0.04), Write(raw_hist[2]))
        self.wait(0.8)

        arrow = Arrow(raw_hist.get_right(), log_hist.get_left(),
                      color=C_YELLOW, stroke_width=4)
        log_label = MathTex(r"x' = \log_{10}(x+1)", font_size=28, color=C_YELLOW)
        log_label.next_to(arrow, UP, buff=0.15)

        self.play(GrowArrow(arrow), Write(log_label))
        self.play(FadeIn(log_hist[0]))
        self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in log_hist[1]],
                               lag_ratio=0.04), Write(log_hist[2]))
        self.wait(1)

        note = info_box("The log transform compresses large values & spreads small ones → symmetry!",
                        color=C_TEAL).to_edge(DOWN, buff=0.2)
        self.play(FadeIn(note))
        self.wait(3)
        self.play(FadeOut(VGroup(title, raw_hist, log_hist, arrow, log_label, note)))


# ══════════════════════════════════════════════════════════════════════════════
# Scene 06 – Point-by-Point Transformation (animated)
# ══════════════════════════════════════════════════════════════════════════════
class Scene06_PointTransform(Scene):
    def construct(self):
        title = section_title("Point-by-Point: Watch Values Move").to_edge(UP, buff=0.25)
        self.play(FadeIn(title))

        # Two number lines
        raw_line = NumberLine(x_range=[0, 1000, 100], length=11,
                               include_numbers=True, font_size=18,
                               color=C_LIGHT).shift(UP * 1.2)
        log_line = NumberLine(x_range=[0, 3, 0.5], length=11,
                               include_numbers=True, font_size=18,
                               color=C_LIGHT).shift(DOWN * 1.5)

        raw_lbl = Text("Original scale", font_size=24, color=C_RED).next_to(raw_line, LEFT, buff=0.2)
        log_lbl = Text("Log₁₀ scale",    font_size=24, color=C_GREEN).next_to(log_line, LEFT, buff=0.2)

        self.play(Create(raw_line), Write(raw_lbl))
        self.play(Create(log_line), Write(log_lbl))

        values = [1, 10, 100, 500, 1000]
        colors  = [C_YELLOW, C_ORANGE, C_BLUE, C_PURPLE, C_TEAL]

        raw_dots  = VGroup()
        log_dots  = VGroup()
        val_labels = VGroup()
        log_labels = VGroup()

        for v, col in zip(values, colors):
            rd = Dot(raw_line.n2p(v), color=col, radius=0.12)
            lv = np.log10(v)
            ld = Dot(log_line.n2p(lv), color=col, radius=0.12)
            vl = MathTex(str(v), font_size=22, color=col).next_to(rd, UP, buff=0.15)
            ll = MathTex(rf"{lv:.1f}", font_size=22, color=col).next_to(ld, DOWN, buff=0.15)
            raw_dots.add(rd)
            log_dots.add(ld)
            val_labels.add(vl)
            log_labels.add(ll)

        # Show raw dots one by one
        for rd, vl in zip(raw_dots, val_labels):
            self.play(FadeIn(rd), Write(vl), run_time=0.4)

        self.wait(0.5)

        # Transform each dot with a curving arc
        for rd, ld, vl, ll, col in zip(raw_dots, log_dots, val_labels, log_labels, colors):
            ghost = rd.copy().set_color(col)
            path  = ArcBetweenPoints(rd.get_center(), ld.get_center(),
                                     angle=-TAU / 4, color=col)
            self.play(
                MoveAlongPath(ghost, path),
                FadeIn(ld),
                Write(ll),
                run_time=0.7,
            )
            self.remove(ghost)

        # Spacing annotation
        brace_raw = BraceBetweenPoints(raw_line.n2p(100), raw_line.n2p(1000),
                                        direction=UP, color=C_YELLOW)
        brace_raw_lbl = brace_raw.get_text("900 units apart", font_size=20)
        brace_log = BraceBetweenPoints(log_line.n2p(2), log_line.n2p(3),
                                        direction=DOWN, color=C_YELLOW)
        brace_log_lbl = brace_log.get_text("1 unit apart", font_size=20)

        self.play(Create(brace_raw), Write(brace_raw_lbl))
        self.play(Create(brace_log), Write(brace_log_lbl))
        self.wait(2.5)
        self.play(FadeOut(VGroup(title, raw_line, log_line, raw_lbl, log_lbl,
                                  raw_dots, log_dots, val_labels, log_labels,
                                  brace_raw, brace_raw_lbl, brace_log, brace_log_lbl)))


# ══════════════════════════════════════════════════════════════════════════════
# Scene 07 – Multiplicative → Additive (the secret superpower)
# ══════════════════════════════════════════════════════════════════════════════
class Scene07_MultiplicativeAdditive(Scene):
    def construct(self):
        title = section_title("Multiplicative  →  Additive").to_edge(UP, buff=0.3)
        self.play(FadeIn(title))

        # Step 1: show multiplicative growth table
        table_data = [
            ["Year", "Value", "log₁₀(Value)"],
            ["0",    "100",   "2.000"],
            ["1",    "200",   "2.301"],
            ["2",    "400",   "2.602"],
            ["3",    "800",   "2.903"],
            ["4",    "1600",  "3.204"],
        ]
        tbl = Table(
            table_data[1:],
            col_labels=[Text(h, font_size=22, color=C_YELLOW) for h in table_data[0]],
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": GREY},
            element_to_mobject=lambda s: Text(s, font_size=22, color=C_LIGHT),
        ).scale(0.75).shift(LEFT * 2.8 + DOWN * 0.3)
        self.play(FadeIn(tbl))
        self.wait(0.5)

        # Annotate constant ratio vs constant difference
        r_brace = Brace(tbl.get_columns()[1], RIGHT, color=C_RED)
        r_text  = Text("×2 each year", font_size=22, color=C_RED).next_to(r_brace, RIGHT)
        self.play(GrowFromCenter(r_brace), Write(r_text))

        d_brace = Brace(tbl.get_columns()[2], RIGHT, color=C_GREEN)
        d_text  = Text("+0.301 each year", font_size=22, color=C_GREEN).next_to(d_brace, RIGHT)
        self.play(
            r_brace.animate.shift(RIGHT * 1.8),
            r_text.animate.shift(RIGHT * 1.8),
        )
        self.play(GrowFromCenter(d_brace), Write(d_text))

        # Rule reminder
        reminder = MathTex(
            r"\log(x \cdot 2) = \log(x) + \log(2)",
            font_size=34, color=C_ORANGE
        ).to_edge(DOWN, buff=0.5)
        self.play(Write(reminder))
        self.wait(2)

        # Show: on log scale, exponential growth becomes linear
        self.play(FadeOut(VGroup(tbl, r_brace, r_text, d_brace, d_text, reminder)))

        axes = Axes(
            x_range=[0, 4.5, 1], y_range=[0, 2000, 400],
            x_length=5, y_length=3.5,
            axis_config={"color": C_LIGHT},
        ).shift(LEFT * 3 + DOWN * 0.3)
        ax2 = Axes(
            x_range=[0, 4.5, 1], y_range=[1.8, 3.4, 0.4],
            x_length=5, y_length=3.5,
            axis_config={"color": C_LIGHT},
        ).shift(RIGHT * 3 + DOWN * 0.3)

        curve1 = axes.plot(lambda x: 100 * 2**x, color=C_RED,   stroke_width=3)
        curve2 = ax2.plot(lambda x: np.log10(100 * 2**x), color=C_GREEN, stroke_width=3)

        lbl1 = Text("Raw scale (exponential)", font_size=20, color=C_RED).next_to(axes, UP, buff=0.1)
        lbl2 = Text("Log scale (linear!)",     font_size=20, color=C_GREEN).next_to(ax2, UP, buff=0.1)

        self.play(Create(axes), Create(ax2), Write(lbl1), Write(lbl2))
        self.play(Create(curve1), Create(curve2), run_time=2)
        self.wait(2.5)
        self.play(FadeOut(VGroup(title, axes, ax2, curve1, curve2, lbl1, lbl2)))


# ══════════════════════════════════════════════════════════════════════════════
# Scene 08 – Variance Stabilisation
# ══════════════════════════════════════════════════════════════════════════════
class Scene08_VarianceStabilisation(Scene):
    def construct(self):
        title = section_title("Variance Stabilisation").to_edge(UP, buff=0.3)
        self.play(FadeIn(title))

        # Show heteroscedastic scatter, then transformed
        np.random.seed(7)
        xs = np.array([1, 2, 5, 10, 20, 50, 100])
        raw_pts = []
        for x in xs:
            ys = x * (1 + np.random.normal(0, 0.25, 8))
            for y in ys:
                raw_pts.append((x, y))

        def scatter_axes(x_range, y_range, x_len, y_len, x_lbl, y_lbl, pos):
            ax = Axes(x_range=x_range, y_range=y_range,
                      x_length=x_len, y_length=y_len,
                      axis_config={"color": C_LIGHT}
                      ).shift(pos)
            xl = ax.get_x_axis_label(x_lbl)
            yl = ax.get_y_axis_label(y_lbl)
            return ax, xl, yl

        ax_raw, xl_r, yl_r = scatter_axes(
            [0, 110, 20], [0, 130, 20], 5, 3.5, "x", "y", LEFT*3.2+DOWN*0.4)
        ax_log, xl_l, yl_l = scatter_axes(
            [0, 2.2, 0.5], [0, 2.2, 0.5], 5, 3.5,
            r"\log(x)", r"\log(y)", RIGHT*3.2+DOWN*0.4)

        dots_raw = VGroup()
        dots_log = VGroup()
        for (x, y) in raw_pts:
            if 0 < x < 110 and 0 < y < 130:
                dots_raw.add(Dot(ax_raw.c2p(x, y), radius=0.06,
                                 color=C_RED, fill_opacity=0.7))
            if x > 0 and y > 0:
                lx, ly = np.log10(x), np.log10(y)
                if 0 <= lx <= 2.2 and 0 <= ly <= 2.2:
                    dots_log.add(Dot(ax_log.c2p(lx, ly), radius=0.06,
                                     color=C_GREEN, fill_opacity=0.7))

        lbl_r = Text("Heteroscedastic", font_size=22, color=C_RED).next_to(ax_raw, UP, buff=0.1)
        lbl_l = Text("Stabilised variance", font_size=22, color=C_GREEN).next_to(ax_log, UP, buff=0.1)

        self.play(Create(ax_raw), Write(xl_r), Write(yl_r), Write(lbl_r))
        self.play(LaggedStart(*[FadeIn(d) for d in dots_raw], lag_ratio=0.02))
        self.wait(0.5)

        arrow = Arrow(ax_raw.get_right(), ax_log.get_left(), color=C_YELLOW, stroke_width=4)
        log_note = MathTex(r"\log(\cdot)", font_size=28, color=C_YELLOW).next_to(arrow, UP)
        self.play(GrowArrow(arrow), Write(log_note))

        self.play(Create(ax_log), Write(xl_l), Write(yl_l), Write(lbl_l))
        self.play(LaggedStart(*[FadeIn(d) for d in dots_log], lag_ratio=0.02))
        self.wait(2.5)
        self.play(FadeOut(VGroup(title, ax_raw, ax_log, xl_r, yl_r, xl_l, yl_l,
                                  dots_raw, dots_log, lbl_r, lbl_l, arrow, log_note)))


# ══════════════════════════════════════════════════════════════════════════════
# Scene 09 – Natural log vs log₁₀ vs log₂
# ══════════════════════════════════════════════════════════════════════════════
class Scene09_BasesComparison(Scene):
    def construct(self):
        title = section_title("Comparing Bases: ln, log₁₀, log₂").to_edge(UP, buff=0.3)
        self.play(FadeIn(title))

        axes = Axes(
            x_range=[0.01, 20, 4],
            y_range=[-2, 4.5, 1],
            x_length=9, y_length=5,
            axis_config={"color": C_LIGHT, "include_tip": True},
        ).shift(DOWN * 0.4)

        funcs = [
            (np.log,   "ln(x)  — natural log",  C_ORANGE),
            (np.log10, "log₁₀(x) — common log", C_BLUE),
            (np.log2,  "log₂(x)  — binary log",  C_GREEN),
        ]

        curves = VGroup()
        legends = VGroup()
        for i, (fn, name, col) in enumerate(funcs):
            curve = axes.plot(lambda x, f=fn: f(x), x_range=[0.05, 20],
                              color=col, stroke_width=3)
            leg = VGroup(
                Line(ORIGIN, RIGHT * 0.5, color=col, stroke_width=3),
                Text(name, font_size=22, color=col)
            ).arrange(RIGHT, buff=0.2)
            curves.add(curve)
            legends.add(leg)

        legends.arrange(DOWN, buff=0.25, aligned_edge=LEFT).to_corner(UR).shift(LEFT * 0.3 + DOWN * 0.5)

        self.play(Create(axes))
        for curve, leg in zip(curves, legends):
            self.play(Create(curve, run_time=1.2), FadeIn(leg))
        self.wait(0.5)

        # All share the same shape – just scaled
        note = info_box("All log bases have the same shape — just scaled by a constant  (change-of-base).",
                        color=C_TEAL).to_edge(DOWN, buff=0.2)
        self.play(FadeIn(note))
        self.wait(2.5)
        self.play(FadeOut(VGroup(title, axes, curves, legends, note)))


# ══════════════════════════════════════════════════════════════════════════════
# Scene 10 – When NOT to use log transform
# ══════════════════════════════════════════════════════════════════════════════
class Scene10_Caveats(Scene):
    def construct(self):
        title = section_title("Caveats & When NOT to Use It", color=C_RED).to_edge(UP, buff=0.3)
        self.play(FadeIn(title))

        items = [
            ("⚠  Zeros & Negatives",
             "log(0) = −∞   and   log(x) undefined for x < 0\n"
             "Fix: use log(x+1) or log(x+c) for a small constant c"),
            ("⚠  Already-normal data",
             "If your data is symmetric & unimodal, log can introduce\n"
             "left-skew — making things worse, not better!"),
            ("⚠  Interpretability cost",
             "Regression coefficients are now on the log scale.\n"
             "Always back-transform predictions: ŷ = 10^(ŷ_log)"),
            ("⚠  Negative counts / differences",
             "Differences and residuals can be negative.\n"
             "Log-transform raw values, not differences."),
        ]

        boxes = VGroup()
        for head, body in items:
            title_t = Text(head, font_size=24, color=C_RED, weight=BOLD)
            body_t  = Text(body, font_size=20, color=C_LIGHT, line_spacing=1.3)
            body_t.next_to(title_t, DOWN, buff=0.15, aligned_edge=LEFT)
            rect = SurroundingRectangle(VGroup(title_t, body_t),
                                         color=C_RED, buff=0.2, corner_radius=0.15,
                                         fill_color=C_DARK, fill_opacity=0.6)
            grp = VGroup(rect, title_t, body_t)
            boxes.add(grp)

        boxes.arrange_in_grid(rows=2, cols=2, buff=0.4).shift(DOWN * 0.3)

        for box in boxes:
            self.play(FadeIn(box, scale=0.9), run_time=0.7)
            self.wait(0.3)

        self.wait(2)
        self.play(FadeOut(VGroup(title, boxes)))


# ══════════════════════════════════════════════════════════════════════════════
# Scene 11 – Real-World Examples
# ══════════════════════════════════════════════════════════════════════════════
class Scene11_RealWorld(Scene):
    def construct(self):
        title = section_title("Real-World Uses of Log Transform").to_edge(UP, buff=0.3)
        self.play(FadeIn(title))

        examples = VGroup(
            VGroup(
                Text("💰 Income & Wealth", font_size=26, color=C_YELLOW, weight=BOLD),
                Text("Incomes span $10k – $100B+.\nLog makes distribution near-normal for modeling.",
                     font_size=21, color=C_LIGHT, line_spacing=1.3),
            ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            VGroup(
                Text("🌍 Earthquake Magnitude (Richter)", font_size=26, color=C_ORANGE, weight=BOLD),
                Text("Each +1 on the scale = ×10 in ground motion amplitude.",
                     font_size=21, color=C_LIGHT, line_spacing=1.3),
            ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            VGroup(
                Text("🔊 Sound (Decibels)", font_size=26, color=C_GREEN, weight=BOLD),
                Text("dB = 10 × log₁₀(I / I₀). Human hearing spans 12 orders of magnitude.",
                     font_size=21, color=C_LIGHT, line_spacing=1.3),
            ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            VGroup(
                Text("🧬 Gene Expression", font_size=26, color=C_BLUE, weight=BOLD),
                Text("RNA-seq counts: log₂ fold-change is the standard\nbecause ×2 change is biologically symmetric.",
                     font_size=21, color=C_LIGHT, line_spacing=1.3),
            ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            VGroup(
                Text("📈 Stock Prices", font_size=26, color=C_PURPLE, weight=BOLD),
                Text("Returns modeled as log-normal. Log returns are additive over time.",
                     font_size=21, color=C_LIGHT, line_spacing=1.3),
            ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            VGroup(
                Text("🌐 Web Traffic / Zipf's Law", font_size=26, color=C_TEAL, weight=BOLD),
                Text("Word frequencies, city sizes follow power laws.\nLog-log plot reveals a straight line.",
                     font_size=21, color=C_LIGHT, line_spacing=1.3),
            ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
        )

        examples.arrange_in_grid(rows=3, cols=2, buff=0.5).shift(DOWN * 0.2)

        for ex in examples:
            rect = SurroundingRectangle(ex, buff=0.18, corner_radius=0.1,
                                         stroke_width=1, color=GREY_B,
                                         fill_color="#1e2d3a", fill_opacity=0.6)
            ex.add_to_back(rect)
            self.play(FadeIn(ex, scale=0.92), run_time=0.5)
        self.wait(3)
        self.play(FadeOut(VGroup(title, examples)))


# ══════════════════════════════════════════════════════════════════════════════
# Scene 12 – Summary Cheat Sheet
# ══════════════════════════════════════════════════════════════════════════════
class Scene12_Summary(Scene):
    def construct(self):
        title = Text("Log Transform — Summary Cheat Sheet",
                     font_size=38, color=C_YELLOW, weight=BOLD).to_edge(UP, buff=0.3)
        self.play(Write(title))

        rows = [
            ("What it does",      r"x \;\mapsto\; \log(x)",            C_ORANGE),
            ("Compresses range",  r"1,\,10,\,100,\,1000 \;\to\; 0,1,2,3", C_BLUE),
            ("Product → sum",     r"\log(ab) = \log a + \log b",       C_GREEN),
            ("Power → product",   r"\log(a^n) = n\log a",              C_PURPLE),
            ("Fixes right skew",  "heavy tail → near-normal",           C_TEAL),
            ("Stabilises σ",      "variance grows with mean → constant", C_RED),
            ("Watch out for",     "zeros, negatives, already-normal data", C_YELLOW),
        ]

        tbl_rows = []
        for label, formula, col in rows:
            t1 = Text(label, font_size=22, color=col)
            t2 = MathTex(formula, font_size=22, color=C_LIGHT) \
                 if "\\" in formula else Text(formula, font_size=22, color=C_LIGHT)
            tbl_rows.append(VGroup(t1, t2))

        table_group = VGroup()
        for row in tbl_rows:
            row[0].set_width(3.5)
            row[1].set_width(6)
            row.arrange(RIGHT, buff=0.5, aligned_edge=LEFT)
            sep = Line(LEFT * 5.5, RIGHT * 5.5, stroke_width=0.5, color=GREY)
            table_group.add(row, sep)

        table_group.arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        table_group.next_to(title, DOWN, buff=0.4)

        for item in table_group:
            self.play(FadeIn(item, shift=RIGHT * 0.3), run_time=0.35)

        self.wait(3)

        goodbye = Text("Good luck transforming your data! 🚀",
                       font_size=32, color=C_YELLOW).to_edge(DOWN, buff=0.4)
        self.play(Write(goodbye))
        self.wait(2)


# ══════════════════════════════════════════════════════════════════════════════
# FULL COMBINED SCENE  (renders all scenes in sequence)
# ══════════════════════════════════════════════════════════════════════════════
class LogTransformFull(Scene):
    """Run this to get the complete educational video."""

    def construct(self):
        for SceneCls in [
            Scene01_Intro,
            Scene02_WhatIsLog,
            Scene03_LogGraph,
            Scene04_LogRules,
            Scene05_DistributionTransform,
            Scene06_PointTransform,
            Scene07_MultiplicativeAdditive,
            Scene08_VarianceStabilisation,
            Scene09_BasesComparison,
            Scene10_Caveats,
            Scene11_RealWorld,
            Scene12_Summary,
        ]:
            scene = SceneCls()
            scene.camera = self.camera
            scene.renderer = self.renderer
            scene.construct()
            self.wait(0.5)