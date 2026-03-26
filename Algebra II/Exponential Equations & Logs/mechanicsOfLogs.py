from manim import *
import numpy as np

# ---------------------------------------------------------------------------
# Colour palette
# ---------------------------------------------------------------------------
C_BLUE   = "#4A90D9"
C_ORANGE = "#E8834A"
C_GREEN  = "#50C878"
C_RED    = "#E05C5C"
C_PURPLE = "#9B59B6"
C_YELLOW = "#F4D03F"
C_DARK   = "#1C2833"
C_LIGHT  = "#ECF0F1"
C_TEAL   = "#1ABC9C"

# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

def make_section_title(text: str, color=C_YELLOW) -> VGroup:
    bar   = Line(LEFT * 6, RIGHT * 6, color=color, stroke_width=2)
    label = Text(text, font_size=36, color=color, weight=BOLD)
    label.next_to(bar, UP, buff=0.15)
    return VGroup(label, bar)


def make_info_box(text: str, width=10, color=C_BLUE) -> VGroup:
    rect = RoundedRectangle(
        corner_radius=0.2, width=width, height=1.0,
        color=color, fill_color=color, fill_opacity=0.12, stroke_width=1.5,
    )
    t = Text(text, font_size=20, color=C_LIGHT).move_to(rect)
    return VGroup(rect, t)


# ---------------------------------------------------------------------------
# Per-scene build functions
# Each function receives `self` (a Scene instance) and draws + clears its content.
# This pattern lets us call them from both standalone classes AND LogTransformFull.
# ---------------------------------------------------------------------------

def build_s01(self):
    title = Text("The Log Transform", font_size=64, color=C_YELLOW, weight=BOLD)
    sub   = Text("Taming Skewed & Explosive Data", font_size=30, color=C_LIGHT)
    sub.next_to(title, DOWN, buff=0.4)
    self.play(Write(title), run_time=1.5)
    self.play(FadeIn(sub, shift=UP * 0.3))
    self.wait(1)

    bullets = VGroup(
        Text("• Data spanning many orders of magnitude",       font_size=26, color=C_LIGHT),
        Text("• Heavy right-skewed distributions",             font_size=26, color=C_LIGHT),
        Text("• Multiplicative relationships become additive", font_size=26, color=C_LIGHT),
        Text("• Stabilise variance  ->  better models",        font_size=26, color=C_LIGHT),
    ).arrange(UP, aligned_edge=LEFT, buff=0.35)
    bullets.next_to(sub, DOWN, buff=0.6)

    self.play(title.animate.scale(0.6).to_corner(UL), FadeOut(sub))
    for b in bullets:
        self.play(FadeIn(b, shift=RIGHT * 0.4), run_time=0.5)
    self.wait(2)
    self.play(FadeOut(VGroup(title, bullets)))


def build_s02(self):
    title = make_section_title("What is a Logarithm?").to_edge(UP, buff=0.3)
    self.play(FadeIn(title))

    defn = MathTex(r"\log_b(x) = y", r"\quad\Longleftrightarrow\quad", r"b^y = x", font_size=52)
    defn[0].set_color(C_ORANGE)
    defn[2].set_color(C_BLUE)
    defn.move_to(UP * 1.8)
    self.play(Write(defn), run_time=2)
    self.wait(0.5)

    ex = MathTex(r"\log_{10}(1000)=3", r"\quad\Longleftrightarrow\quad", r"10^3=1000", font_size=42)
    ex[0].set_color(C_ORANGE)
    ex[2].set_color(C_BLUE)
    ex.next_to(defn, DOWN, buff=0.5)
    self.play(Write(ex))
    self.wait(0.5)

    q = Text('"How many times must I multiply b by itself to get x?"',
             font_size=24, color=C_TEAL, slant=ITALIC)
    q.next_to(ex, DOWN, buff=0.45)
    self.play(FadeIn(q, shift=UP * 0.2))
    self.wait(1.2)

    ladder_title = Text("Powers-of-10 ladder:", font_size=26, color=C_YELLOW)
    ladder_title.next_to(q, DOWN, buff=0.4)
    self.play(Write(ladder_title))

    rows_data = [
        (r"10^0 = 1",             r"\;\Rightarrow\;\log_{10}(1)=0"),
        (r"10^1 = 10",            r"\;\Rightarrow\;\log_{10}(10)=1"),
        (r"10^2 = 100",           r"\;\Rightarrow\;\log_{10}(100)=2"),
        (r"10^3 = 1{,}000",       r"\;\Rightarrow\;\log_{10}(1000)=3"),
        (r"10^6 = 1{,}000{,}000", r"\;\Rightarrow\;\log_{10}(10^6)=6"),
    ]
    ladder = VGroup(*[MathTex(a + b, font_size=26) for a, b in rows_data])
    ladder.arrange(DOWN, buff=0.15, aligned_edge=LEFT)
    ladder.next_to(ladder_title, DOWN, buff=0.18)
    self.play(LaggedStart(*[FadeIn(r, shift=RIGHT * 0.3) for r in ladder], lag_ratio=0.2))
    self.wait(2)
    self.play(FadeOut(VGroup(title, defn, ex, q, ladder_title, ladder)))


