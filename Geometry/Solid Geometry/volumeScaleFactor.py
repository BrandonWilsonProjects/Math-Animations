from manim import *


class ScaleVolumeRelationship(ThreeDScene):
    def construct(self):
        # ── Title Screen ──────────────────────────────────────────────
        title = Text("Scale Factor & Volume Scale Factor", font_size=42, color=BLUE)
        subtitle = Text("If scale factor = k,  then volume scale factor = k³",
                        font_size=28, color=YELLOW)
        subtitle.next_to(title, DOWN, buff=0.4)

        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle, shift=UP * 0.3))
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(subtitle))

        # ── Part 1: Formula derivation ────────────────────────────────
        self.show_formula()

        # ── Part 2: 3-D cube animation ────────────────────────────────
        self.show_cube_scaling()

        # ── Part 3: Graph k vs k³ ─────────────────────────────────────
        self.show_graph()

        # ── Outro ─────────────────────────────────────────────────────
        outro = Text("Volume grows MUCH faster than length!", font_size=36, color=GREEN)
        self.play(Write(outro))
        self.wait(2)
        self.play(FadeOut(outro))

    # ──────────────────────────────────────────────────────────────────
    def show_formula(self):
        """Animate the algebraic derivation."""
        header = Text("The Rule", font_size=38, color=BLUE_B).to_edge(UP)

        line1 = MathTex(r"\text{Original volume:}", r"V = s^3")
        line2 = MathTex(r"\text{Scale each side by } k:", r"(ks)^3 = k^3 s^3")
        line3 = MathTex(r"\Rightarrow", r"\text{Volume scale factor} = k^3",
                        color=YELLOW)

        lines = VGroup(line1, line2, line3).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        lines.center()

        box = SurroundingRectangle(line3, color=YELLOW, buff=0.2, corner_radius=0.1)

        self.play(FadeIn(header))
        for line in lines:
            self.play(Write(line), run_time=1.2)
            self.wait(0.5)

        self.play(Create(box))
        self.wait(2)
        self.play(FadeOut(VGroup(header, lines, box)))

    # ──────────────────────────────────────────────────────────────────
    def show_cube_scaling(self):
        """Show a unit cube scaling and track side vs volume."""
        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES)

        header = Text("Scaling a Cube", font_size=34, color=BLUE_B)
        header.to_corner(UL)
        self.add_fixed_in_frame_mobjects(header)
        self.play(FadeIn(header))

        # Create labels once and pin them to the frame
        side_label = MathTex(r"k = 1", font_size=30, color=WHITE)
        vol_label  = MathTex(r"k^3 = 1", font_size=30, color=YELLOW)
        side_label.to_corner(UR).shift(DOWN * 0.8)
        vol_label.next_to(side_label, DOWN, buff=0.3)
        self.add_fixed_in_frame_mobjects(side_label, vol_label)

        cube = Cube(side_length=1, fill_color=BLUE, fill_opacity=0.45,
                    stroke_color=WHITE, stroke_width=1.5)
        self.play(Create(cube), Write(side_label), Write(vol_label))
        self.wait(1.2)

        for k in [2, 3]:
            new_cube = Cube(side_length=k, fill_color=BLUE, fill_opacity=0.45,
                            stroke_color=WHITE, stroke_width=1.5)

            # Build replacement labels at the same anchored positions
            new_side = MathTex(rf"k = {k}", font_size=30, color=WHITE)
            new_vol  = MathTex(rf"k^3 = {k**3}", font_size=30, color=YELLOW)
            new_side.to_corner(UR).shift(DOWN * 0.8)
            new_vol.next_to(new_side, DOWN, buff=0.3)

            # Transform cube; swap label content via FadeTransform on fixed-frame objects
            self.play(
                Transform(cube, new_cube),
                FadeTransform(side_label, new_side),
                FadeTransform(vol_label,  new_vol),
                run_time=1.8,
            )
            # Re-pin the new label objects so subsequent transforms work correctly
            self.add_fixed_in_frame_mobjects(new_side, new_vol)
            side_label = new_side
            vol_label  = new_vol
            self.wait(1.2)

        # Clean up
        self.play(FadeOut(cube),
                  FadeOut(side_label),
                  FadeOut(vol_label),
                  FadeOut(header))
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES)

    # ──────────────────────────────────────────────────────────────────
    def show_graph(self):
        """Plot k (x-axis) vs k³ (y-axis) and compare with k¹ and k²."""
        header = Text("Graph: k  vs  k³", font_size=34, color=BLUE_B).to_edge(UP)
        self.play(FadeIn(header))

        ax = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 65, 10],
            x_length=7,
            y_length=5,
            axis_config={"color": GREY_B, "include_numbers": True},
        ).center().shift(DOWN * 0.3)

        x_label = ax.get_x_axis_label(MathTex("k"), direction=RIGHT)
        y_label = ax.get_y_axis_label(MathTex("\\text{scale factor}"), direction=UP)

        self.play(Create(ax), Write(x_label), Write(y_label))

        # k¹  – length scale factor (green)
        curve_k1 = ax.plot(lambda x: x,      color=GREEN,  x_range=[0, 4])
        lbl_k1   = MathTex("k", color=GREEN, font_size=28)
        lbl_k1.next_to(ax.i2gp(3.8, curve_k1), RIGHT, buff=0.15)

        # k²  – area scale factor (orange)
        curve_k2 = ax.plot(lambda x: x**2,   color=ORANGE, x_range=[0, 4])
        lbl_k2   = MathTex("k^2", color=ORANGE, font_size=28)
        lbl_k2.next_to(ax.i2gp(3.8, curve_k2), RIGHT, buff=0.15)

        # k³  – volume scale factor (red)
        curve_k3 = ax.plot(lambda x: x**3,   color=RED,    x_range=[0, 4])
        lbl_k3   = MathTex("k^3", color=RED, font_size=28)
        lbl_k3.next_to(ax.i2gp(2.5, curve_k3), RIGHT, buff=0.15)

        self.play(Create(curve_k1), Write(lbl_k1), run_time=1)
        self.wait(0.4)
        self.play(Create(curve_k2), Write(lbl_k2), run_time=1)
        self.wait(0.4)
        self.play(Create(curve_k3), Write(lbl_k3), run_time=1.5)
        self.wait(0.6)

        # Highlight a single k value
        k_val  = 3
        dot_k3 = Dot(ax.c2p(k_val, k_val**3), color=YELLOW, radius=0.12)
        vline  = ax.get_vertical_line(ax.c2p(k_val, k_val**3), color=YELLOW,
                                      stroke_width=2, line_func=DashedLine)
        annotation = MathTex(rf"k={k_val} \Rightarrow k^3={k_val**3}",
                              font_size=28, color=YELLOW)
        annotation.next_to(dot_k3, UP + LEFT, buff=0.25)

        self.play(Create(vline), FadeIn(dot_k3), Write(annotation))
        self.wait(2.5)

        self.play(FadeOut(VGroup(ax, x_label, y_label,
                                  curve_k1, lbl_k1,
                                  curve_k2, lbl_k2,
                                  curve_k3, lbl_k3,
                                  dot_k3, vline, annotation,
                                  header)))