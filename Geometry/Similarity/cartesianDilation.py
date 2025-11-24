# dilations_lesson_no_latex_fixed.py
from manim import *
import numpy as np

class DilationsInCoordinatePlaneNoLaTeX(Scene):
    def construct(self):
        # Grid and axes
        axes = Axes(
            x_range=[-8, 8, 1],
            y_range=[-5, 5, 1],
            axis_config={"color": BLUE_D},
            x_length=12,
            y_length=7.5,
            tips=False,
        )
        grid = NumberPlane(
            x_range=[-8, 8, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
                "stroke_opacity": 0.3
            }
        )
        self.add(grid, axes)

        # Title (plain text)
        title = Text("Dilations in the Coordinate Plane", font_size=48, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Helper function – now uses only Text objects and fixes point handling
        def dilate_shape(original, center_point, k, shape_name, run_time=3):
            # Center of dilation (create Dot as Mobject for get_center)
            center_dot = Dot(center_point, color=RED, radius=0.08)  # Pass array directly to Dot
            center_label = Text("C", color=RED, font_size=36).next_to(center_dot, DOWN+RIGHT, buff=0.1)

            # Create scaled copy (use center_point array directly in about_point)
            scaled = original.copy().scale(k, about_point=center_point)

            # Simple equation text (no LaTeX)
            eq = Text("New point = k × (old point - C) + C", font_size=36).to_corner(UL)
            k_display = Text(f"k = {k}", color=YELLOW, font_size=42).next_to(eq, DOWN, buff=0.3)

            self.play(FadeIn(center_dot), Write(center_label))
            self.play(Write(eq), Write(k_display))
            self.wait(0.8)

            # Label original
            orig_label = Text(shape_name, font_size=40, color=WHITE).next_to(original, UP)

            self.play(Write(orig_label))

            # Perform the dilation animation
            self.play(
                Transform(original, scaled),
                run_time=run_time,
                rate_func=linear
            )
            self.wait(1)

            # Describe the result
            if k > 1:
                result = "Enlargement"
            elif 0 < k < 1:
                result = "Reduction"
            elif k == 1:
                result = "No change (identity)"
            elif k == 0:
                result = "Collapses to center C"
            elif k < 0 and abs(k) > 1:
                result = "Enlargement + 180° rotation"
            elif k < 0 and abs(k) < 1:
                result = "Reduction + 180° rotation"
            else:
                result = "180° rotation only"

            result_text = Text(f"k = {k} → {result}", font_size=40, color=GREEN)
            result_text.to_edge(DOWN)

            self.play(Write(result_text))
            self.wait(2)

            # Clean up for next example
            self.play(
                FadeOut(original), FadeOut(scaled), FadeOut(orig_label),
                FadeOut(center_dot), FadeOut(center_label),
                FadeOut(eq), FadeOut(k_display), FadeOut(result_text),
                run_time=0.7
            )

        # === Sequence of examples ===

        # 1. Single point
        pt = Dot(axes.c2p(4, 2), color=YELLOW)
        pt_label = Text("Point A", font_size=36).next_to(pt, UR)
        self.play(FadeIn(pt), Write(pt_label))
        self.wait(1)
        self.play(FadeOut(pt_label))
        dilate_shape(pt, axes.c2p(0,0), k=2, shape_name="Original Point")
        self.remove(pt)

        # 3. Square (reduction)
        sq = Square(side_length=2.5, color=PURPLE, fill_opacity=0.6)
        sq.move_to(axes.c2p(3, 1.5))
        self.play(DrawBorderThenFill(sq))
        dilate_shape(sq, axes.c2p(0,0), k=0.4, shape_name="Square")

        # 4. Pentagon (k=1)
        pent = RegularPolygon(5, radius=1.3, color=ORANGE, fill_opacity=0.7)
        pent.move_to(axes.c2p(-3, -1))
        self.play(DrawBorderThenFill(pent))
        dilate_shape(pent, axes.c2p(0,0), k=1, shape_name="Pentagon (k=1)")

        # 5. Star (negative k)
        star = Star(outer_radius=1.5, color=PINK, fill_opacity=0.8)
        star.move_to(axes.c2p(3, -1))
        self.play(DrawBorderThenFill(star))
        dilate_shape(star, axes.c2p(0,0), k=-1.3, shape_name="Star (negative k)")

        # Final summary – why dilations matter
        self.play(FadeOut(grid, axes))

        summary_title = Text("Why Dilations Are Important", font_size=48, color=YELLOW)
        summary_title.to_edge(UP)

        bullets = VGroup(
            Text("• Create similar figures (same shape, different size)", font_size=36),
            Text("• Used in maps, blueprints, and computer graphics", font_size=36),
            Text("• Preserve angles – only size changes (when k > 0)", font_size=36),
            Text("• Negative k adds a 180° rotation", font_size=36),
            Text("• Key to proving triangles or polygons are similar", font_size=36),
            Text("• Foundation of scaling in linear algebra", font_size=36),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(summary_title, DOWN, buff=0.6)

        self.play(Write(summary_title))
        self.play(LaggedStart(*[Write(b) for b in bullets], lag_ratio=0.6))
        self.wait(8)

        closing = Text("Dilations = Controlled Scaling + Similarity", font_size=48, color=GOLD)
        closing.to_edge(DOWN)
        self.play(Write(closing))
        self.wait(3)

        # Fade everything out
        self.play(FadeOut(Group(*self.mobjects)))