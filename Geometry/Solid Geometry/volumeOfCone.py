from manim import *


class ConeVolume(ThreeDScene):
    def construct(self):
        # ── Title ─────────────────────────────────────────────────────
        title    = Text("Volume of a Cone", font_size=44, color=RED)
        subtitle = Text("V = ⅓πr²h", font_size=32, color=YELLOW)
        subtitle.next_to(title, DOWN, buff=0.4)

        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle, shift=UP * 0.3))
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(subtitle))

        # ── Scene 1: One-third intuition ──────────────────────────────
        self.show_one_third_intuition()

        # ── Scene 2: 3-D cone with labelled dimensions ─────────────────
        self.show_labelled_cone()

        # ── Scene 3: Formula derivation ───────────────────────────────
        self.show_derivation()

        # ── Scene 4: Numeric worked example ───────────────────────────
        self.show_numeric_example()

        # ── Scene 5: Effect of changing r vs h ────────────────────────
        self.show_parameter_effect()

        # ── Outro ─────────────────────────────────────────────────────
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES)
        outro = Text("V = ⅓πr²h", font_size=52, color=YELLOW)
        self.play(Write(outro))
        self.wait(2)
        self.play(FadeOut(outro))

    # ──────────────────────────────────────────────────────────────────
    def show_one_third_intuition(self):
        """Show shrinking disc stack that tapers — motivating the 1/3 factor."""
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES)

        header = Text("Key Idea: A Tapering Stack", font_size=34, color=RED_B).to_edge(UP)
        self.play(FadeIn(header))

        idea = Text(
            "A cone is like a cylinder, but the discs shrink to a point.",
            font_size=26, color=WHITE,
        ).next_to(header, DOWN, buff=0.4)
        self.play(Write(idea), run_time=1.3)
        self.wait(0.5)

        # Draw tapering disc stack
        n_discs  = 10
        disc_h   = 0.27
        max_r    = 1.4
        base_y   = -1.9

        discs = VGroup()
        for i in range(n_discs):
            frac   = (n_discs - 1 - i) / (n_discs - 1)   # 1 at base → 0 at tip
            r_disc = max_r * frac + 0.04
            disc   = Ellipse(width=r_disc * 2, height=r_disc * 0.5,
                             fill_color=RED, fill_opacity=0.5,
                             stroke_color=WHITE, stroke_width=1.0)
            disc.move_to(UP * (base_y + i * disc_h))
            discs.add(disc)

        self.play(
            LaggedStart(*[FadeIn(d, shift=UP * 0.1) for d in discs],
                        lag_ratio=0.10),
            run_time=2.5,
        )
        self.wait(0.5)

        # Annotate shrinking radius
        brace = Brace(discs[0], direction=RIGHT, color=YELLOW)
        brace_lbl = brace.get_tex(r"r").scale(0.85)
        tip_lbl = MathTex(r"\text{radius} \to 0\ \text{at tip}",
                           font_size=24, color=ORANGE)
        tip_lbl.next_to(discs[-1], RIGHT, buff=0.5)

        self.play(FadeIn(brace), Write(brace_lbl), Write(tip_lbl))
        self.wait(0.6)

        # The 1/3 punchline
        third_lbl = VGroup(
            MathTex(r"\text{Average disc area} = \tfrac{1}{3}\,\pi r^2",
                    font_size=28, color=YELLOW),
            MathTex(r"\Rightarrow V = \tfrac{1}{3}\,\pi r^2 h",
                    font_size=28, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(DOWN, buff=0.55)
        self.play(Write(third_lbl), run_time=1.5)
        self.wait(2)

        self.play(FadeOut(VGroup(header, idea, discs, brace, brace_lbl,
                                  tip_lbl, third_lbl)))

    # ──────────────────────────────────────────────────────────────────
    def show_labelled_cone(self):
        """Render a 3-D cone and annotate r and h."""
        self.move_camera(phi=65 * DEGREES, theta=-45 * DEGREES, run_time=1.5)

        header = Text("The Dimensions", font_size=34, color=RED_B)
        header.to_corner(UL)
        self.add_fixed_in_frame_mobjects(header)
        self.play(FadeIn(header))

        cone = Cone(base_radius=1.2, height=2.8,
                    fill_color=RED, fill_opacity=0.4,
                    stroke_color=WHITE, stroke_width=1)
        self.play(Create(cone), run_time=1.8)
        self.wait(0.5)

        r_label = MathTex(r"r = \text{base radius}", font_size=28, color=GREEN)
        h_label = MathTex(r"h = \text{height}", font_size=28, color=ORANGE)
        r_label.to_corner(UR).shift(DOWN * 1.0)
        h_label.next_to(r_label, DOWN, buff=0.35)

        self.add_fixed_in_frame_mobjects(r_label, h_label)
        self.play(Write(r_label), Write(h_label))

        self.begin_ambient_camera_rotation(rate=0.25)
        self.wait(4)
        self.stop_ambient_camera_rotation()

        self.play(FadeOut(cone), FadeOut(header), FadeOut(r_label), FadeOut(h_label))
        self.move_camera(phi=0, theta=-90 * DEGREES, run_time=1)

    # ──────────────────────────────────────────────────────────────────
    def show_derivation(self):
        """Animate the formula build-up including the 1/3 comparison."""
        header = Text("Building the Formula", font_size=36, color=RED_B).to_edge(UP)
        self.play(FadeIn(header))

        steps = [
            MathTex(r"\text{Cylinder with same base and height:}\ V_{\mathrm{cyl}} = \pi r^2 h",
                    font_size=30),
            MathTex(r"\text{A cone is exactly } \tfrac{1}{3} \text{ of that cylinder:}",
                    font_size=30),
            MathTex(r"\therefore\ V_{\mathrm{cone}} = \frac{1}{3}\,\pi r^2 h",
                    font_size=38, color=YELLOW),
        ]

        group = VGroup(*steps).arrange(DOWN, aligned_edge=LEFT, buff=0.6).center()

        for step in steps:
            self.play(Write(step), run_time=1.2)
            self.wait(0.6)

        # Cone : Cylinder comparison bar
        bar_cyl  = Rectangle(width=6.0, height=0.45,
                              fill_color=BLUE, fill_opacity=0.5,
                              stroke_color=WHITE, stroke_width=1)
        bar_cone = Rectangle(width=2.0, height=0.45,
                              fill_color=RED, fill_opacity=0.7,
                              stroke_color=WHITE, stroke_width=1)

        bars = VGroup(bar_cyl, bar_cone).arrange(DOWN, buff=0.18)
        bars.next_to(group, DOWN, buff=0.5)

        lbl_cyl  = Text("Cylinder  (πr²h)", font_size=20, color=BLUE_B)
        lbl_cone = Text("Cone  (⅓ πr²h)", font_size=20, color=RED_B)
        lbl_cyl.next_to(bar_cyl,  RIGHT, buff=0.2)
        lbl_cone.next_to(bar_cone, RIGHT, buff=0.2)

        self.play(FadeIn(bar_cyl), FadeIn(bar_cone),
                  Write(lbl_cyl), Write(lbl_cone))

        box = SurroundingRectangle(steps[-1], color=YELLOW, buff=0.22,
                                   corner_radius=0.1)
        self.play(Create(box))
        self.wait(2.5)
        self.play(FadeOut(VGroup(header, group, box, bars, lbl_cyl, lbl_cone)))

    # ──────────────────────────────────────────────────────────────────
    def show_numeric_example(self):
        """Worked example: r = 3 cm, h = 5 cm."""
        header = Text("Worked Example", font_size=36, color=RED_B).to_edge(UP)
        self.play(FadeIn(header))

        problem = VGroup(
            Text("A cone has radius r = 3 cm", font_size=28, color=WHITE),
            Text("and height h = 5 cm.", font_size=28, color=WHITE),
        ).arrange(DOWN, aligned_edge=LEFT).shift(UP * 1.9)
        self.play(Write(problem), run_time=1.4)
        self.wait(0.5)

        steps = VGroup(
            MathTex(r"\text{Step 1:}\quad \pi r^2 = \pi \times 3^2 = 9\pi",
                    font_size=32),
            MathTex(r"\text{Step 2:}\quad 9\pi \times h = 9\pi \times 5 = 45\pi",
                    font_size=32),
            MathTex(r"\text{Step 3:}\quad V = \tfrac{1}{3} \times 45\pi = 15\pi",
                    font_size=32),
            MathTex(r"\text{Step 4:}\quad V \approx 47.1\ \text{cm}^3",
                    font_size=32, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.45).center().shift(DOWN * 0.1)

        for step in steps:
            self.play(Write(step), run_time=1.0)
            self.wait(0.6)

        box = SurroundingRectangle(steps[-1], color=YELLOW, buff=0.2,
                                   corner_radius=0.1)
        self.play(Create(box))

        # Side note: exactly 1/3 of the cylinder (141.4 / 3)
        note = Text("(1/3 of the cylinder: 141.4 / 3 ≈ 47.1)",
                     font_size=22, color=GREY_B)
        note.next_to(steps, DOWN, buff=0.35)
        self.play(FadeIn(note))
        self.wait(2.2)
        self.play(FadeOut(VGroup(header, problem, steps, box, note)))

    
    # ──────────────────────────────────────────────────────────────────