def build_s03(self):
    title = make_section_title("Graph of log10(x)").to_edge(UP, buff=0.3)
    self.play(FadeIn(title))

    axes = Axes(
        x_range=[0.01, 120, 20], y_range=[-2.5, 2.5, 0.5],
        x_length=9, y_length=5,
        axis_config={"color": C_LIGHT, "include_tip": True},
    ).shift(DOWN * 0.3)
    x_lbl = axes.get_x_axis_label("x", direction=RIGHT)
    y_lbl = axes.get_y_axis_label(r"\log_{10}(x)", direction=UP)
    self.play(Create(axes), Write(x_lbl), Write(y_lbl))

    log_curve = axes.plot(np.log10, x_range=[0.01, 120], color=C_ORANGE, stroke_width=3)
    self.play(Create(log_curve), run_time=2)

    key_pts = [(1, 0, UR), (10, 1, UR), (100, 2, UR), (0.1, -1, DR)]
    dots, lbls = VGroup(), VGroup()
    for xv, yv, dir_ in key_pts:
        d = Dot(axes.c2p(xv, yv), color=C_YELLOW, radius=0.08)
        l = MathTex(rf"({xv},\,{yv})", font_size=20, color=C_YELLOW).next_to(d, dir_, buff=0.1)
        dots.add(d)
        lbls.add(l)

    self.play(LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.3))
    self.play(LaggedStart(*[Write(l) for l in lbls],  lag_ratio=0.3))
    self.wait(0.4)

    arr1  = Arrow(axes.c2p(1, 0),  axes.c2p(10, 1), color=C_GREEN, buff=0, stroke_width=3)
    arr2  = Arrow(axes.c2p(10, 1), axes.c2p(100, 2), color=C_GREEN, buff=0, stroke_width=3)
    note1 = Text("x10 -> +1", font_size=22, color=C_GREEN).next_to(arr1, RIGHT, buff=0.08)
    note2 = Text("x10 -> +1", font_size=22, color=C_GREEN).next_to(arr2, RIGHT, buff=0.08)
    self.play(GrowArrow(arr1), Write(note1))
    self.play(GrowArrow(arr2), Write(note2))

    box = make_info_box(
        "Multiplying x by 10 always adds exactly 1 to log(x)  ->  massive compression!"
    ).to_edge(DOWN, buff=0.2)
    self.play(FadeIn(box))
    self.wait(2.5)
    self.play(FadeOut(VGroup(title, axes, x_lbl, y_lbl, log_curve,
                              dots, lbls, arr1, arr2, note1, note2, box)))


