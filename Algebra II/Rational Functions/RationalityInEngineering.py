from manim import *

class RationalEngineering(Scene):
    def construct(self):
        # Title
        title = Text("Rational Functions in Engineering", font_size=48)
        self.play(FadeIn(title))
        self.wait(1.5)
        self.play(title.animate.scale(0.7).to_edge(UP, buff=0.3))
        self.wait(0.5)

        # Explanatory subtitle
        subtitle = Text(
            "Why ratios of quantities describe stability, limits, and system behavior",
            font_size=24, color=GRAY
        ).next_to(title, DOWN, buff=0.2)
        self.play(FadeIn(subtitle, shift=DOWN * 0.3))
        self.wait(2)
        
        # Fade out subtitle before showing plane
        self.play(FadeOut(subtitle))
        self.wait(0.5)

        # Number plane - adjusted positioning
        plane = NumberPlane(
            x_range=[-1, 10, 1],
            y_range=[-5, 15, 1],
            x_length=9,
            y_length=6,
            background_line_style={"stroke_opacity": 0.3}
        ).shift(DOWN * 0.3)
        self.play(Create(plane), run_time=1.5)
        self.wait(0.5)

        # Rational function example for beam deflection
        def func(x):
            if x >= 3.99:
                return None
            return 10 / (4 - x)

        # Vertical asymptote
        asymptote = DashedLine(
            start=plane.c2p(4, -5),
            end=plane.c2p(4, 15),
            color=RED,
            stroke_width=3
        )
        asym_label = Text("System Limit", font_size=24, color=RED)
        asym_label.next_to(plane.c2p(4, 12), RIGHT, buff=0.3)

        self.play(Create(asymptote), run_time=1)
        self.play(Write(asym_label), run_time=0.8)
        self.wait(1)

        # Plot graph with error handling
        try:
            graph = plane.plot(
                func,
                x_range=[-0.5, 3.85, 0.01],
                color=BLUE,
                use_smoothing=True
            )
            graph2 = plane.plot(
                func,
                x_range=[4.15, 9.5, 0.01],
                color=BLUE,
                use_smoothing=True
            )
        except:
            # Fallback if plotting fails
            graph = plane.plot(
                lambda x: 10 / (4 - x),
                x_range=[-0.5, 3.8],
                color=BLUE
            )
            graph2 = VMobject()

        graph_label = Text("Deflection = 10 / (4 - Load)", font_size=22, color=BLUE)
        graph_label.to_edge(DOWN + RIGHT*1.5, buff=3.5)

        self.play(Create(graph), Create(graph2), run_time=2)
        self.play(FadeIn(graph_label, shift=UP * 0.2))
        self.wait(1)

        # Engineering explanation - positioned clearly
        note1 = Text(
            "As load approaches the limit,\ndeflection grows rapidly",
            font_size=24,
            line_spacing=1.2
        ).to_corner(UL, buff=0.5).shift(DOWN * 1.5)
        
        note1_bg = BackgroundRectangle(note1, fill_opacity=0.8, buff=0.2)
        note1_group = VGroup(note1_bg, note1)
        
        self.play(FadeIn(note1_group, shift=RIGHT * 0.3))
        self.wait(1.5)

        # Moving point animation - traces the curve precisely
        dot = Dot(color=YELLOW, radius=0.08)
        dot_label = Text("", font_size=20, color=YELLOW)
        dot_label_bg = BackgroundRectangle(dot_label, fill_opacity=0.85, buff=0.15)
        label_group = VGroup(dot_label_bg, dot_label)

        # Initialize position
        x_start = 0.5
        x_end = 3.75
        
        # Create a ValueTracker to control the x-position
        x_tracker = ValueTracker(x_start)
        
        # Update dot position to always follow the curve
        def update_dot_position(mob):
            x_val = x_tracker.get_value()
            try:
                y_val = func(x_val)
                if y_val is not None:
                    mob.move_to(plane.c2p(x_val, y_val))
            except:
                pass
        
        dot.add_updater(update_dot_position)
        
        # Update label to follow dot
        def update_label(mob):
            try:
                x_val = x_tracker.get_value()
                y_val = func(x_val)
                if y_val is not None:
                    new_label = Text(
                        f"Load: {x_val:.2f}\nDeflection: {y_val:.1f}", 
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
        
        # Animate the x_tracker - dot will follow the curve exactly
        self.play(
            x_tracker.animate.set_value(x_end),
            run_time=7,
            rate_func=smooth
        )
        self.wait(1.5)

        # Clean up
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
            FadeOut(graph),
            FadeOut(graph2),
            FadeOut(asymptote),
            FadeOut(asym_label),
            FadeOut(graph_label),
            run_time=1
        )
        self.wait(0.5)

        # Horizontal asymptote concept
        h_label = Text(
            "Many systems stabilize\nto a steady-state value",
            font_size=24,
            line_spacing=1.2
        ).to_corner(UR, buff=0.5).shift(DOWN * 1.5)
        
        h_label_bg = BackgroundRectangle(h_label, fill_opacity=0.8, buff=0.2)
        h_label_group = VGroup(h_label_bg, h_label)
        
        self.play(FadeIn(h_label_group, shift=LEFT * 0.3))
        self.wait(1)

        # New rational function with horizontal asymptote
        def func2(x):
            if x <= 0:
                return None
            return (5 * x) / (x + 2)

        try:
            graph3 = plane.plot(
                func2,
                x_range=[0.1, 9.5, 0.01],
                color=GREEN,
                use_smoothing=True
            )
        except:
            graph3 = plane.plot(
                lambda x: (5 * x) / (x + 2),
                x_range=[0.1, 9.5],
                color=GREEN
            )

        graph3_label = Text(
            "Response = (5 × input) / (input + 2)",
            font_size=22,
            color=GREEN
        ).to_edge(DOWN + UP*2, buff=3.5)

        self.play(Create(graph3), run_time=2)
        self.play(FadeIn(graph3_label, shift=UP * 0.2))
        self.wait(1)

        # Horizontal asymptote line
        plateau = DashedLine(
            start=plane.c2p(-1, 5),
            end=plane.c2p(10, 5),
            color=GREEN,
            stroke_width=2
        )
        plateau_label = Text("Steady state = 5", font_size=22, color=GREEN)
        plateau_label.next_to(plane.c2p(8, 5), UP, buff=0.2)

        self.play(Create(plateau), run_time=1)
        self.play(Write(plateau_label))
        self.wait(2)

        # Clear everything for final summary
        self.play(
            FadeOut(h_label_group),
            FadeOut(graph3),
            FadeOut(graph3_label),
            FadeOut(plateau),
            FadeOut(plateau_label),
            FadeOut(plane),
            run_time=1.5
        )
        self.wait(0.5)

        # Final summary - centered and clear
        summary = VGroup(
            Text("Rational functions describe:", font_size=32, weight=BOLD),
            Text("Limits and failure points", font_size=26).shift(DOWN * 0.6),
            Text("Stability levels of systems", font_size=26).shift(DOWN * 1.1),
            Text("Ratios of forces, flow, pressure, current", font_size=26).shift(DOWN * 1.6),
            Text("Essential for real engineering models", font_size=28, color=BLUE).shift(DOWN * 2.3)
        ).move_to(ORIGIN)

        self.play(FadeIn(summary, shift=UP * 0.5, lag_ratio=0.2), run_time=2)
        self.wait(3)
        
        self.play(FadeOut(summary), FadeOut(title), run_time=1)
        self.wait(1)