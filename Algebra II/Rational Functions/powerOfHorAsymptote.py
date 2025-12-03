from manim import *

class HorizontalAsymptotesIntricate(Scene):
    def construct(self):
        # Title sequence
        title = Text("Horizontal Asymptotes", font_size=48, gradient=(BLUE, GREEN))
        subtitle = Text("An Intricate Exploration", font_size=28).next_to(title, DOWN)
        self.play(Write(title), FadeIn(subtitle, shift=UP))
        self.wait()
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # Part 1: Basic Definition
        self.show_definition()
        self.wait()
        
        # Part 2: Simple Example
        self.simple_example()
        self.wait()
        
        # Part 3: Multiple Asymptotes
        self.multiple_asymptotes()
        self.wait()
        
        # Part 4: Degree Analysis
        self.degree_analysis()
        self.wait()

    def show_definition(self):
        """Display the formal definition of horizontal asymptotes"""
        def_title = Text("Definition", font_size=36, color=YELLOW).to_edge(UP)
        
        definition = Text(
            "A line y = L is a horizontal asymptote if:",
            font_size=28
        ).next_to(def_title, DOWN, buff=0.5)
        
        limit_left = Text(
            "lim(x→-∞) f(x) = L",
            font_size=32,
            color=BLUE
        ).next_to(definition, DOWN, buff=0.7)
        
        or_text = Text("or", font_size=28).next_to(limit_left, DOWN, buff=0.3)
        
        limit_right = Text(
            "lim(x→+∞) f(x) = L",
            font_size=32,
            color=GREEN
        ).next_to(or_text, DOWN, buff=0.3)
        
        self.play(Write(def_title))
        self.play(FadeIn(definition))
        self.wait()
        self.play(Write(limit_left))
        self.wait(0.5)
        self.play(FadeIn(or_text))
        self.wait(0.5)
        self.play(Write(limit_right))
        self.wait(9)
        self.play(FadeOut(def_title, definition, limit_left, or_text, limit_right))

    def simple_example(self):
        """Show a basic rational function with horizontal asymptote"""
        title = Text("Example 1: Basic Rational Function", font_size=32).to_edge(UP)
        
        # Function expression
        func_tex = Text(
            "f(x) = (2x² + 3x - 1) / (x² + 1)",
            font_size=32
        ).next_to(title, DOWN)
        
        self.play(Write(title), Write(func_tex))
        self.wait()
        
        # Create axes
        axes = Axes(
            x_range=[-10, 10, 2],
            y_range=[-1, 4, 1],
            x_length=10,
            y_length=5,
            axis_config={"include_tip": True, "include_numbers": True}
        ).shift(DOWN * 0.5)
        
        # Function plot
        graph = axes.plot(
            lambda x: (2*x**2 + 3*x - 1)/(x**2 + 1),
            color=BLUE,
            x_range=[-10, 10],
            use_smoothing=True
        )
        
        # Horizontal asymptote y = 2
        h_asymptote = axes.plot(lambda x: 2, color=RED, x_range=[-10, 10])
        asymptote_label = Text("y = 2", color=RED, font_size=28).next_to(axes.c2p(8, 3), UR)
        
        self.play(Create(axes))
        self.play(Create(graph), run_time=2)
        self.wait()
        self.play(Create(h_asymptote), Write(asymptote_label))
        
        # Show behavior at infinity
        arrow_left = Arrow(
            axes.c2p(-8, 1.5), axes.c2p(-8, 2),
            color=YELLOW, buff=0.1
        )
        arrow_right = Arrow(
            axes.c2p(8, 1.5), axes.c2p(8, 2),
            color=YELLOW, buff=0.1
        )
        
        left_label = Text("Approaches 2\nas x→-∞", font_size=20, color=YELLOW).next_to(arrow_left, LEFT + UP*1.5)
        right_label = Text("Approaches 2\nas x→+∞", font_size=20, color=YELLOW).next_to(arrow_right, RIGHT + DOWN*1.5)
        
        self.play(GrowArrow(arrow_left), GrowArrow(arrow_right))
        self.play(Write(left_label), Write(right_label))
        self.wait(2)
        self.play(FadeOut(title, func_tex, axes, graph, h_asymptote, 
                          asymptote_label, arrow_left, arrow_right, left_label, right_label))

    def multiple_asymptotes(self):
        """Show a function with two different horizontal asymptotes"""
        title = Text("Example 2: Different Asymptotes at ±∞", font_size=32).to_edge(UP)
        
        func_tex = Text(
            "f(x) = (3x² + x) / (|x|(x + 1))",
            font_size=30
        ).next_to(title, DOWN)
        
        self.play(Write(title), Write(func_tex))
        self.wait()
        
        axes = Axes(
            x_range=[-10, 10, 2],
            y_range=[-5, 5, 1],
            x_length=10,
            y_length=5,
            axis_config={"include_tip": True, "include_numbers": True}
        ).shift(DOWN * 0.5)
        
        # Plot function with different behavior at +/- infinity
        def complex_func(x):
            if abs(x) < 0.1 or abs(x + 1) < 0.1:
                return 0
            return (3*x**2 + x) / (abs(x) * (x + 1))
        
        graph = axes.plot(
            complex_func,
            color=PURPLE,
            x_range=[-10, -0.2],
            discontinuities=[-1],
            use_smoothing=True
        )
        
        graph2 = axes.plot(
            complex_func,
            color=PURPLE,
            x_range=[0.2, 10],
            discontinuities=[-1],
            use_smoothing=True
        )
        
        # Different horizontal asymptotes
        h_asymptote_left = axes.plot(lambda x: -3, color=RED, x_range=[-10, -1])
        h_asymptote_right = axes.plot(lambda x: 3, color=GREEN, x_range=[0, 10])
        
        label_left = Text("y = -3", color=RED, font_size=28).next_to(axes.c2p(-8, -3), DOWN)
        label_right = Text("y = 3", color=GREEN, font_size=28).next_to(axes.c2p(8, 3), UP)
        
        self.play(Create(axes))
        self.play(Create(graph), Create(graph2), run_time=2)
        self.wait()
        self.play(
            Create(h_asymptote_left), Write(label_left),
            Create(h_asymptote_right), Write(label_right)
        )
        
        # Annotate the limits
        limit_left_text = Text(
            "As x→-∞: f(x)→-3",
            font_size=24,
            color=RED
        ).to_corner(DL)
        
        limit_right_text = Text(
            "As x→+∞: f(x)→3",
            font_size=24,
            color=GREEN
        ).next_to(limit_left_text, UP)
        
        self.play(Write(limit_left_text), Write(limit_right_text))
        self.wait(2)
        self.play(
            FadeOut(title), FadeOut(func_tex), FadeOut(axes), 
            FadeOut(graph), FadeOut(graph2), FadeOut(h_asymptote_left),
            FadeOut(h_asymptote_right), FadeOut(label_left), FadeOut(label_right),
            FadeOut(limit_left_text), FadeOut(limit_right_text)
        )

    def degree_analysis(self):
        """Show how degree of numerator vs denominator affects horizontal asymptotes"""
        title = Text("Degree Analysis for Rational Functions", font_size=32).to_edge(UP)
        self.play(Write(title))
        self.wait(3)
        self.play(FadeOut(title))
        
        # Create three cases
        case1_title = Text("Case 1: n > m", font_size=28).shift(UP * 1.8 + LEFT * 3.5)
        case1_ex = Text("(3x + 2) / (x² + 1) → 0", font_size=24).next_to(case1_title, DOWN)
        case1_result = Text("y = 0", color=YELLOW, font_size=24).next_to(case1_ex, DOWN)
        case1 = VGroup(case1_title, case1_ex, case1_result)
        
        case2_title = Text("Case 2: m = m", font_size=28).shift(UP * 1.8 + RIGHT * 3.5)
        case2_ex = Text("(3x² + 2) / (2x² + 1) → 3/2", font_size=24).next_to(case2_title, DOWN)
        case2_result = Text("y = 3/2", color=YELLOW, font_size=24).next_to(case2_ex, DOWN)
        case2 = VGroup(case2_title, case2_ex, case2_result)
        
        case3_title = Text("Case 3: m > n", font_size=28).shift(DOWN * 0.8)
        case3_ex = Text("(x³ + 2) / (x² + 1) → ±∞", font_size=24).next_to(case3_title, DOWN)
        case3_result = Text("No Horizontal Asymptote", color=RED, font_size=24).next_to(case3_ex, DOWN)
        case3 = VGroup(case3_title, case3_ex, case3_result)
        
        self.play(FadeIn(case1, shift=RIGHT))
        self.wait()
        self.play(FadeIn(case2, shift=LEFT))
        self.wait()
        self.play(FadeIn(case3, shift=UP))
        self.wait(10)
        
        # Visual demonstration
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-2, 3, 1],
            x_length=6,
            y_length=4,
            axis_config={"include_tip": True}
        ).shift(DOWN * 0.8).scale(0.7)
        
        self.play(
            FadeOut(case1, case2, case3),
            Create(axes)
        )
        
        # Case 1: deg(P) < deg(Q)
        case1_label = Text("Case 1: n > m", font_size=32, color=BLUE).to_edge(UP).shift(DOWN * 0.3)
        case1_func = Text("(3x + 2) / (x² + 1)", font_size=28, color=BLUE).next_to(case1_label, DOWN, buff=0.2)
        
        self.play(Write(case1_label), Write(case1_func))
        self.wait()
        
        axes_case1 = Axes(
            x_range=[-5, 5, 1],
            y_range=[-2, 3, 1],
            x_length=9,
            y_length=5.5,
            axis_config={"include_tip": True, "include_numbers": True}
        ).shift(DOWN * 1)
        
        self.play(Transform(axes, axes_case1))
        
        g1 = axes_case1.plot(lambda x: (3*x + 2)/(x**2 + 1), color=BLUE, x_range=[-5, 5], stroke_width=6)
        h1 = axes_case1.plot(lambda x: 0, color=YELLOW, stroke_width=5, x_range=[-5, 5])
        h1_label = Text("y = 0", font_size=28, color=YELLOW).next_to(axes_case1.c2p(4, 0), DOWN*1.2)
        
        self.play(Create(h1), Write(h1_label))
        self.wait(0.5)
        self.play(Create(g1), run_time=2)
        self.wait(2)
        
        # Highlight convergence
        arrow1_left = Arrow(axes_case1.c2p(-4, 0.3), axes_case1.c2p(-4, 0.05), color=YELLOW, buff=0.1, stroke_width=6)
        arrow1_right = Arrow(axes_case1.c2p(4, 0.3), axes_case1.c2p(4, 0.05), color=YELLOW, buff=0.1, stroke_width=6)
        self.play(GrowArrow(arrow1_left), GrowArrow(arrow1_right))
        self.wait(2)
        
        self.play(
            FadeOut(g1), FadeOut(h1), FadeOut(h1_label), 
            FadeOut(case1_label), FadeOut(case1_func),
            FadeOut(arrow1_left), FadeOut(arrow1_right)
        )
        self.wait(0.5)
        
        # Case 2: deg(P) = deg(Q)
        case2_label = Text("Case 2: m = n", font_size=32, color=GREEN).to_edge(UP).shift(DOWN * 0.3)
        case2_func = Text("(3x² + 2) / (2x² + 1)", font_size=28, color=GREEN).next_to(case2_label, DOWN, buff=0.2)
        
        self.play(Write(case2_label), Write(case2_func))
        self.wait()
        
        axes_case2 = Axes(
            x_range=[-5, 5, 1],
            y_range=[-2, 3, 1],
            x_length=9,
            y_length=5.5,
            axis_config={"include_tip": True, "include_numbers": True}
        ).shift(DOWN * 1)
        
        self.play(Transform(axes, axes_case2))
        
        g2 = axes_case2.plot(lambda x: (3*x**2 + 2)/(2*x**2 + 1), color=GREEN, x_range=[-5, 5], stroke_width=6)
        h2 = axes_case2.plot(lambda x: 1.5, color=YELLOW, stroke_width=5, x_range=[-5, 5])
        h2_label = Text("y = 1.5", font_size=28, color=YELLOW).next_to(axes_case2.c2p(4, 1.5), UP)
        
        self.play(Create(h2), Write(h2_label))
        self.wait(0.5)
        self.play(Create(g2), run_time=2)
        self.wait(2)
        
        # Highlight convergence
        arrow2_left = Arrow(axes_case2.c2p(-4, 1.7), axes_case2.c2p(-4, 1.55), color=YELLOW, buff=0.1, stroke_width=6)
        arrow2_right = Arrow(axes_case2.c2p(4, 1.7), axes_case2.c2p(4, 1.55), color=YELLOW, buff=0.1, stroke_width=6)
        self.play(GrowArrow(arrow2_left), GrowArrow(arrow2_right))
        self.wait(2)
        
        self.play(
            FadeOut(g2), FadeOut(h2), FadeOut(h2_label),
            FadeOut(case2_label), FadeOut(case2_func),
            FadeOut(arrow2_left), FadeOut(arrow2_right)
        )
        self.wait(0.5)
        
        # Case 3: deg(P) > deg(Q) - Show it grows without bound
        case3_label = Text("Case 3: m > n", font_size=32, color=RED).to_edge(UP).shift(DOWN * 0.3)
        case3_func = Text("(x³) / (x² + 1)", font_size=28, color=RED).next_to(case3_label, DOWN, buff=0.2)
        case3_note = Text("No Horizontal Asymptote!", font_size=26, color=YELLOW).next_to(case3_func, DOWN, buff=0.2)
        
        self.play(Write(case3_label), Write(case3_func))
        self.wait()
        
        # Adjusted axes for case 3 to show growth
        axes_case3 = Axes(
            x_range=[-3, 3, 1],
            y_range=[-10, 10, 5],
            x_length=9,
            y_length=5.5,
            axis_config={"include_tip": True, "include_numbers": True}
        ).shift(DOWN * 1)
        
        self.play(Transform(axes, axes_case3))
        
        g3 = axes_case3.plot(lambda x: x**3/(x**2 + 1), color=RED, x_range=[-2.8, 2.8], stroke_width=6)
        
        self.play(Create(g3), run_time=2)
        self.wait()
        self.play(Write(case3_note))
        
        # Show arrows pointing to infinity
        arrow3_up = Arrow(axes_case3.c2p(2, 3), axes_case3.c2p(2, 6), color=YELLOW, buff=0.1, stroke_width=6)
        arrow3_down = Arrow(axes_case3.c2p(-2, -3), axes_case3.c2p(-2, -6), color=YELLOW, buff=0.1, stroke_width=6)
        infinity_text = Text("→ ±∞", font_size=24, color=YELLOW).next_to(axes_case3, RIGHT)
        
        self.play(GrowArrow(arrow3_up), GrowArrow(arrow3_down), Write(infinity_text))
        self.wait(2)
        
        self.play(
            FadeOut(axes), FadeOut(g3),
            FadeOut(case3_label), FadeOut(case3_func), FadeOut(case3_note),
            FadeOut(arrow3_up), FadeOut(arrow3_down), FadeOut(infinity_text)
        )
        
        # Final summary
        summary_title = Text("Summary", font_size=40, color=GOLD).shift(UP * 2)
        summary_points = VGroup(
            Text("• Horizontal asymptotes describe end behavior", font_size=24),
            Text("• Can have 0, 1, or 2 horizontal asymptotes", font_size=24),
            Text("• Degree of rational functions determines existence", font_size=24),
            Text("• Functions can cross horizontal asymptotes", font_size=24),
            Text("• Oscillating functions can still approach asymptotes", font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).next_to(summary_title, DOWN, buff=0.7)
        
        self.play(Write(summary_title))
        self.play(FadeIn(summary_points, lag_ratio=0.3))
        self.wait(3)