from manim import *

class ScalingSurfaceAreaAndVolume(Scene):
    def construct(self):
        self.show_title()
        self.show_cube_family()
        self.compare_linear_vs_area_vs_volume()
        self.show_the_ratios()
        self.conclusion()

    def show_title(self):
        title = Text("How Surface Area & Volume change when we scale", font_size=42)
        subtitle = Text("Similar shapes • Linear scale factor k", font_size=32, color=BLUE)
        
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        self.play(FadeIn(subtitle.next_to(title, DOWN, buff=0.5)))
        self.wait(1.5)
        self.play(FadeOut(VGroup(title, subtitle)))

    def show_cube_family(self):
        self.scale_factor = ValueTracker(1.0)
        
        def get_cube_group(scale=1.0):
            cube = Cube(side_length=scale, fill_opacity=0.35, stroke_width=2.5)
            label = Integer(
                scale,
                font_size=36,
                color=YELLOW
            ).next_to(cube, DOWN, buff=0.4)
            label.add_updater(lambda m: m.next_to(cube, DOWN, buff=0.4))
            return VGroup(cube, label)

        self.cube1 = always_redraw(lambda: get_cube_group(1.0))
        self.cube2 = always_redraw(lambda: get_cube_group(self.scale_factor.get_value()))
        
        self.play(FadeIn(self.cube1))
        self.wait(0.8)
        
        self.play(self.cube1.animate.shift(LEFT*3.2))
        self.cube2.move_to(RIGHT*3.2)
        self.play(FadeIn(self.cube2))
        self.wait(1)

        scale_label = always_redraw(
            lambda: Text(f"Scale factor = {self.scale_factor.get_value():.1f}×", 
                         font_size=36, color=YELLOW)
            .to_edge(UP, buff=1.2)
        )
        self.add(scale_label)

    def compare_linear_vs_area_vs_volume(self):
        # Prepare comparison texts
        linear   = Text("Length",   font_size=38).shift(UP*2.0 + LEFT*3.8)
        area     = Text("Area",     font_size=38).next_to(linear, DOWN, buff=0.9)
        volume   = Text("Volume",   font_size=38).next_to(area,   DOWN, buff=0.9)

        arrow1 = Arrow(LEFT*1.8, RIGHT*1.8, buff=0.2, color=BLUE, stroke_width=6)
        arrow2 = arrow1.copy().shift(DOWN*0.9)
        arrow3 = arrow1.copy().shift(DOWN*1.8)

        self.play(
            FadeIn(linear, area, volume),
            GrowArrow(arrow1), GrowArrow(arrow2), GrowArrow(arrow3)
        )
        self.wait(0.8)

        # Show multipliers
        k   = always_redraw(lambda: MathTex("k",   font_size=54).next_to(arrow1.get_tip(), UP, buff=0.2))
        k2  = always_redraw(lambda: MathTex("k^2", font_size=54).next_to(arrow2.get_tip(), UP, buff=0.2))
        k3  = always_redraw(lambda: MathTex("k^3", font_size=54).next_to(arrow3.get_tip(), UP, buff=0.2))

        self.play(Write(k), Write(k2), Write(k3))
        self.wait(1.5)

        self.group_labels = VGroup(linear, area, volume, arrow1, arrow2, arrow3, k, k2, k3)

    def show_the_ratios(self):
        formulas = VGroup(
            MathTex(r"\text{Length:} \quad \ell' = k \cdot \ell", font_size=42),
            MathTex(r"\text{Surface area:} \quad A' = k^2 \cdot A", font_size=42),
            MathTex(r"\text{Volume:} \quad V' = k^3 \cdot V", font_size=42),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.7).shift(UP*0.5)

        for formula in formulas:
            self.play(Write(formula))
            self.wait(1.2)

        self.formulas = formulas

        # Animate scaling and show numbers
        self.play(
            self.scale_factor.animate.set_value(2.0),
            run_time=3,
            rate_func=linear
        )
        self.wait(1.5)

        self.play(
            self.scale_factor.animate.set_value(0.5),
            run_time=3,
            rate_func=linear
        )
        self.wait(1.5)

        self.play(
            self.scale_factor.animate.set_value(3.0),
            run_time=4,
            rate_func=linear
        )
        self.wait(2)

    def conclusion(self):
        final_text = VGroup(
            Text("Key idea:", font_size=48, color=YELLOW),
            Text("When linear dimensions scale by k,", font_size=38),
            Text("→ areas grow by k²", font_size=38, color=BLUE),
            Text("→ volumes grow by k³", font_size=38, color=RED),
        ).arrange(DOWN, buff=0.45, aligned_edge=LEFT).move_to(ORIGIN)

        self.play(
            FadeOut(self.cube1),
            FadeOut(self.cube2),
            FadeOut(self.group_labels),
            FadeOut(self.formulas),
            run_time=1.2
        )

        for line in final_text:
            self.play(Write(line), run_time=1.2)
            self.wait(0.9)

        self.wait(3)