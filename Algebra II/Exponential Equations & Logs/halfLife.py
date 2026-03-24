from manim import *
import numpy as np

# ─── Colour palette ────────────────────────────────────────────────────────────
BG       = "#0D1117"
ACCENT1  = "#58A6FF"   # blue
ACCENT2  = "#3FB950"   # green
ACCENT3  = "#F78166"   # red/orange
ACCENT4  = "#D2A8FF"   # purple
WARM     = "#FFA657"   # orange
WHITE_   = "#E6EDF3"
GREY_    = "#8B949E"

config.background_color = BG


# ══════════════════════════════════════════════════════════════════════════════
# 1. TITLE SCENE
# ══════════════════════════════════════════════════════════════════════════════
class TitleScene(Scene):
    def construct(self):
        title = Text("Half-Life &\nExponential Decay",
                     font_size=64, color=WHITE_, weight=BOLD,
                     line_spacing=1.1).move_to(ORIGIN)

        subtitle = Text("Understanding radioactive decay through mathematics",
                        font_size=26, color=GREY_).next_to(title, DOWN, buff=0.6)

        atom_ring = Circle(radius=1.4, color=ACCENT1, stroke_width=3)
        nucleus   = Dot(color=ACCENT3, radius=0.25)
        electrons = VGroup(*[
            Dot(color=ACCENT2, radius=0.10).move_to(
                atom_ring.point_at_angle(angle)
            )
            for angle in np.linspace(0, TAU, 6, endpoint=False)
        ])
        atom = VGroup(atom_ring, nucleus, electrons).scale(0.55).to_corner(UL, buff=0.4)

        # animated appearance
        self.play(Write(title, run_time=1.8))
        self.play(FadeIn(subtitle, shift=UP*0.3), run_time=0.8)
        self.play(Create(atom_ring), FadeIn(nucleus, electrons), run_time=1.2)
        self.play(Rotate(electrons, angle=TAU, about_point=ORIGIN,
                         rate_func=linear, run_time=2))
        self.wait(0.5)
        self.play(FadeOut(VGroup(title, subtitle, atom)))


# ══════════════════════════════════════════════════════════════════════════════
# 2. EXPONENTIAL DECAY FORMULA
# ══════════════════════════════════════════════════════════════════════════════
class ExponentialFormula(Scene):
    def construct(self):
        header = Text("The Decay Equation", font_size=40,
                      color=ACCENT1, weight=BOLD).to_edge(UP, buff=0.5)
        self.play(Write(header))

        # build formula piece by piece
        parts = [
            MathTex(r"N(t)", color=ACCENT2, font_size=64),
            MathTex(r"=",    color=WHITE_,  font_size=64),
            MathTex(r"N_0",  color=WARM,    font_size=64),
            MathTex(r"\cdot e^{-\lambda t}", color=ACCENT3, font_size=64),
        ]
        formula = VGroup(*parts).arrange(RIGHT, buff=0.15).move_to(ORIGIN + UP*0.5)

        labels = VGroup(
            Text("atoms at time t", font_size=20, color=ACCENT2),
            Text("initial count",   font_size=20, color=WARM),
            Text("decay constant",  font_size=20, color=ACCENT3),
        )

        arrows = VGroup(
            Arrow(labels[0].get_top(), parts[0].get_bottom(), color=ACCENT2,
                  buff=0.1, stroke_width=2),
            Arrow(labels[1].get_top(), parts[2].get_bottom(), color=WARM,
                  buff=0.1, stroke_width=2),
            Arrow(labels[2].get_top(), parts[3].get_bottom(), color=ACCENT3,
                  buff=0.1, stroke_width=2),
        )

        labels[0].next_to(parts[0], DOWN + LEFT * 2, buff=1.0)
        labels[1].next_to(parts[2], DOWN, buff=1.0)
        labels[2].next_to(parts[3], DOWN + RIGHT * 2, buff=1.0)

        for p in parts:
            self.play(Write(p), run_time=0.6)
        self.wait(0.4)
        for lbl, arr in zip(labels, arrows):
            self.play(FadeIn(lbl, shift=DOWN*0.2), GrowArrow(arr), run_time=0.5)
        self.wait(1.5)
        self.play(FadeOut(Group(*self.mobjects)))


