from manim import *
import numpy as np


# ─────────────────────────────────────────────────────────────────────────────
# Helper: build a Surface of revolution by rotating f(x) around the x-axis
# ─────────────────────────────────────────────────────────────────────────────
def revolution_surface(f, x_min, x_max, color=BLUE_D, opacity=0.85, resolution=30):
    """
    Returns a Surface obtained by rotating y = f(x) (f(x) >= 0) around the x-axis.
    Parametrisation:  P(x, v) = (x,  f(x)*cos(v),  f(x)*sin(v))
    """
    def param(u, v):
        x = x_min + u * (x_max - x_min)
        r = f(x)
        return np.array([x, r * np.cos(v), r * np.sin(v)])

    surf = Surface(
        param,
        u_range=[0, 1],
        v_range=[0, TAU],
        resolution=(resolution, resolution),
        fill_opacity=opacity,
    )
    surf.set_fill_by_checkerboard(color, color.darker(0.3) if hasattr(color, "darker") else BLUE_E, opacity=opacity)
    surf.set_style(stroke_width=0.3, stroke_color=WHITE)
    return surf


# ─────────────────────────────────────────────────────────────────────────────
# Helper: build end-cap disk at x = x0 with radius r
# ─────────────────────────────────────────────────────────────────────────────
def end_cap(x0, r, color=BLUE_D, opacity=0.7):
    def param(u, v):
        radius = u * r
        return np.array([x0, radius * np.cos(v), radius * np.sin(v)])
    cap = Surface(param, u_range=[0, 1], v_range=[0, TAU],
                  resolution=(12, 24), fill_opacity=opacity)
    cap.set_fill_by_checkerboard(color, color, opacity=opacity)
    cap.set_style(stroke_width=0.2, stroke_color=WHITE)
    return cap