def build_s04(self):
    title = make_section_title("Key Logarithm Rules").to_edge(UP, buff=0.3)
    self.play(FadeIn(title))

    rule_data = [
        (r"\log(a \cdot b) = \log(a) + \log(b)",                     "Product rule",    C_ORANGE),
        (r"\log\!\left(\tfrac{a}{b}\right) = \log(a) - \log(b)",     "Quotient rule",   C_BLUE),
        (r"\log(a^n) = n\cdot\log(a)",                                "Power rule",      C_GREEN),
        (r"\log_b(x) = \dfrac{\ln x}{\ln b}\quad\text{(change of base)}", "Change-of-base", C_PURPLE),
    ]
    rules = VGroup(*[MathTex(r, font_size=40, color=col) for r, _, col in rule_data])
    tags  = VGroup(*[Text(t, font_size=22, color=col)    for _, t, col in rule_data])
    rules.arrange(DOWN, buff=0.5, aligned_edge=LEFT).shift(LEFT * 0.5)
    for tag, rule in zip(tags, rules):
        tag.next_to(rule, RIGHT, buff=0.4)

    for rule, tag in zip(rules, tags):
        self.play(Write(rule), FadeIn(tag, shift=LEFT * 0.2), run_time=0.85)
        self.wait(0.2)

    box = SurroundingRectangle(rules[0], color=C_ORANGE, buff=0.12, corner_radius=0.1)
    demo = MathTex(
        r"\log_{10}(2\times5)=\log_{10}2+\log_{10}5\approx0.301+0.699=1",
        font_size=28, color=C_LIGHT,
    ).next_to(rules[-1], DOWN, buff=0.45)
    self.play(Create(box))
    self.play(Write(demo), run_time=1.5)
    self.wait(2.5)
    self.play(FadeOut(VGroup(title, rules, tags, box, demo)))


def build_s05(self):
    title = make_section_title("Skewed Data  ->  Log Transform").to_edge(UP, buff=0.25)
    self.play(FadeIn(title))

    np.random.seed(42)
    raw = np.sort(np.concatenate([
        np.random.exponential(scale=5,  size=120),
        np.random.exponential(scale=50, size=10),
    ]))
    log_raw = np.log10(raw + 1)

    def histogram(data, x_range, n_bins, ax_kw, label_str, color, pos):
        ax = Axes(x_range=x_range, y_range=[0, 1.15], **ax_kw,
                  axis_config={"color": C_LIGHT}).shift(pos)
        counts, edges = np.histogram(data, bins=n_bins, range=(x_range[0], x_range[1]))
        counts = counts / max(counts)
        bars = VGroup()
        for cnt, lo, hi in zip(counts, edges[:-1], edges[1:]):
            if cnt == 0:
                continue
            bl, tr = ax.c2p(lo, 0), ax.c2p(hi, cnt)
            r = Rectangle(
                width=abs(tr[0]-bl[0]), height=abs(tr[1]-bl[1]),
                fill_color=color, fill_opacity=0.78,
                stroke_width=0.4, stroke_color=WHITE,
            ).move_to((bl + tr) / 2)
            bars.add(r)
        lbl = Text(label_str, font_size=20, color=color).next_to(ax, UP, buff=0.12)
        return VGroup(ax, bars, lbl)

    raw_h = histogram(raw,     [0, 160, 40], 20,
                      dict(x_length=5.5, y_length=3.2),
                      "Raw data  (right-skewed)",    C_RED,   LEFT*3.4+DOWN*0.5)
    log_h = histogram(log_raw, [0, 2.5, 0.5], 20,
                      dict(x_length=5.5, y_length=3.2),
                      "After log10  (near-normal)", C_GREEN, RIGHT*3.4+DOWN*0.5)

    self.play(FadeIn(raw_h[0]))
    self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in raw_h[1]], lag_ratio=0.04),
              Write(raw_h[2]))
    self.wait(0.6)

    arrow   = Arrow(raw_h.get_right(), log_h.get_left(), color=C_YELLOW, stroke_width=4)
    log_lbl = MathTex(r"x' = \log_{10}(x+1)", font_size=28, color=C_YELLOW).next_to(arrow, UP, buff=0.12)
    self.play(GrowArrow(arrow), Write(log_lbl))

    self.play(FadeIn(log_h[0]))
    self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in log_h[1]], lag_ratio=0.04),
              Write(log_h[2]))
    self.wait(0.8)

    box = make_info_box(
        "Log compresses large values & spreads small ones  ->  symmetry emerges!"
    ).to_edge(DOWN, buff=0.2)
    self.play(FadeIn(box))
    self.wait(3)
    self.play(FadeOut(VGroup(title, raw_h, log_h, arrow, log_lbl, box)))