# ══════════════════════════════════════════════════════════════════════════════
# 3. HALF-LIFE DERIVATION
# ══════════════════════════════════════════════════════════════════════════════
class HalfLifeDefinition(Scene):
    def construct(self):
        header = Text("Deriving the Half-Life Formula",
                      font_size=38, color=ACCENT1, weight=BOLD).to_edge(UP, buff=0.4)
        self.play(Write(header))

        steps = [
            (r"N(T_{1/2}) = \tfrac{1}{2} N_0",
             "After one half-life, exactly half remains"),
            (r"\tfrac{1}{2}N_0 = N_0 \cdot e^{-\lambda T_{1/2}}",
             "Substitute into decay equation"),
            (r"\tfrac{1}{2} = e^{-\lambda T_{1/2}}",
             "Divide both sides by N₀"),
            (r"\ln\!\left(\tfrac{1}{2}\right) = -\lambda T_{1/2}",
             "Take natural log of both sides"),
            (r"T_{1/2} = \frac{\ln 2}{\lambda}",
             "Solve for T½  (the key result!)"),
        ]

        step_colors = [ACCENT2, ACCENT2, ACCENT1, ACCENT1, ACCENT4]
        prev = header
        for i, (eq, desc) in enumerate(steps):
            color = step_colors[i % len(step_colors)]
            mobj = MathTex(eq, color=color, font_size=48)
            mobj.next_to(prev, DOWN, buff=0.45)
            hint = Text(desc, font_size=18, color=GREY_).next_to(mobj, RIGHT, buff=0.4)
            self.play(Write(mobj), FadeIn(hint, shift=RIGHT*0.2), run_time=0.9)
            prev = mobj

        # highlight final result
        box = SurroundingRectangle(prev, color=ACCENT3, buff=0.15, stroke_width=3)
        self.play(Create(box), run_time=0.7)
        self.wait(2)
        self.play(FadeOut(Group(*self.mobjects)))


# ══════════════════════════════════════════════════════════════════════════════
# 4. ANIMATED DECAY CURVE
# ══════════════════════════════════════════════════════════════════════════════
class DecayCurveScene(Scene):
    def construct(self):
        header = Text("Decay Curve with Half-Life Markers",
                      font_size=34, color=ACCENT1, weight=BOLD).to_edge(UP, buff=0.3)
        self.play(Write(header))

        # axes
        ax = Axes(
            x_range=[0, 5.2, 1],
            y_range=[0, 1.1, 0.25],
            x_length=9,
            y_length=5,
            axis_config={"color": WHITE_, "stroke_width": 2,
                         "include_tip": True, "tip_length": 0.2},
            x_axis_config={"numbers_to_include": list(range(0, 6)),
                           "label_direction": DOWN},
            y_axis_config={"numbers_to_include": [0, 0.25, 0.5, 0.75, 1.0]},
        ).shift(DOWN*0.3)

        x_lbl = MathTex(r"t / T_{1/2}", color=WHITE_, font_size=28)\
                    .next_to(ax.x_axis.get_right(), DOWN+RIGHT, buff=0.2)
        y_lbl = MathTex(r"N(t)/N_0",   color=WHITE_, font_size=28)\
                    .next_to(ax.y_axis.get_top(), LEFT, buff=0.1)

        self.play(Create(ax), Write(x_lbl), Write(y_lbl))

        # curve  N/N₀ = 2^(-t/T½) = e^(-ln2·t)
        lam = np.log(2)
        curve = ax.plot(lambda t: np.exp(-lam * t),
                        x_range=[0, 5], color=ACCENT1, stroke_width=3)
        self.play(Create(curve, run_time=2.5))

        # half-life dashed markers
        marker_group = VGroup()
        dot_group    = VGroup()
        for n in range(1, 6):
            x_val = n
            y_val = 0.5 ** n
            h_dash = DashedLine(ax.c2p(0, y_val), ax.c2p(x_val, y_val),
                                color=ACCENT3, stroke_width=1.5, dash_length=0.12)
            v_dash = DashedLine(ax.c2p(x_val, 0), ax.c2p(x_val, y_val),
                                color=ACCENT3, stroke_width=1.5, dash_length=0.12)
            dot    = Dot(ax.c2p(x_val, y_val), color=ACCENT3, radius=0.09)
            frac   = MathTex(rf"\tfrac{{1}}{{{2**n}}}",
                             color=WARM, font_size=22)\
                        .next_to(ax.c2p(0, y_val), LEFT, buff=0.1)
            marker_group.add(h_dash, v_dash, frac)
            dot_group.add(dot)

        self.play(Create(marker_group), run_time=1.5)
        self.play(FadeIn(dot_group))

        note = Text("Each half-life halves the remaining quantity",
                    font_size=21, color=GREY_).to_edge(DOWN, buff=0.25)
        self.play(FadeIn(note))
        self.wait(8)
        self.play(FadeOut(Group(*self.mobjects)))