# ─────────────────────────────────────────────────────────────────────────────
# Main scene
# ─────────────────────────────────────────────────────────────────────────────
class SolidsOfRevolution(ThreeDScene):

    def construct(self):
        self._intro()
        self._demo_semicircle()
        self._demo_rectangle()
        self._demo_triangle()
        self._demo_parabola()
        self._outro()

    # ── intro title ──────────────────────────────────────────────────────────
    def _intro(self):
        title = Text("Solids of Revolution", font_size=52, color=YELLOW)
        sub   = Text("Rotating 2D figures about the x-axis", font_size=28, color=WHITE)
        sub.next_to(title, DOWN, buff=0.4)
        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(sub, shift=UP * 0.3))
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(sub))

    # ── shared: section header ────────────────────────────────────────────────
    def _section_header(self, shape_name, solid_name):
        header = Text(f"{shape_name}  →  {solid_name}", font_size=36, color=YELLOW)
        self.add_fixed_in_frame_mobjects(header)
        header.to_corner(UL, buff=0.35)
        self.play(Write(header), run_time=0.8)
        return header

    # ── shared: remove all mobjects cleanly ──────────────────────────────────
    def _clear_scene(self, *mobjects):
        self.play(*[FadeOut(m) for m in mobjects if m is not None], run_time=0.6)

    # =========================================================================
    # DEMO 1 — Semicircle → Sphere
    # =========================================================================
    def _demo_semicircle(self):
        # ── 2D setup ─────────────────────────────────────────────────────────
        self.set_camera_orientation(phi=0, theta=-PI / 2)   # flat front view
        axes2d = Axes(
            x_range=[-2.5, 2.5, 1], y_range=[-0.3, 2.5, 1],
            x_length=6, y_length=4,
            axis_config={"include_tip": True, "color": WHITE},
        ).shift(DOWN * 0.3)

        # Semicircle: upper half of unit circle scaled to radius 2
        R = 2.0
        curve = axes2d.plot(lambda x: np.sqrt(max(R**2 - x**2, 0)),
                            x_range=[-R, R], color=BLUE_B, stroke_width=3)
        region = axes2d.get_area(curve, x_range=[-R, R], color=BLUE_D, opacity=0.4)
        diam   = axes2d.plot(lambda x: 0, x_range=[-R, R],
                             color=WHITE, stroke_width=2, stroke_opacity=0.5)

        label_curve = MathTex(r"y = \sqrt{r^2 - x^2}", font_size=30, color=BLUE_B)
        label_curve.next_to(axes2d, UP, buff=0.1).shift(RIGHT * 0.5)

        header = self._section_header("Semicircle", "Sphere")

        self.play(Create(axes2d), run_time=0.8)
        self.play(Create(curve), Create(diam), run_time=1.0)
        self.play(FadeIn(region), Write(label_curve), run_time=0.8)
        self.wait(0.8)

        # ── transition to 3D ─────────────────────────────────────────────────
        self.play(FadeOut(region), FadeOut(curve), FadeOut(diam),
                  FadeOut(label_curve), FadeOut(axes2d), run_time=0.5)

        axes3d = ThreeDAxes(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1],
            x_length=6, y_length=6, z_length=6,
        )
        self.play(Create(axes3d), run_time=0.6)
        self.move_camera(phi=70 * DEGREES, theta=-60 * DEGREES, run_time=1.5)

        # ── sweeping half-disk (trace of rotation) ───────────────────────────
        def sweep_surface(angle_max):
            def param(u, v):
                x = -R + u * 2 * R
                r = np.sqrt(max(R**2 - x**2, 0))
                theta = v * angle_max
                return np.array([x, r * np.cos(theta), r * np.sin(theta)])
            surf = Surface(param, u_range=[0, 1], v_range=[0, 1],
                           resolution=(20, 20), fill_opacity=0.75)
            surf.set_fill_by_checkerboard(BLUE_D, TEAL_D, opacity=0.75)
            surf.set_style(stroke_width=0.2, stroke_color=WHITE)
            return surf

        # Show rotation sweep
        partial = sweep_surface(PI / 6)
        self.play(FadeIn(partial), run_time=0.4)
        for frac in [1/3, 1/2, 2/3, 5/6, 1]:
            new_partial = sweep_surface(TAU * frac)
            self.play(Transform(partial, new_partial), run_time=0.35)
        self.remove(partial)

        # ── full sphere ───────────────────────────────────────────────────────
        sphere = Surface(
            lambda u, v: np.array([
                R * np.cos(u) * np.cos(v),
                R * np.cos(u) * np.sin(v),
                R * np.sin(u),
            ]),
            u_range=[-PI / 2, PI / 2],
            v_range=[0, TAU],
            resolution=(24, 48),
            fill_opacity=0.85,
        )
        sphere.set_fill_by_checkerboard(BLUE_D, TEAL_D, opacity=0.85)
        sphere.set_style(stroke_width=0.2, stroke_color=WHITE)

        self.play(FadeIn(sphere), run_time=0.5)
        self.begin_ambient_camera_rotation(rate=0.25)
        self.wait(3)
        self.stop_ambient_camera_rotation()

        self._clear_scene(axes3d, sphere, header)
        self.set_camera_orientation(phi=0, theta=-PI / 2)

    # =========================================================================
    # DEMO 2 — Rectangle → Cylinder
    # =========================================================================
    def _demo_rectangle(self):
        self.set_camera_orientation(phi=0, theta=-PI / 2)
        axes2d = Axes(
            x_range=[-0.3, 3.5, 1], y_range=[-0.3, 2.5, 1],
            x_length=6, y_length=4,
            axis_config={"include_tip": True, "color": WHITE},
        ).shift(DOWN * 0.3 + LEFT * 0.5)

        # Rectangle from x=1 to x=3, height=1.8
        x0, x1, h = 1.0, 3.0, 1.8
        rect = axes2d.get_area(
            axes2d.plot(lambda x: h, x_range=[x0, x1], color=GREEN_B, stroke_width=3),
            x_range=[x0, x1], color=GREEN_D, opacity=0.5,
        )
        rect_outline = axes2d.plot(lambda x: h, x_range=[x0, x1],
                                   color=GREEN_B, stroke_width=3)
        vert_l = axes2d.plot_parametric_curve(lambda t: [x0, t, 0],
                                              t_range=[0, h], color=GREEN_B)
        vert_r = axes2d.plot_parametric_curve(lambda t: [x1, t, 0],
                                              t_range=[0, h], color=GREEN_B)

        label = MathTex(r"\text{Rectangle}", font_size=30, color=GREEN_B)
        label.next_to(axes2d, UP, buff=0.1)

        header = self._section_header("Rectangle", "Cylinder")

        self.play(Create(axes2d), run_time=0.8)
        self.play(Create(rect_outline), Create(vert_l), Create(vert_r),
                  FadeIn(rect), Write(label), run_time=1.0)
        self.wait(0.8)

        self.play(FadeOut(rect), FadeOut(rect_outline), FadeOut(vert_l),
                  FadeOut(vert_r), FadeOut(label), FadeOut(axes2d), run_time=0.5)

        axes3d = ThreeDAxes(
            x_range=[-0.5, 4, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1],
            x_length=7, y_length=6, z_length=6,
        )
        self.play(Create(axes3d), run_time=0.6)
        self.move_camera(phi=70 * DEGREES, theta=-60 * DEGREES, run_time=1.5)

        # Cylinder surface (lateral)
        cyl = Surface(
            lambda u, v: np.array([
                x0 + u * (x1 - x0),
                h * np.cos(v),
                h * np.sin(v),
            ]),
            u_range=[0, 1], v_range=[0, TAU],
            resolution=(12, 48), fill_opacity=0.8,
        )
        cyl.set_fill_by_checkerboard(GREEN_D, TEAL_E, opacity=0.8)
        cyl.set_style(stroke_width=0.2, stroke_color=WHITE)

        cap_left  = end_cap(x0, h, color=GREEN_D, opacity=0.75)
        cap_right = end_cap(x1, h, color=GREEN_D, opacity=0.75)

        self.play(FadeIn(cyl), FadeIn(cap_left), FadeIn(cap_right), run_time=0.7)
        self.begin_ambient_camera_rotation(rate=0.25)
        self.wait(3)
        self.stop_ambient_camera_rotation()

        self._clear_scene(axes3d, cyl, cap_left, cap_right, header)
        self.set_camera_orientation(phi=0, theta=-PI / 2)

    # =========================================================================
    # DEMO 3 — Triangle → Cone
    # =========================================================================
    def _demo_triangle(self):
        self.set_camera_orientation(phi=0, theta=-PI / 2)
        axes2d = Axes(
            x_range=[-0.3, 3.5, 1], y_range=[-0.3, 2.5, 1],
            x_length=6, y_length=4,
            axis_config={"include_tip": True, "color": WHITE},
        ).shift(DOWN * 0.3 + LEFT * 0.5)

        # Triangle: right angle at origin, base along x to x=3, height=2 on y-axis
        # Hypotenuse: y = 2 - (2/3)*x  from x=0 to x=3
        x_base = 3.0
        hyp_height = 2.0

        def hyp(x):
            return hyp_height * (1 - x / x_base)

        hyp_curve = axes2d.plot(hyp, x_range=[0, x_base],
                                color=RED_B, stroke_width=3)
        triangle_region = axes2d.get_area(hyp_curve, x_range=[0, x_base],
                                          color=RED_D, opacity=0.45)
        vert_side = axes2d.plot_parametric_curve(
            lambda t: [0, t, 0], t_range=[0, hyp_height], color=RED_B)
        label = MathTex(r"y = h\!\left(1 - \tfrac{x}{b}\right)", font_size=28, color=RED_B)
        label.next_to(axes2d, UP, buff=0.1)

        header = self._section_header("Triangle", "Cone")

        self.play(Create(axes2d), run_time=0.8)
        self.play(Create(hyp_curve), Create(vert_side),
                  FadeIn(triangle_region), Write(label), run_time=1.0)
        self.wait(0.8)

        self.play(FadeOut(triangle_region), FadeOut(hyp_curve),
                  FadeOut(vert_side), FadeOut(label), FadeOut(axes2d), run_time=0.5)

        axes3d = ThreeDAxes(
            x_range=[-0.5, 4, 1], y_range=[-3, 3, 1], z_range=[-3, 3, 1],
            x_length=7, y_length=6, z_length=6,
        )
        self.play(Create(axes3d), run_time=0.6)
        self.move_camera(phi=70 * DEGREES, theta=-60 * DEGREES, run_time=1.5)

        # Cone surface: apex at x=x_base, base circle at x=0 with radius=hyp_height
        cone = Surface(
            lambda u, v: np.array([
                u * x_base,
                hyp(u * x_base) * np.cos(v),
                hyp(u * x_base) * np.sin(v),
            ]),
            u_range=[0, 1], v_range=[0, TAU],
            resolution=(20, 48), fill_opacity=0.85,
        )
        cone.set_fill_by_checkerboard(RED_D, MAROON_D, opacity=0.85)
        cone.set_style(stroke_width=0.2, stroke_color=WHITE)

        # Base cap
        cone_cap = end_cap(0, hyp_height, color=RED_D, opacity=0.75)

        self.play(FadeIn(cone), FadeIn(cone_cap), run_time=0.7)
        self.begin_ambient_camera_rotation(rate=0.25)
        self.wait(3)
        self.stop_ambient_camera_rotation()

        self._clear_scene(axes3d, cone, cone_cap, header)
        self.set_camera_orientation(phi=0, theta=-PI / 2)

    # =========================================================================
    # DEMO 4 — Parabola → Paraboloid
    # =========================================================================
    def _demo_parabola(self):
        self.set_camera_orientation(phi=0, theta=-PI / 2)
        axes2d = Axes(
            x_range=[-0.3, 3.5, 1], y_range=[-0.3, 2.5, 1],
            x_length=6, y_length=4,
            axis_config={"include_tip": True, "color": WHITE},
        ).shift(DOWN * 0.3 + LEFT * 0.5)

        def parab(x):
            return 0.7 * np.sqrt(x)      # y = 0.7*sqrt(x)

        x_end = 3.0
        curve = axes2d.plot(parab, x_range=[0.001, x_end],
                            color=ORANGE, stroke_width=3)
        region = axes2d.get_area(curve, x_range=[0.001, x_end],
                                 color=GOLD_D, opacity=0.45)
        label = MathTex(r"y = \sqrt{x}", font_size=30, color=ORANGE)
        label.next_to(axes2d, UP, buff=0.1)

        header = self._section_header("Parabola", "Paraboloid")

        self.play(Create(axes2d), run_time=0.8)
        self.play(Create(curve), FadeIn(region), Write(label), run_time=1.0)
        self.wait(0.8)

        self.play(FadeOut(region), FadeOut(curve),
                  FadeOut(label), FadeOut(axes2d), run_time=0.5)

        axes3d = ThreeDAxes(
            x_range=[-0.5, 4, 1], y_range=[-2.5, 2.5, 1], z_range=[-2.5, 2.5, 1],
            x_length=7, y_length=6, z_length=6,
        )
        self.play(Create(axes3d), run_time=0.6)
        self.move_camera(phi=70 * DEGREES, theta=-60 * DEGREES, run_time=1.5)

        # Paraboloid surface
        paraboloid = Surface(
            lambda u, v: np.array([
                u * x_end,
                parab(u * x_end + 0.001) * np.cos(v),
                parab(u * x_end + 0.001) * np.sin(v),
            ]),
            u_range=[0, 1], v_range=[0, TAU],
            resolution=(24, 48), fill_opacity=0.85,
        )
        paraboloid.set_fill_by_checkerboard(GOLD_D, ORANGE, opacity=0.85)
        paraboloid.set_style(stroke_width=0.2, stroke_color=WHITE)

        # End cap at x = x_end
        para_cap = end_cap(x_end, parab(x_end), color=GOLD_D, opacity=0.75)

        self.play(FadeIn(paraboloid), FadeIn(para_cap), run_time=0.7)
        self.begin_ambient_camera_rotation(rate=0.25)
        self.wait(3)
        self.stop_ambient_camera_rotation()

        self._clear_scene(axes3d, paraboloid, para_cap, header)
        self.set_camera_orientation(phi=0, theta=-PI / 2)

    # ── outro ─────────────────────────────────────────────────────────────────
    def _outro(self):
        lines = VGroup(
            Text("Solids of Revolution", font_size=44, color=YELLOW),
            Text("Semicircle  →  Sphere",    font_size=28, color=BLUE_B),
            Text("Rectangle   →  Cylinder",  font_size=28, color=GREEN_B),
            Text("Triangle    →  Cone",      font_size=28, color=RED_B),
            Text("Parabola    →  Paraboloid",font_size=28, color=ORANGE),
        ).arrange(DOWN, buff=0.35).move_to(ORIGIN)

        self.play(LaggedStart(*[FadeIn(l, shift=RIGHT * 0.3) for l in lines],
                              lag_ratio=0.18), run_time=2)
        self.wait(2)
        self.play(FadeOut(lines))