def build_s06(self):
    title = make_section_title("Watch Values Transform Point-by-Point").to_edge(UP, buff=0.25)
    self.play(FadeIn(title))

    raw_line = NumberLine(x_range=[0, 1000, 100], length=11,
                           include_numbers=True, font_size=16,
                           color=C_LIGHT).shift(UP * 1.3)
    log_line = NumberLine(x_range=[0, 3, 0.5], length=11,
                           include_numbers=True, font_size=16,
                           color=C_LIGHT).shift(DOWN * 1.6)

    raw_lbl = Text("Original scale", font_size=22, color=C_RED  ).next_to(raw_line, LEFT, buff=0.15)
    log_lbl = Text("log10 scale",    font_size=22, color=C_GREEN).next_to(log_line, LEFT, buff=0.15)
    self.play(Create(raw_line), Write(raw_lbl), Create(log_line), Write(log_lbl))

    values = [1, 10, 100, 500, 1000]
    colors  = [C_YELLOW, C_ORANGE, C_BLUE, C_PURPLE, C_TEAL]

    raw_dots, log_dots, raw_lbls, log_lbls = VGroup(), VGroup(), VGroup(), VGroup()
    for v, col in zip(values, colors):
        rd = Dot(raw_line.n2p(v), color=col, radius=0.13)
        lv = np.log10(v)
        ld = Dot(log_line.n2p(lv), color=col, radius=0.13)
        rl = MathTex(str(v),      font_size=22, color=col).next_to(rd, UP,   buff=0.14)
        ll = MathTex(f"{lv:.1f}", font_size=22, color=col).next_to(ld, DOWN, buff=0.14)
        raw_dots.add(rd); log_dots.add(ld)
        raw_lbls.add(rl); log_lbls.add(ll)

    for rd, rl in zip(raw_dots, raw_lbls):
        self.play(FadeIn(rd), Write(rl), run_time=0.35)
    self.wait(0.5)

    for rd, ld, ll, col in zip(raw_dots, log_dots, log_lbls, colors):
        ghost = rd.copy()
        path  = ArcBetweenPoints(rd.get_center(), ld.get_center(), angle=-TAU / 4, color=col)
        self.play(MoveAlongPath(ghost, path), FadeIn(ld), Write(ll), run_time=0.65)
        self.remove(ghost)

    brace_r   = BraceBetweenPoints(raw_line.n2p(100), raw_line.n2p(1000), UP,   color=C_YELLOW)
    brace_r_l = brace_r.get_text("900 units apart", font_size=20)
    brace_l   = BraceBetweenPoints(log_line.n2p(2),  log_line.n2p(3),    DOWN, color=C_YELLOW)
    brace_l_l = brace_l.get_text("1 unit apart", font_size=20)

    self.play(Create(brace_r), Write(brace_r_l))
    self.play(Create(brace_l), Write(brace_l_l))
    self.wait(2.5)
    self.play(FadeOut(VGroup(title, raw_line, log_line, raw_lbl, log_lbl,
                              raw_dots, log_dots, raw_lbls, log_lbls,
                              brace_r, brace_r_l, brace_l, brace_l_l)))


def build_s07(self):
    title = make_section_title("Multiplicative  ->  Additive").to_edge(UP, buff=0.3)
    self.play(FadeIn(title))

    rows = [["0","100","2.000"],["1","200","2.301"],
            ["2","400","2.602"],["3","800","2.903"],["4","1600","3.204"]]
    tbl = Table(
        rows,
        col_labels=[Text(h, font_size=22, color=C_YELLOW)
                    for h in ["Year", "Value", "log10(Value)"]],
        include_outer_lines=True,
        line_config={"stroke_width": 1, "color": GREY},
        element_to_mobject=lambda s: Text(s, font_size=22, color=C_LIGHT),
    ).scale(0.72).shift(LEFT * 2.5 + DOWN * 0.3)
    self.play(FadeIn(tbl))
    self.wait(0.5)

    rb = Brace(tbl.get_columns()[1], RIGHT, color=C_RED)
    rt = Text("x2 each year",    font_size=22, color=C_RED  ).next_to(rb, RIGHT)
    db = Brace(tbl.get_columns()[2], RIGHT, color=C_GREEN)
    dt = Text("+0.301 each year", font_size=22, color=C_GREEN).next_to(db, RIGHT)

    self.play(GrowFromCenter(rb), Write(rt))
    self.play(GrowFromCenter(db), Write(dt))

    reminder = MathTex(r"\log(x \cdot 2) = \log(x) + \log(2)", font_size=34, color=C_ORANGE)
    reminder.to_edge(DOWN, buff=0.45)
    self.play(Write(reminder))
    self.wait(1.5)
    self.play(FadeOut(VGroup(tbl, rb, rt, db, dt, reminder)))

    ax1 = Axes(x_range=[0,4.5,1], y_range=[0,2000,400],   x_length=5, y_length=3.4,
               axis_config={"color": C_LIGHT}).shift(LEFT*3.1+DOWN*0.4)
    ax2 = Axes(x_range=[0,4.5,1], y_range=[1.8,3.35,0.4], x_length=5, y_length=3.4,
               axis_config={"color": C_LIGHT}).shift(RIGHT*3.1+DOWN*0.4)

    c1 = ax1.plot(lambda x: 100*2**x,               color=C_RED,   stroke_width=3)
    c2 = ax2.plot(lambda x: np.log10(100*2**x),     color=C_GREEN, stroke_width=3)
    l1 = Text("Raw scale (exponential)", font_size=20, color=C_RED  ).next_to(ax1, UP, buff=0.1)
    l2 = Text("Log scale (linear!)",     font_size=20, color=C_GREEN).next_to(ax2, UP, buff=0.1)

    self.play(Create(ax1), Create(ax2), Write(l1), Write(l2))
    self.play(Create(c1), Create(c2), run_time=2)
    self.wait(2.5)
    self.play(FadeOut(VGroup(title, ax1, ax2, c1, c2, l1, l2)))


