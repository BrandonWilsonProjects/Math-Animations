from manim import *

class RationalMedicine(Scene):
    def construct(self):
        # Title
        title = Text("Rational Functions in Medicine", font_size=48)
        self.play(FadeIn(title))
        self.wait(1.5)
        self.play(title.animate.scale(0.7).to_edge(UP, buff=0.3))
        self.wait(0.5)

        # Explanatory subtitle
        subtitle = Text(
            "How drug dosing, enzyme kinetics, and patient response are modeled",
            font_size=24, color=GRAY
        ).next_to(title, DOWN, buff=0.2)
        self.play(FadeIn(subtitle, shift=DOWN * 0.3))
        self.wait(2)
        
        # Fade out subtitle before showing plane
        self.play(FadeOut(subtitle))
        self.wait(0.5)

        # Number plane for drug concentration over time
        plane = NumberPlane(
            x_range=[0, 24, 2],
            y_range=[0, 10, 1],
            x_length=9,
            y_length=6,
            background_line_style={"stroke_opacity": 0.3},
            axis_config={"include_numbers": False}
        ).shift(DOWN * 0.3)
        
        # Axis labels
        x_label = Text("Time (hours)", font_size=20).next_to(plane, DOWN, buff=0.2)
        y_label = Text("Drug Concentration", font_size=20).next_to(plane, LEFT, buff=0.3).rotate(PI/2)
        
        self.play(Create(plane), run_time=1.5)
        self.play(FadeIn(x_label), FadeIn(y_label))
        self.wait(0.5)

        # Drug elimination model: C(t) = 100 / (t + 10)
        # Shows how drug concentration decreases over time
        def drug_decay(t):
            if t < 0:
                return None
            return 100 / (t + 10)

        # Therapeutic range lines
        therapeutic_max = Line(
            start=plane.c2p(0, 8),
            end=plane.c2p(24, 8),
            color=RED,
            stroke_width=2
        )
        therapeutic_min = Line(
            start=plane.c2p(0, 3),
            end=plane.c2p(24, 3),
            color=ORANGE,
            stroke_width=2
        )
        
        max_label = Text("Toxic Level", font_size=20, color=RED)
        max_label.next_to(plane.c2p(22, 8), UP, buff=0.1)
        min_label = Text("Minimum Effective", font_size=20, color=ORANGE)
        min_label.next_to(plane.c2p(20, 3), DOWN, buff=0.1)

        self.play(Create(therapeutic_max), Create(therapeutic_min), run_time=1)
        self.play(Write(max_label), Write(min_label))
        self.wait(1)

        # Plot drug concentration curve
        try:
            drug_curve = plane.plot(
                drug_decay,
                x_range=[0, 24, 0.1],
                color=BLUE,
                use_smoothing=True
            )
        except:
            drug_curve = plane.plot(
                lambda t: 100 / (t + 10),
                x_range=[0, 24],
                color=BLUE
            )

        curve_label = Text("Drug Concentration = 100 / (t + 10)", font_size=22, color=BLUE)
        curve_label.to_edge(DOWN, buff=3.5)

        self.play(Create(drug_curve), run_time=2)
        self.play(FadeIn(curve_label, shift=UP * 0.2))
        self.wait(1)

        # Explanation
        note1 = Text(
            "Drug levels must stay\nwithin therapeutic window",
            font_size=24,
            line_spacing=1.2
        ).to_corner(UL, buff=0.5).shift(DOWN * 1.5)
        
        note1_bg = BackgroundRectangle(note1, fill_opacity=0.8, buff=0.2)
        note1_group = VGroup(note1_bg, note1)
        
        self.play(FadeIn(note1_group, shift=RIGHT * 0.3))
        self.wait(1.5)

        # Moving point showing drug concentration over time
        dot = Dot(color=YELLOW, radius=0.08)
        dot_label = Text("", font_size=20, color=YELLOW)
        dot_label_bg = BackgroundRectangle(dot_label, fill_opacity=0.85, buff=0.15)
        label_group = VGroup(dot_label_bg, dot_label)

        # Initialize position
        t_start = 0
        t_end = 22
        
        # Create a ValueTracker to control the time
        t_tracker = ValueTracker(t_start)
        
        # Update dot position to always follow the curve
        def update_dot_position(mob):
            t_val = t_tracker.get_value()
            try:
                c_val = drug_decay(t_val)
                if c_val is not None:
                    mob.move_to(plane.c2p(t_val, c_val))
            except:
                pass
        
        dot.add_updater(update_dot_position)
        
        # Update label to follow dot
        def update_label(mob):
            try:
                t_val = t_tracker.get_value()
                c_val = drug_decay(t_val)
                if c_val is not None:
                    new_label = Text(
                        f"Time: {t_val:.1f}h\nLevel: {c_val:.1f}", 
                        font_size=20, 
                        color=YELLOW,
                        line_spacing=1
                    )
                    new_bg = BackgroundRectangle(new_label, fill_opacity=0.85, buff=0.15)
                    mob.become(VGroup(new_bg, new_label))
                    mob.next_to(dot, UR, buff=0.15)
            except:
                pass

        label_group.add_updater(update_label)
        
        self.add(dot, label_group)
        
        # Animate the tracker - dot will follow the curve exactly
        self.play(
            t_tracker.animate.set_value(t_end),
            run_time=7,
            rate_func=smooth
        )
        self.wait(1.5)

        # Clean up
        dot.remove_updater(update_dot_position)
        label_group.remove_updater(update_label)
        self.play(
            FadeOut(dot), 
            FadeOut(label_group),
            FadeOut(note1_group),
            run_time=0.8
        )
        self.wait(0.5)

        # Transition: fade out first graph
        self.play(
            FadeOut(drug_curve),
            FadeOut(therapeutic_max),
            FadeOut(therapeutic_min),
            FadeOut(max_label),
            FadeOut(min_label),
            FadeOut(curve_label),
            FadeOut(x_label),
            FadeOut(y_label),
            run_time=1
        )
        self.wait(0.5)

        # New plane for enzyme kinetics (Michaelis-Menten)
        plane2 = NumberPlane(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            x_length=9,
            y_length=6,
            background_line_style={"stroke_opacity": 0.3},
            axis_config={"include_numbers": False}
        ).shift(DOWN * 0.3)
        
        x_label2 = Text("Substrate Concentration", font_size=20).next_to(plane2, DOWN, buff=0.2)
        y_label2 = Text("Reaction Rate", font_size=20).next_to(plane2, LEFT, buff=0.3).rotate(PI/2)
        
        self.play(FadeOut(plane), Create(plane2), run_time=1)
        self.play(FadeIn(x_label2), FadeIn(y_label2))
        self.wait(0.5)

        # Enzyme kinetics explanation
        h_label = Text(
            "Enzyme reactions saturate\nat maximum velocity",
            font_size=24,
            line_spacing=1.2
        ).to_corner(UR, buff=0.5).shift(DOWN * 1.5)
        
        h_label_bg = BackgroundRectangle(h_label, fill_opacity=0.8, buff=0.2)
        h_label_group = VGroup(h_label_bg, h_label)
        
        self.play(FadeIn(h_label_group, shift=LEFT * 0.3))
        self.wait(1)

        # Michaelis-Menten equation: v = (Vmax × S) / (Km + S)
        # Vmax = 8, Km = 2
        def michaelis_menten(s):
            if s < 0:
                return None
            vmax = 8
            km = 2
            return (vmax * s) / (km + s)

        try:
            enzyme_curve = plane2.plot(
                michaelis_menten,
                x_range=[0, 10, 0.05],
                color=GREEN,
                use_smoothing=True
            )
        except:
            enzyme_curve = plane2.plot(
                lambda s: (8 * s) / (2 + s),
                x_range=[0, 10],
                color=GREEN
            )

        enzyme_label = Text(
            "Reaction Rate = (Vmax × S) / (Km + S)",
            font_size=22,
            color=GREEN
        ).to_edge(DOWN, buff=3.5)

        self.play(Create(enzyme_curve), run_time=2)
        self.play(FadeIn(enzyme_label, shift=UP * 0.2))
        self.wait(1)

        # Maximum velocity line
        vmax_line = DashedLine(
            start=plane2.c2p(0, 8),
            end=plane2.c2p(10, 8),
            color=GREEN,
            stroke_width=2
        )
        vmax_label = Text("Vmax = 8", font_size=22, color=GREEN)
        vmax_label.next_to(plane2.c2p(8.5, 8), UP, buff=0.2)

        self.play(Create(vmax_line), run_time=1)
        self.play(Write(vmax_label))
        self.wait(1)

        # Km indicator
        km_line = DashedLine(
            start=plane2.c2p(2, 0),
            end=plane2.c2p(2, 4),
            color=YELLOW,
            stroke_width=2
        )
        km_label = Text("Km", font_size=22, color=YELLOW)
        km_label.next_to(plane2.c2p(2, 0), DOWN, buff=0.2)
        
        km_point = Dot(plane2.c2p(2, 4), color=YELLOW, radius=0.1)

        self.play(Create(km_line), Write(km_label))
        self.play(FadeIn(km_point, scale=1.5))
        self.wait(2)

        # Clear everything for final summary
        self.play(
            FadeOut(h_label_group),
            FadeOut(enzyme_curve),
            FadeOut(enzyme_label),
            FadeOut(vmax_line),
            FadeOut(vmax_label),
            FadeOut(km_line),
            FadeOut(km_label),
            FadeOut(km_point),
            FadeOut(plane2),
            FadeOut(x_label2),
            FadeOut(y_label2),
            run_time=1.5
        )
        self.wait(0.5)

        # Final summary - centered and clear
        summary = VGroup(
            Text("Rational functions in medicine:", font_size=32, weight=BOLD),
            Text("Drug dosing and elimination rates", font_size=26).shift(DOWN * 0.6),
            Text("Enzyme kinetics (Michaelis-Menten)", font_size=26).shift(DOWN * 1.1),
            Text("Oxygen binding to hemoglobin", font_size=26).shift(DOWN * 1.6),
            Text("Pharmacokinetics and drug interactions", font_size=26).shift(DOWN * 2.1),
            Text("Critical for safe and effective treatment", font_size=28, color=BLUE).shift(DOWN * 2.8)
        ).move_to(ORIGIN)

        self.play(FadeIn(summary, shift=UP * 0.5, lag_ratio=0.2), run_time=2)
        self.wait(3)
        
        self.play(FadeOut(summary), FadeOut(title), run_time=1)
        self.wait(1)