# ══════════════════════════════════════════════════════════════════════════════
# 5. SUCCESSIVE HALVINGS BAR
# ══════════════════════════════════════════════════════════════════════════════
class MultipleHalfLives(Scene):
    def construct(self):
        header = Text("Successive Halvings", font_size=38,
                      color=ACCENT1, weight=BOLD).to_edge(UP, buff=0.4)
        self.play(Write(header))

        n_steps = 6
        colors   = color_gradient([ACCENT1, ACCENT2, ACCENT3, WARM, ACCENT4], n_steps)
        bar_w    = 0.9
        max_h    = 5.0
        bars     = VGroup()
        lbls     = VGroup()
        pct_lbls = VGroup()

        for i in range(n_steps):
            frac   = 0.5 ** i
            height = frac * max_h
            bar    = Rectangle(width=bar_w, height=height, fill_color=colors[i],
                               fill_opacity=0.85, stroke_width=1.5,
                               stroke_color=WHITE_)
            bar.move_to(np.array([-3.0 + i*1.3, -2.5 + height/2, 0]))
            period_lbl = MathTex(rf"T_{{1/2}} \times {i}", color=WHITE_,
                                 font_size=20).next_to(bar, DOWN, buff=0.15)
            pct_val    = f"{frac*100:.1f}%"
            pct_lbl    = Text(pct_val, font_size=19, color=WHITE_)\
                             .next_to(bar, UP, buff=0.08)
            bars.add(bar)
            lbls.add(period_lbl)
            pct_lbls.add(pct_lbl)

        for bar, lbl, pct in zip(bars, lbls, pct_lbls):
            self.play(GrowFromEdge(bar, DOWN),
                      FadeIn(lbl), FadeIn(pct), run_time=0.55)

        note = Text("After 10 half-lives → less than 0.1% remains",
                    font_size=22, color=GREY_).to_edge(DOWN, buff=0.25)
        self.play(FadeIn(note))
        self.wait(8)
        self.play(FadeOut(Group(*self.mobjects)))


# ══════════════════════════════════════════════════════════════════════════════
# 6. COMPARE DIFFERENT HALF-LIVES
# ══════════════════════════════════════════════════════════════════════════════
class CompareHalfLives(Scene):
    def construct(self):
        header = Text("Effect of Different Half-Lives",
                      font_size=34, color=ACCENT1, weight=BOLD).to_edge(UP, buff=0.3)
        self.play(Write(header))

        ax = Axes(
            x_range=[0, 5.5, 1],
            y_range=[0, 1.15, 0.25],
            x_length=9.5,
            y_length=5.2,
            axis_config={"color": WHITE_, "stroke_width": 2, "include_tip": True,
                         "tip_length": 0.2},
            x_axis_config={"numbers_to_include": list(range(0, 6))},
            y_axis_config={"numbers_to_include": [0, 0.25, 0.5, 0.75, 1.0]},
        ).shift(DOWN*0.35)

        x_lbl = Text("Time (arbitrary units)", color=WHITE_, font_size=22)\
                    .next_to(ax.x_axis.get_right(), DOWN+RIGHT, buff=0.15)
        y_lbl = MathTex(r"N(t)/N_0", color=WHITE_, font_size=26)\
                    .next_to(ax.y_axis.get_top(), LEFT, buff=0.1)
        self.play(Create(ax), Write(x_lbl), Write(y_lbl))

        substances = [
            ("Short  T½ = 0.5",  0.5,  ACCENT3),
            ("Medium T½ = 1.0",  1.0,  ACCENT2),
            ("Long   T½ = 2.5",  2.5,  ACCENT4),
        ]

        legend_items = VGroup()
        for label, t_half, col in substances:
            lam   = np.log(2) / t_half
            curve = ax.plot(lambda t, l=lam: np.exp(-l * t),
                            x_range=[0, 5.2], color=col, stroke_width=3)
            self.play(Create(curve, run_time=1.5))

            dot  = Dot(color=col, radius=0.1)
            txt  = Text(label, font_size=20, color=col)
            row  = VGroup(dot, txt).arrange(RIGHT, buff=0.2)
            legend_items.add(row)

        legend_box = VGroup(*legend_items).arrange(DOWN, aligned_edge=LEFT, buff=0.2)\
                         .to_corner(UR, buff=0.5)
        bg = SurroundingRectangle(legend_box, color=GREY_, fill_color=BG,
                                  fill_opacity=0.7, buff=0.15, stroke_width=1)
        self.play(FadeIn(bg), FadeIn(legend_box))

        conclusion = Text("Larger T½  →  slower decay  →  longer persistence",
                          font_size=22, color=GREY_).to_edge(DOWN, buff=0.2)
        self.play(FadeIn(conclusion))
        self.wait(5)
        self.play(FadeOut(Group(*self.mobjects)))