def build_s08(self):
    title = make_section_title("Variance Stabilisation").to_edge(UP, buff=0.3)
    self.play(FadeIn(title))

    np.random.seed(7)
    xs = [1, 2, 5, 10, 20, 50, 100]
    raw_pts = [(x, y)
               for x in xs
               for y in x * (1 + np.random.normal(0, 0.25, 8))]

    ax_r = Axes(x_range=[0,110,20], y_range=[0,130,20], x_length=5, y_length=3.5,
                axis_config={"color": C_LIGHT}).shift(LEFT*3.2+DOWN*0.4)
    ax_l = Axes(x_range=[0,2.2,0.5], y_range=[0,2.2,0.5], x_length=5, y_length=3.5,
                axis_config={"color": C_LIGHT}).shift(RIGHT*3.2+DOWN*0.4)

    dr = VGroup(*[Dot(ax_r.c2p(x, y), radius=0.06, color=C_RED,   fill_opacity=0.7)
                  for x, y in raw_pts if 0 < x < 110 and 0 < y < 130])
    dl = VGroup(*[Dot(ax_l.c2p(np.log10(x), np.log10(y)), radius=0.06, color=C_GREEN, fill_opacity=0.7)
                  for x, y in raw_pts
                  if x > 0 and y > 0
                  and 0 <= np.log10(x) <= 2.2 and 0 <= np.log10(y) <= 2.2])

    lr = Text("Heteroscedastic",     font_size=22, color=C_RED  ).next_to(ax_r, UP, buff=0.1)
    ll = Text("Stabilised variance", font_size=22, color=C_GREEN).next_to(ax_l, UP, buff=0.1)

    self.play(Create(ax_r), Write(lr))
    self.play(LaggedStart(*[FadeIn(d) for d in dr], lag_ratio=0.02))
    self.wait(0.4)

    arr     = Arrow(ax_r.get_right(), ax_l.get_left(), color=C_YELLOW, stroke_width=4)
    arr_lbl = MathTex(r"\log(\cdot)", font_size=28, color=C_YELLOW).next_to(arr, UP)
    self.play(GrowArrow(arr), Write(arr_lbl))

    self.play(Create(ax_l), Write(ll))
    self.play(LaggedStart(*[FadeIn(d) for d in dl], lag_ratio=0.02))
    self.wait(2.5)
    self.play(FadeOut(VGroup(title, ax_r, ax_l, dr, dl, lr, ll, arr, arr_lbl)))


