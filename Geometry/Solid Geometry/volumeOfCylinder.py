from manim import *


class CylinderVolume(ThreeDScene):
    def construct(self):
        # ── Title ─────────────────────────────────────────────────────
        title    = Text("Volume of a Cylinder", font_size=44, color=BLUE)
        subtitle = Text("V = πr²h", font_size=32, color=YELLOW)
        subtitle.next_to(title, DOWN, buff=0.4)

        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle, shift=UP * 0.3))
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(subtitle))

        # ── Scene 1: Stack of coins intuition ─────────────────────────
        self.show_stacking_intuition()

        # ── Scene 2: 3-D cylinder with labelled dimensions ─────────────
        self.show_labelled_cylinder()

        # ── Scene 3: Formula derivation ───────────────────────────────
        self.show_derivation()

        # ── Scene 4: Numeric worked example ───────────────────────────
        self.show_numeric_example()

        # ── Scene 5: Effect of changing r vs h ────────────────────────
        self.show_parameter_effect()

        # ── Outro ─────────────────────────────────────────────────────
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES)
        outro = Text("V = πr²h", font_size=52, color=YELLOW)
        self.play(Write(outro))
        self.wait(2)
        self.play(FadeOut(outro))

    # ──────────────────────────────────────────────────────────────────
    def show_stacking_intuition(self):
        """Show that a cylinder = a stack of thin circular discs."""
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES)

        header = Text("Key Idea: Stack of Circles", font_size=34, color=BLUE_B).to_edge(UP)
        self.play(FadeIn(header))

        idea = MathTex(
            r"\text{Cylinder} = \text{many thin circular discs stacked up}",
            font_size=28, color=WHITE,
        ).next_to(header, DOWN, buff=0.4)
        self.play(Write(idea), run_time=1.3)
        self.wait(0.5)

        # Draw discs one by one, building up the cylinder
        n_discs   = 8
        disc_h    = 0.28
        radius    = 1.2
        base_y    = -1.8

        discs = VGroup()
        for i in range(n_discs):
            disc = Ellipse(width=radius * 2, height=radius * 0.55,
                           fill_color=BLUE, fill_opacity=0.55,
                           stroke_color=WHITE, stroke_width=1.2)
            disc.move_to(UP * (base_y + i * disc_h))
            discs.add(disc)

        self.play(
            LaggedStart(*[FadeIn(d, shift=UP * 0.1) for d in discs],
                        lag_ratio=0.12),
            run_time=2.5,
        )
        self.wait(0.5)

        # Label one disc
        brace = Brace(discs[-1], direction=RIGHT, color=YELLOW)
        brace_lbl = brace.get_tex(r"\delta h").scale(0.7)
        self.play(FadeIn(brace), Write(brace_lbl))
        self.wait(0.4)

        disc_area_lbl = MathTex(r"\text{Each disc area} = \pi r^2",
                                 font_size=28, color=GREEN)
        disc_area_lbl.next_to(discs, LEFT, buff=0.6)
        self.play(Write(disc_area_lbl))
        self.wait(1.2)

        total_lbl = MathTex(r"\text{Total volume} = \pi r^2 \times h",
                             font_size=30, color=YELLOW)
        total_lbl.to_edge(DOWN, buff=0.6)
        self.play(Write(total_lbl))
        self.wait(2)

        self.play(FadeOut(VGroup(header, idea, discs, brace, brace_lbl,
                                  disc_area_lbl, total_lbl)))

    # ──────────────────────────────────────────────────────────────────
    def show_labelled_cylinder(self):
        """Render a 3-D cylinder and annotate r and h."""
        self.move_camera(phi=65 * DEGREES, theta=-45 * DEGREES, run_time=1.5)

        header = Text("The Dimensions", font_size=34, color=BLUE_B)
        header.to_corner(UL)
        self.add_fixed_in_frame_mobjects(header)
        self.play(FadeIn(header))

        cyl = Cylinder(radius=1.2, height=2.8,
                       fill_color=BLUE, fill_opacity=0.4,
                       stroke_color=WHITE, stroke_width=1)
        self.play(Create(cyl), run_time=1.8)
        self.wait(0.5)

        # Radius arrow (fixed in frame for readability)
        r_label = MathTex(r"r = \text{radius}", font_size=28, color=GREEN)
        h_label = MathTex(r"h = \text{height}", font_size=28, color=ORANGE)
        r_label.to_corner(UR).shift(DOWN * 1.0)
        h_label.next_to(r_label, DOWN, buff=0.35)

        self.add_fixed_in_frame_mobjects(r_label, h_label)
        self.play(Write(r_label), Write(h_label))

        # Slowly orbit so viewer sees the 3-D shape
        self.begin_ambient_camera_rotation(rate=0.25)
        self.wait(4)
        self.stop_ambient_camera_rotation()

        self.play(FadeOut(cyl), FadeOut(header), FadeOut(r_label), FadeOut(h_label))
        self.move_camera(phi=0, theta=-90 * DEGREES, run_time=1)

    # ──────────────────────────────────────────────────────────────────
    def show_derivation(self):
        """Animate the formula build-up."""
        header = Text("Building the Formula", font_size=36, color=BLUE_B).to_edge(UP)
        self.play(FadeIn(header))

        steps = [
            MathTex(r"\text{Area of circular base:}",
                    r"\quad A = \pi r^2",
                    font_size=32),
            MathTex(r"\text{Multiply by height } h:",
                    r"\quad V = A \times h",
                    font_size=32),
            MathTex(r"\therefore",
                    r"\quad V = \pi r^2 h",
                    font_size=38, color=YELLOW),
        ]

        group = VGroup(*steps).arrange(DOWN, aligned_edge=LEFT, buff=0.6).center()

        for step in steps:
            self.play(Write(step), run_time=1.2)
            self.wait(0.6)

        box = SurroundingRectangle(steps[-1], color=YELLOW, buff=0.22,
                                   corner_radius=0.1)
        self.play(Create(box))
        self.wait(2)
        self.play(FadeOut(VGroup(header, group, box)))

    # ──────────────────────────────────────────────────────────────────
    def show_numeric_example(self):
        """Worked example: r = 3 cm, h = 5 cm."""
        header = Text("Worked Example", font_size=36, color=BLUE_B).to_edge(UP)
        self.play(FadeIn(header))

        problem = MathTex(
            r"\text{A cylinder has radius } r = 3\ \text{cm}",
            r"\text{ and height } h = 5\ \text{cm.}",
            font_size=30,
        ).arrange(DOWN, aligned_edge=LEFT).shift(UP * 1.9)
        self.play(Write(problem), run_time=1.4)
        self.wait(0.5)

        steps = VGroup(
            MathTex(r"\text{Step 1:}\quad \pi r^2 = \pi \times 3^2 = 9\pi",
                    font_size=32),
            MathTex(r"\text{Step 2:}\quad V = 9\pi \times 5 = 45\pi",
                    font_size=32),
            MathTex(r"\text{Step 3:}\quad V \approx 141.4\ \text{cm}^3",
                    font_size=32, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5).center().shift(DOWN * 0.2)

        for step in steps:
            self.play(Write(step), run_time=1.1)
            self.wait(0.7)

        box = SurroundingRectangle(steps[-1], color=YELLOW, buff=0.2,
                                   corner_radius=0.1)
        self.play(Create(box))
        self.wait(2)
        self.play(FadeOut(VGroup(header, problem, steps, box)))

    # ──────────────────────────────────────────────────────────────────
    def show_parameter_effect(self):
        """Graph: show how V scales with r (quadratic) and h (linear)."""
        header = Text("How r and h affect Volume", font_size=34, color=BLUE_B).to_edge(UP)
        self.play(FadeIn(header))

        note = MathTex(
            r"V \propto r^2 \quad \text{(doubling } r \text{ quadruples } V)",
            r"\qquad V \propto h \quad \text{(doubling } h \text{ doubles } V)",
            font_size=26, color=WHITE,
        ).arrange(DOWN).next_to(header, DOWN, buff=0.35)
        self.play(Write(note), run_time=1.4)
        self.wait(0.5)

        ax = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 80, 10],
            x_length=7,
            y_length=4.2,
            axis_config={"color": GREY_B, "include_numbers": True},
        ).center().shift(DOWN * 0.6)

        x_lbl = ax.get_x_axis_label(MathTex("r \\ \\text{or}\\ h"), direction=RIGHT)
        y_lbl = ax.get_y_axis_label(MathTex("V"), direction=UP)

        self.play(Create(ax), Write(x_lbl), Write(y_lbl))

        # V vs r  (h fixed = 2)  → quadratic
        h_fixed = 2
        curve_r = ax.plot(lambda r: PI * r**2 * h_fixed,
                          color=GREEN, x_range=[0, 3.5])
        lbl_r   = MathTex(r"V = \pi r^2 \cdot 2 \quad (h=2)",
                           font_size=24, color=GREEN)
        lbl_r.next_to(ax.i2gp(3.5, curve_r), RIGHT, buff=0.3)

        # V vs h  (r fixed = 2)  → linear
        r_fixed = 2
        curve_h = ax.plot(lambda h: PI * r_fixed**2 * h,
                          color=ORANGE, x_range=[0, 4.8])
        lbl_h   = MathTex(r"V = \pi \cdot 4 \cdot h \quad (r=2)",
                           font_size=24, color=ORANGE)
        lbl_h.next_to(ax.i2gp(4.8, curve_h), RIGHT, buff=0.3)
        lbl_h.shift(UP * 0.35)

        self.play(Create(curve_r), Write(lbl_r), run_time=1.2)
        self.wait(0.4)
        self.play(Create(curve_h), Write(lbl_h), run_time=1.2)
        self.wait(0.6)

        # Highlight doubling r  (r: 1 → 2, h=2)
        dot1 = Dot(ax.c2p(1, PI * 1**2 * 2), color=YELLOW, radius=0.1)
        dot2 = Dot(ax.c2p(2, PI * 2**2 * 2), color=YELLOW, radius=0.1)
        arrow = Arrow(dot1.get_center(), dot2.get_center(),
                      buff=0.1, color=YELLOW, stroke_width=2)
        double_lbl = MathTex(r"r \times 2 \Rightarrow V \times 4",
                              font_size=24, color=YELLOW)
        double_lbl.next_to(arrow, RIGHT, buff=0.15)

        self.play(FadeIn(dot1), FadeIn(dot2), Create(arrow), Write(double_lbl))
        self.wait(2.5)

        self.play(FadeOut(VGroup(header, note, ax, x_lbl, y_lbl,
                                  curve_r, lbl_r, curve_h, lbl_h,
                                  dot1, dot2, arrow, double_lbl)))