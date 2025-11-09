from manim import *
import numpy as np

class MeanStdVisualization(Scene):
    def construct(self):
        # ---------- Data ----------
        np.random.seed(7)
        true_mean, true_std = 10.0, 2.0
        data = np.random.normal(loc=true_mean, scale=true_std, size=600)

        mu  = float(np.mean(data))
        sig = float(np.std(data, ddof=1))

        x_min, x_max = mu - 4*sig, mu + 4*sig
        bins = 20
        counts, edges = np.histogram(data, bins=bins, range=(x_min, x_max))
        y_max = max(counts) * 1.15

        # ---------- Axes (smaller + moved down) ----------
        axes = Axes(
            x_range=[x_min, x_max, (x_max - x_min) / 8],
            y_range=[0, y_max, max(1, int(y_max // 4))],
            x_length=7.2,   # smaller
            y_length=4.1,   # smaller
            axis_config={"include_numbers": False, "include_ticks": True, "stroke_width": 2},
            tips=True,
        ).to_edge(LEFT, buff=0.6).shift(DOWN * 0.6)  # move graph down
        self.play(Create(axes))

        # Manual tick labels
        xticks = VGroup()
        for xv in np.linspace(x_min, x_max, 9):
            lbl = Text(f"{xv:0.1f}", font_size=18)
            lbl.next_to(axes.c2p(xv, 0), DOWN, buff=0.10)
            xticks.add(lbl)

        yticks = VGroup()
        for yv in np.linspace(0, y_max, 6)[1:]:
            lbl = Text(f"{yv:0.0f}", font_size=18)
            lbl.next_to(axes.c2p(x_min, yv), LEFT, buff=0.10)
            yticks.add(lbl)

        # Axis titles adjusted to avoid overlap
        x_label = Text("Value", font_size=24).next_to(axes.x_axis.get_right(), RIGHT, buff=0.2).shift(DOWN * 0.1)
        y_label = Text("Frequency", font_size=24).next_to(axes.y_axis.get_top(), RIGHT, buff=0.15).shift(UP * 0.1)

        self.play(FadeIn(xticks), FadeIn(yticks), FadeIn(x_label), FadeIn(y_label))

        # ---------- Histogram ----------
        bars = VGroup()
        for i in range(len(edges) - 1):
            left, right = edges[i], edges[i + 1]
            h = counts[i]
            poly = Polygon(
                axes.c2p(left, 0),
                axes.c2p(left, h),
                axes.c2p(right, h),
                axes.c2p(right, 0),
            ).set_fill(TEAL_D, 0.7).set_stroke(WHITE, 1)
            bars.add(poly)
        self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.05))

        # ---------- Mean line ----------
        mean_line = Line(axes.c2p(mu, 0), axes.c2p(mu, y_max), color=YELLOW).set_stroke(width=4)
        mean_label = Text(f"Mean ≈ {mu:.2f}", font_size=26, weight=BOLD, color=YELLOW)
        # add extra spacing from the ±1σ label by shifting right
        mean_label.next_to(axes.c2p(mu, y_max), UP, buff=0.30).shift(RIGHT * 0.6)

        self.play(Create(mean_line), FadeIn(mean_label))

        # ---------- ±1σ band + brace ----------
        band = Polygon(
            axes.c2p(mu - sig, 0),
            axes.c2p(mu - sig, y_max),
            axes.c2p(mu + sig, y_max),
            axes.c2p(mu + sig, 0),
        ).set_fill(BLUE_E, 0.18).set_stroke(BLUE_E, 0)
        self.play(FadeIn(band))

        top_y = y_max * 0.88
        brace = BraceBetweenPoints(axes.c2p(mu - sig, top_y), axes.c2p(mu + sig, top_y), direction=UP)
        brace_label = Text(f"±1 standard deviation ≈ ±{sig:.2f}", font_size=24)
        # more space from mean label by increasing buff and shifting left slightly
        brace_label.next_to(brace, UP*2, buff=0.35).shift(LEFT * 0.6)

        self.play(GrowFromCenter(brace), FadeIn(brace_label))
        self.bring_to_front(mean_label, brace_label)

        # ---------- Legend ----------
        legend = VGroup(
            VGroup(Square(0.22).set_fill(TEAL_D, 0.8).set_stroke(WHITE, 1), Text("Histogram", font_size=18)).arrange(RIGHT, buff=0.25),
            VGroup(Line(ORIGIN, RIGHT*0.55, color=YELLOW).set_stroke(width=4), Text("Mean", font_size=18)).arrange(RIGHT, buff=0.25),
            VGroup(Rectangle(width=0.55, height=0.22).set_fill(BLUE_E, 0.18).set_stroke(BLUE_E, 0), Text("±1σ band", font_size=18)).arrange(RIGHT, buff=0.25),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).to_corner(UR).shift(LEFT*0.2 + DOWN*0.25)
        self.play(FadeIn(legend))

        # Title
        title = Text("Mean & Standard Deviation (Sample)", font_size=30, weight=BOLD)
        title.to_edge(UP)
        self.play(FadeIn(title))
        self.wait(2)