def build_s09(self):
    title = make_section_title("Comparing Bases: ln,  log10,  log2").to_edge(UP, buff=0.3)
    self.play(FadeIn(title))

    axes = Axes(
        x_range=[0.01, 20, 4], y_range=[-2, 4.5, 1],
        x_length=9, y_length=5,
        axis_config={"color": C_LIGHT, "include_tip": True},
    ).shift(DOWN * 0.4)

    funcs = [
        (np.log,   "ln(x)    - natural log",  C_ORANGE),
        (np.log10, "log10(x) - common log",   C_BLUE),
        (np.log2,  "log2(x)  - binary log",   C_GREEN),
    ]
    curves  = VGroup()
    legends = VGroup()
    for fn, name, col in funcs:
        crv = axes.plot(fn, x_range=[0.05, 20], color=col, stroke_width=3)
        leg = VGroup(
            Line(ORIGIN, RIGHT*0.5, color=col, stroke_width=3),
            Text(name, font_size=22, color=col),
        ).arrange(RIGHT, buff=0.2)
        curves.add(crv)
        legends.add(leg)

    legends.arrange(DOWN, buff=0.25, aligned_edge=LEFT).to_corner(UR).shift(LEFT*0.3+DOWN*0.5)

    self.play(Create(axes))
    for crv, leg in zip(curves, legends):
        self.play(Create(crv, run_time=1.2), FadeIn(leg))
    self.wait(0.4)

    box = make_info_box(
        "All log bases have the same shape - just scaled by a constant  (change-of-base).",
        color=C_TEAL,
    ).to_edge(DOWN, buff=0.2)
    self.play(FadeIn(box))
    self.wait(2.5)
    self.play(FadeOut(VGroup(title, axes, curves, legends, box)))


def build_s10(self):
    title = make_section_title("Caveats & When NOT to Use It", color=C_RED).to_edge(UP, buff=0.3)
    self.play(FadeIn(title))

    items = [
        ("WARNING  Zeros & Negatives",
         "log(0) = -inf  and  log(x) undefined for x < 0\n"
         "Fix: use log(x+1) or log(x+c) for a small constant c"),
        ("WARNING  Already-normal data",
         "If your data is symmetric & unimodal,\n"
         "log can introduce left-skew -- making things worse!"),
        ("WARNING  Interpretability cost",
         "Regression coefficients live on the log scale.\n"
         "Back-transform predictions: y_hat = 10^(y_hat_log)"),
        ("WARNING  Negative differences",
         "Differences and residuals can be negative.\n"
         "Log-transform raw values, never differences."),
    ]
    boxes = VGroup()
    for head, body in items:
        ht = Text(head, font_size=23, color=C_RED,   weight=BOLD)
        bt = Text(body, font_size=20, color=C_LIGHT, line_spacing=1.3)
        bt.next_to(ht, DOWN, buff=0.12, aligned_edge=LEFT)
        grp  = VGroup(ht, bt)
        rect = SurroundingRectangle(grp, color=C_RED, buff=0.2, corner_radius=0.15,
                                     fill_color=C_DARK, fill_opacity=0.55)
        boxes.add(VGroup(rect, ht, bt))

    boxes.arrange_in_grid(rows=2, cols=2, buff=0.4).shift(DOWN * 0.3)
    for box in boxes:
        self.play(FadeIn(box, scale=0.92), run_time=0.65)
        self.wait(0.25)

    self.wait(2)
    self.play(FadeOut(VGroup(title, boxes)))


def build_s11(self):
    title = make_section_title("Real-World Uses of Log Transform").to_edge(UP, buff=0.3)
    self.play(FadeIn(title))

    data = [
        ("Income & Wealth",          C_YELLOW, "Incomes span $10k-$100B+. Log makes\ndistribution near-normal for modeling."),
        ("Richter Scale",             C_ORANGE, "Each +1 = x10 in ground motion.\nLog turns orders of magnitude into steps."),
        ("Sound (Decibels)",          C_GREEN,  "dB = 10 x log10(I/I0). Hearing spans\n12 orders of magnitude."),
        ("Gene Expression",           C_BLUE,   "log2 fold-change is standard: x2 and /2\nbecome +1 and -1 -- symmetric."),
        ("Stock Prices",              C_PURPLE, "Returns are log-normal. Log returns\nare additive over time."),
        ("Web Traffic / Zipf's Law",  C_TEAL,   "Power-law data: log-log plot\nreveals a straight line."),
    ]
    examples = VGroup()
    for icon_text, col, body in data:
        h    = Text(icon_text, font_size=24, color=col, weight=BOLD)
        b    = Text(body, font_size=19, color=C_LIGHT, line_spacing=1.3)
        b.next_to(h, DOWN, buff=0.08, aligned_edge=LEFT)
        grp  = VGroup(h, b)
        rect = SurroundingRectangle(grp, buff=0.18, corner_radius=0.1,
                                     stroke_width=1, color=GREY_B,
                                     fill_color="#1e2d3a", fill_opacity=0.55)
        examples.add(VGroup(rect, h, b))

    examples.arrange_in_grid(rows=3, cols=2, buff=0.45).shift(DOWN * 0.2)
    for ex in examples:
        self.play(FadeIn(ex, scale=0.93), run_time=0.45)
    self.wait(3)
    self.play(FadeOut(VGroup(title, examples)))


