from manim import *
import numpy as np


class CrossSections(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES)

        title = Text("Cross Sections of 3D Figures", font_size=36, color=WHITE)
        title.to_corner(UL)
        title.fix_in_frame()

        subtitle = Text("Slicing shapes to reveal hidden geometry", font_size=22, color=YELLOW_B)
        subtitle.next_to(title, DOWN, aligned_edge=LEFT)
        subtitle.fix_in_frame()

        self.play(Write(title), FadeIn(subtitle))
        self.wait(1)
        self.play(FadeOut(subtitle))

        self._show_cylinder(title)
        self._show_sphere(title)
        self._show_cone(title)
        self._show_prism(title)

        closing = Text(
            "Cross sections reveal the inner structure\nof every 3D shape!",
            font_size=28, color=WHITE
        ).fix_in_frame()
        self.play(FadeIn(closing))
        self.wait(3)
        self.play(FadeOut(closing), FadeOut(title))

    def _label(self, text, color=YELLOW):
        lbl = Text(text, font_size=28, color=color).to_corner(UR).fix_in_frame()
        return lbl

    def _cs_label(self, text, color=GREEN):
        lbl = Text(text, font_size=24, color=color).to_edge(DOWN).fix_in_frame()
        return lbl

    # ── CYLINDER ──────────────────────────────────────────────
    def _show_cylinder(self, title):
        lbl = self._label("Cylinder")
        self.play(Write(lbl))

        cyl = Cylinder(radius=1, height=2.5, color=BLUE_D,
                       fill_opacity=0.45, stroke_color=BLUE_A, stroke_width=1.5)
        self.play(Create(cyl), run_time=1.5)
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(2)
        self.stop_ambient_camera_rotation()

        plane = Square(side_length=3, color=WHITE, fill_color=WHITE, fill_opacity=0.15)
        plane.set_stroke(WHITE, 2)
        self.play(Create(plane))
        self.play(plane.animate.shift(DOWN * 1.0), run_time=1.2)

        circle = Circle(radius=1, color=GREEN, stroke_width=6)
        cs_lbl = self._cs_label("Cross Section: Circle  ●")
        self.play(Create(circle), Write(cs_lbl))
        self.wait(2)

        self.play(FadeOut(cyl), FadeOut(plane), FadeOut(circle), FadeOut(lbl), FadeOut(cs_lbl))

    # ── SPHERE ────────────────────────────────────────────────
    def _show_sphere(self, title):
        lbl = self._label("Sphere")
        self.play(Write(lbl))

        sphere = Sphere(radius=1.4, color=RED_D, fill_opacity=0.55)
        sphere.set_stroke(RED_A, 1)
        self.play(Create(sphere), run_time=1.5)
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(2)
        self.stop_ambient_camera_rotation()

        plane = Square(side_length=3.5, color=WHITE, fill_color=WHITE, fill_opacity=0.12)
        plane.set_stroke(WHITE, 2)
        self.play(Create(plane))
        self.play(plane.animate.shift(DOWN * 0.4), run_time=1.2)

        great_circle = Circle(radius=1.4, color=GREEN, stroke_width=6)
        cs_lbl = self._cs_label("Cross Section: Great Circle  ●")
        self.play(Create(great_circle), Write(cs_lbl))
        self.wait(1.5)

        smaller = Circle(radius=0.9, color=YELLOW, stroke_width=5)
        off_lbl = self._cs_label("Off-center slice → Smaller Circle  ●")
        self.play(
            plane.animate.shift(DOWN * 0.7),
            ReplacementTransform(great_circle, smaller),
            ReplacementTransform(cs_lbl, off_lbl),
            run_time=1.2
        )
        self.wait(2)

        self.play(FadeOut(sphere), FadeOut(plane), FadeOut(smaller), FadeOut(lbl), FadeOut(off_lbl))

    # ── CONE ──────────────────────────────────────────────────
    def _show_cone(self, title):
        lbl = self._label("Cone")
        self.play(Write(lbl))

        cone = Cone(base_radius=1.3, height=2.8, color=ORANGE,
                    fill_opacity=0.5, stroke_color=YELLOW_A, stroke_width=1.5)
        cone.shift(DOWN * 0.5)
        self.play(Create(cone), run_time=1.5)
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(2)
        self.stop_ambient_camera_rotation()

        plane = Square(side_length=3.2, color=WHITE, fill_color=WHITE, fill_opacity=0.12)
        plane.set_stroke(WHITE, 2)
        self.play(Create(plane))
        self.play(plane.animate.shift(DOWN * 0.8), run_time=1)

        big_circle = Circle(radius=1.0, color=GREEN, stroke_width=6)
        cs_lbl = self._cs_label("Horizontal slice → Circle  ●")
        self.play(Create(big_circle), Write(cs_lbl))
        self.wait(1.5)

        small_circle = Circle(radius=0.45, color=GREEN, stroke_width=6)
        up_lbl = self._cs_label("Higher slice → Smaller Circle  ●")
        self.play(
            plane.animate.shift(UP * 0.9),
            ReplacementTransform(big_circle, small_circle),
            ReplacementTransform(cs_lbl, up_lbl),
            run_time=1.2
        )
        self.wait(2)

        self.play(FadeOut(cone), FadeOut(plane), FadeOut(small_circle), FadeOut(lbl), FadeOut(up_lbl))

    # ── RECTANGULAR PRISM ─────────────────────────────────────
    def _show_prism(self, title):
        lbl = self._label("Rectangular Prism")
        self.play(Write(lbl))

        prism = Prism(dimensions=[2.5, 1.5, 2.0], fill_color=PURPLE_D,
                      fill_opacity=0.5, stroke_color=PURPLE_A, stroke_width=1.5)
        self.play(Create(prism), run_time=1.5)
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(2)
        self.stop_ambient_camera_rotation()

        plane = Rectangle(width=3.5, height=2.5, color=WHITE,
                          fill_color=WHITE, fill_opacity=0.12)
        plane.set_stroke(WHITE, 2)
        self.play(Create(plane))
        self.play(plane.animate.shift(DOWN * 0.3), run_time=1)

        rect = Rectangle(width=2.5, height=1.5, color=GREEN, stroke_width=6)
        cs_lbl = self._cs_label("Horizontal slice → Rectangle  ▬")
        self.play(Create(rect), Write(cs_lbl))
        self.wait(2)

        diag_shape = Polygon(
            [-1.4, -0.6, 0], [1.4, -0.6, 0], [1.0, 0.6, 0], [-1.8, 0.6, 0],
            color=YELLOW, stroke_width=6
        )
        diag_lbl = self._cs_label("Diagonal slice → Parallelogram  ▱")
        self.play(
            plane.animate.rotate(20 * DEGREES, axis=RIGHT),
            ReplacementTransform(rect, diag_shape),
            ReplacementTransform(cs_lbl, diag_lbl),
            run_time=1.5
        )
        self.wait(2)

        self.play(FadeOut(prism), FadeOut(plane), FadeOut(diag_shape), FadeOut(lbl), FadeOut(diag_lbl))


if __name__ == "__main__":
    import subprocess, sys
    quality = sys.argv[1] if len(sys.argv) > 1 else "l"
    subprocess.run(["manim", f"-pq{quality}", __file__, "CrossSections"])