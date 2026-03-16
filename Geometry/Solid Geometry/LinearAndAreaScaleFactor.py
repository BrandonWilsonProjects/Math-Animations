from manim import *


class ScaleFactorScene(Scene):
    def construct(self):
        # ── Title ──────────────────────────────────────────────────────────────
        title = Text("Linear Scale Factor vs Area Scale Factor", font_size=36)
        subtitle = Text("If lengths scale by k, area scales by k²", font_size=24,
                        color=YELLOW)
        subtitle.next_to(title, DOWN, buff=0.3)
        title_group = VGroup(title, subtitle)
        title_group.to_edge(UP)

        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle, shift=UP * 0.3))
        self.wait(0.5)

        # ── Helper to make a labelled square ──────────────────────────────────
        def make_square(side, color, label_text, show_area=True):
            sq = Square(side_length=side, color=color, fill_color=color,
                        fill_opacity=0.25)
            side_label = MathTex(f"k={label_text}", font_size=28, color=color)
            side_label.next_to(sq, LEFT, buff=0.15)
            area_val = f"{label_text}^2" if label_text != "1" else "1"
            area_label = MathTex(rf"\text{{Area}}={area_val}", font_size=26,
                                 color=color)
            area_label.next_to(sq, DOWN, buff=0.2)
            return VGroup(sq, side_label, area_label)

        # ── Show three squares with k = 1, 2, 3 ──────────────────────────────
        unit = 1.2          # side length for k=1
        colors = [BLUE, GREEN, RED]
        k_vals = [1, 2, 3]
        labels = ["1", "2", "3"]

        squares = VGroup(*[
            make_square(unit * k, c, lbl)
            for k, c, lbl in zip(k_vals, colors, labels)
        ])

        # Layout: spread horizontally, centred vertically
        squares.arrange(RIGHT, buff=0.9)
        squares.move_to(ORIGIN + DOWN * 0.6)

        self.play(FadeIn(squares[0], scale=0.5))
        self.wait(0.3)

        for i in range(1, 3):
            self.play(TransformFromCopy(squares[0][0], squares[i][0]),
                      FadeIn(squares[i][1]), FadeIn(squares[i][2]),
                      run_time=1)
            self.wait(0.3)

        self.wait(0.8)

        # ── Highlight: side doubles → area quadruples ─────────────────────────
        arrow_side = Arrow(squares[0][0].get_right(),
                           squares[1][0].get_left(),
                           color=WHITE, buff=0.1)
        arrow_side_lbl = MathTex(r"\times 2\text{ (side)}", font_size=24,
                                 color=WHITE)
        arrow_side_lbl.next_to(arrow_side, UP, buff=0.1)

        arrow_area = Arrow(squares[0][2].get_right(),
                           squares[1][2].get_left(),
                           color=YELLOW, buff=0.1)
        arrow_area_lbl = MathTex(r"\times 4\text{ (area)}", font_size=24,
                                 color=YELLOW)
        arrow_area_lbl.next_to(arrow_area, DOWN, buff=0.1)

        self.play(GrowArrow(arrow_side.shift(UP * 0.3)), Write(arrow_side_lbl.shift(UP * 0.3)))    
        self.wait(5)

        self.play(*[FadeOut(m) for m in
                   [arrow_side, arrow_side_lbl, arrow_area, arrow_area_lbl]])

        # ── Clear squares and show the graph ──────────────────────────────────
        self.play(FadeOut(squares), FadeOut(subtitle))
        self.wait(0.3)

        # ── Axes ──────────────────────────────────────────────────────────────
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 16, 4],
            x_length=5.5,
            y_length=4,
            axis_config={"include_numbers": True, "font_size": 22},
            tips=True,
        )
        axes_labels = axes.get_axis_labels(
            x_label=MathTex("k", font_size=30),
            y_label=MathTex("k^2", font_size=30),
        )
        axes_group = VGroup(axes, axes_labels)
        axes_group.move_to(ORIGIN + DOWN * 0.5)

        self.play(Create(axes), Write(axes_labels))

        # k² curve
        curve = axes.plot(lambda x: x**2, x_range=[0, 4], color=YELLOW,
                          stroke_width=3)
        curve_label = MathTex(r"\text{Area scale} = k^2", font_size=28,
                              color=YELLOW)
        curve_label.next_to(axes.c2p(3.2, 12), RIGHT * 4.5, buff=0.1)

        self.play(Create(curve), run_time=2)
        self.play(Write(curve_label))
        self.wait(0.5)

        # linear reference
        linear = DashedVMobject(
            axes.plot(lambda x: x, x_range=[0, 4], color=BLUE_B,
                      stroke_width=2.5),
            num_dashes=30, dashed_ratio=0.6
        )
        linear_label = MathTex(r"\text{If area} = k\;\text{(linear — wrong!)}",
                               font_size=22, color=BLUE_B)
        linear_label.next_to(axes.c2p(3.2, 3.5), RIGHT + UP * 2.7, buff=0.05)

        self.play(Create(linear), Write(linear_label), run_time=1.5)
        self.wait(1)

        # ── Dot tracer for k = 1, 2, 3 ────────────────────────────────────────
        dot = Dot(color=RED, radius=0.1)
        dot.move_to(axes.c2p(0, 0))

        k_tracker = ValueTracker(0)
        dot.add_updater(
            lambda d: d.move_to(axes.c2p(k_tracker.get_value(),
                                         k_tracker.get_value() ** 2))
        )

        coord_label = always_redraw(lambda: MathTex(
            rf"k={k_tracker.get_value():.1f},\; k^2="
            rf"{k_tracker.get_value()**2:.1f}",
            font_size=26, color=RED
        ).next_to(dot, UP * 2 + LEFT, buff=0.15))

        self.play(FadeIn(dot), FadeIn(coord_label))

        for k_target in [1, 2, 3]:
            self.play(k_tracker.animate.set_value(k_target), run_time=1.2)
            self.wait(0.6)

        self.wait(1)

        # ── Summary formula ───────────────────────────────────────────────────
        formula_box = SurroundingRectangle(
            MathTex(r"\text{Area scale factor} = (\text{Linear scale factor})^2",
                    font_size=32).to_edge(DOWN, buff=0.5),
            color=YELLOW, buff=0.2, corner_radius=0.15
        )
        formula = MathTex(
            r"\text{Area scale factor} = (\text{Linear scale factor})^2",
            font_size=32
        ).move_to(formula_box)

        self.play(Create(formula_box), Write(formula))
        self.wait(2.5)

        # ── Fade out ──────────────────────────────────────────────────────────
        self.play(*[FadeOut(m) for m in self.mobjects])
        self.wait(0.5)