def build_s12(self):
    title = Text("Log Transform -- Summary Cheat Sheet",
                 font_size=38, color=C_YELLOW, weight=BOLD).to_edge(UP, buff=0.3)
    self.play(Write(title))

    rows_data = [
        ("What it does",     r"x \;\mapsto\; \log(x)",              C_ORANGE, True),
        ("Compresses range", r"1,10,100,1000 \;\to\; 0,1,2,3",      C_BLUE,   True),
        ("Product -> sum",   r"\log(ab) = \log a + \log b",         C_GREEN,  True),
        ("Power rule",       r"\log(a^n) = n\log a",                C_PURPLE, True),
        ("Fixes right skew", "heavy tail -> near-normal",            C_TEAL,   False),
        ("Stabilises var",   "variance grows with mean -> constant", C_RED,    False),
        ("Watch out for",    "zeros, negatives, already-normal data",C_YELLOW, False),
    ]
    table_group = VGroup()
    for label, formula, col, use_math in rows_data:
        t1 = Text(label, font_size=22, color=col)
        t2 = (MathTex(formula, font_size=22, color=C_LIGHT)
              if use_math else Text(formula, font_size=22, color=C_LIGHT))
        t1.set_width(3.5)
        row = VGroup(t1, t2).arrange(RIGHT, buff=0.5, aligned_edge=LEFT)
        sep = Line(LEFT*5.8, RIGHT*5.8, stroke_width=0.5, color=GREY)
        table_group.add(row, sep)

    table_group.arrange(DOWN, buff=0.15, aligned_edge=LEFT)
    table_group.next_to(title, DOWN, buff=0.4)
    for item in table_group:
        self.play(FadeIn(item, shift=RIGHT*0.3), run_time=0.32)

    self.wait(2.5)
    bye = Text("Good luck transforming your data!", font_size=32, color=C_YELLOW)
    bye.to_edge(DOWN, buff=0.35)
    self.play(Write(bye))
    self.wait(2)
    self.play(FadeOut(VGroup(title, table_group, bye)))


# ---------------------------------------------------------------------------
# Standalone scene classes  (each renders a single section)
# ---------------------------------------------------------------------------

class S01_Intro(Scene):
    def construct(self): build_s01(self)

class S02_WhatIsLog(Scene):
    def construct(self): build_s02(self)

class S03_LogGraph(Scene):
    def construct(self): build_s03(self)

class S04_LogRules(Scene):
    def construct(self): build_s04(self)

class S05_DistributionTransform(Scene):
    def construct(self): build_s05(self)

class S06_PointTransform(Scene):
    def construct(self): build_s06(self)

class S07_MultiplicativeAdditive(Scene):
    def construct(self): build_s07(self)

class S08_VarianceStabilisation(Scene):
    def construct(self): build_s08(self)

class S09_BasesComparison(Scene):
    def construct(self): build_s09(self)

class S10_Caveats(Scene):
    def construct(self): build_s10(self)

class S11_RealWorld(Scene):
    def construct(self): build_s11(self)

class S12_Summary(Scene):
    def construct(self): build_s12(self)


# ---------------------------------------------------------------------------
# LogTransformFull  —  all 12 scenes as one continuous video
#
# KEY FIX: each build_sXX(self) call runs directly inside THIS scene's
# construct(), sharing its single camera/renderer naturally.
# No cross-scene instantiation or camera-swapping is needed.
# ---------------------------------------------------------------------------

class LogTransformFull(Scene):
    def construct(self):
        build_s01(self);  self.wait(0.4)
        build_s02(self);  self.wait(0.4)
        build_s03(self);  self.wait(0.4)
        build_s04(self);  self.wait(0.4)
        build_s05(self);  self.wait(0.4)
        build_s06(self);  self.wait(0.4)
        build_s07(self);  self.wait(0.4)
        build_s08(self);  self.wait(0.4)
        build_s09(self);  self.wait(0.4)
        build_s10(self);  self.wait(0.4)
        build_s11(self);  self.wait(0.4)
        build_s12(self)