# ══════════════════════════════════════════════════════════════════════════════
# 7. REAL-WORLD EXAMPLES
# ══════════════════════════════════════════════════════════════════════════════
class RealWorldExamples(Scene):
    def construct(self):
        header = Text("Real-World Examples", font_size=40,
                      color=ACCENT1, weight=BOLD).to_edge(UP, buff=0.4)
        self.play(Write(header))

        data = [
            ("Carbon-14",   r"^{14}\text{C}",  "5,730 years",
             "Archaeological dating", ACCENT2),
            ("Iodine-131",  r"^{131}\text{I}",  "8 days",
             "Medical imaging / thyroid", ACCENT3),
            ("Uranium-238", r"^{238}\text{U}", "4.47 billion years",
             "Geological age of Earth", ACCENT4),
        ]

        cards = VGroup()
        for name, sym, half, use, col in data:
            rect  = RoundedRectangle(corner_radius=0.2, width=3.4, height=2.8,
                                     fill_color=col, fill_opacity=0.15,
                                     stroke_color=col, stroke_width=2)
            title = Text(name,  font_size=24, color=col, weight=BOLD)
            sym_  = MathTex(sym, font_size=40, color=WHITE_)
            t_lbl = VGroup(
                Text("T½ =", font_size=18, color=GREY_),
                Text(half,   font_size=18, color=WHITE_),
            ).arrange(RIGHT, buff=0.15)
            use_  = Text(use, font_size=16, color=GREY_, slant=ITALIC)

            content = VGroup(title, sym_, t_lbl, use_)\
                          .arrange(DOWN, buff=0.2, center=True)
            content.move_to(rect.get_center())
            cards.add(VGroup(rect, content))

        cards.arrange(RIGHT, buff=0.35).shift(DOWN*0.2)

        for card in cards:
            self.play(FadeIn(card, scale=0.85), run_time=0.7)
        self.wait(0.5)

        note = Text("Half-life spans 8 orders of magnitude — same physics, different scales!",
                    font_size=20, color=GREY_).to_edge(DOWN, buff=0.2)
        self.play(FadeIn(note))
        self.wait(2.5)
        self.play(FadeOut(Group(*self.mobjects)))


# ══════════════════════════════════════════════════════════════════════════════
# 8. OUTRO / SUMMARY
# ══════════════════════════════════════════════════════════════════════════════
class OutroScene(Scene):
    def construct(self):
        key_eq = MathTex(
            r"T_{1/2} = \frac{\ln 2}{\lambda}",
            font_size=80, color=ACCENT1
        ).move_to(ORIGIN + UP*0.8)

        box = SurroundingRectangle(key_eq, color=ACCENT3, buff=0.3,
                                   stroke_width=3, corner_radius=0.2)

        bullets = VGroup(
            Text("N(t) = N₀·e^(−λt)   describes any exponential decay",
                 font_size=22, color=WHITE_),
            Text("The half-life T½ is fully determined by the decay constant λ",
                 font_size=22, color=WHITE_),
            Text("After n half-lives, only (½)ⁿ of the original remains",
                 font_size=22, color=WHITE_),
            Text("Half-life is scale-independent — from nanoseconds to eons",
                 font_size=22, color=WHITE_),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28).next_to(key_eq, DOWN, buff=0.6)

        self.play(Write(key_eq), Create(box), run_time=1.5)
        for b in bullets:
            self.play(FadeIn(b, shift=RIGHT*0.3), run_time=0.6)
        self.wait(2.5)
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=1.5)


# ══════════════════════════════════════════════════════════════════════════════
# COMBINED SCENE — renders all scenes sequentially
# ══════════════════════════════════════════════════════════════════════════════
class HalfLifeAll(Scene):
    """Single entry point that plays every scene back-to-back."""

    def construct(self):
        scenes = [
            TitleScene,
            ExponentialFormula,
            HalfLifeDefinition,
            DecayCurveScene,
            MultipleHalfLives,
            CompareHalfLives,
            RealWorldExamples,
            OutroScene,
        ]
        for SceneClass in scenes:
            # instantiate and run each scene's construct() inside this scene
            s = SceneClass()
            s.renderer = self.renderer
            s.camera   = self.camera
            s.construct()
            self.wait(0.4)   # brief pause between scenes