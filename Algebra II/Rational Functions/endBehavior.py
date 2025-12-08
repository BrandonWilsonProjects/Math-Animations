from manim import *
import numpy as np

class RationalFunctionEndBehavior(Scene):
    """Complete demonstration of end behavior for rational functions"""
    def construct(self):
        # INTRO: Title Sequence
        title = Text("End Behavior of Rational Functions", font_size=48, gradient=(BLUE, PURPLE))
        subtitle = Text("Understanding limits as x approaches infinity", font_size=26, color=GRAY).next_to(title, DOWN)
        
        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle, shift=UP))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # PART 1: DEFINITION OF RATIONAL FUNCTION
        definition_title = Text("What is a Rational Function?", font_size=36, color=YELLOW).to_edge(UP)
        self.play(Write(definition_title))
        self.wait(0.5)
        
        # Define rational function
        definition_text = VGroup(
            Text("A rational function has the form:", font_size=28),
            Text("f(x) = P(x) / Q(x)", font_size=32, color=BLUE),
            Text("where P(x) and Q(x) are polynomials", font_size=24, color=GRAY),
            Text("and Q(x) ≠ 0", font_size=24, color=RED)
        ).arrange(DOWN, center=True, buff=0.4).shift(UP * 0.5)
        
        self.play(Write(definition_text), run_time=3, lag_ratio=0.3)
        self.wait(2)
        
        # Example
        example_text = Text("Example: f(x) = (2x² + 3x) / (x² - 1)", font_size=28, color=GREEN).next_to(definition_text, DOWN, buff=0.5)
        self.play(FadeIn(example_text, shift=UP))
        self.wait(2)
        
        self.play(FadeOut(definition_text), FadeOut(example_text))
        
        # PART 2: END BEHAVIOR DEFINITION
        end_behavior_title = Text("What is End Behavior?", font_size=36, color=YELLOW).to_edge(UP)
        self.play(Transform(definition_title, end_behavior_title))
        self.wait(0.5)
        
        end_behavior_def = VGroup(
            Text("End behavior describes what happens", font_size=28),
            Text("to f(x) as x approaches +∞ or -∞", font_size=28),
            Text("Written as:", font_size=24, color=GRAY).shift(DOWN * 0.3),
            Text("lim f(x) as x → +∞", font_size=26, color=BLUE),
            Text("lim f(x) as x → -∞", font_size=26, color=BLUE)
        ).arrange(DOWN, center=True, buff=0.3)
        
        self.play(Write(end_behavior_def), run_time=4, lag_ratio=0.3)
        self.wait(2)
        self.play(FadeOut(end_behavior_def))
        
        # PART 3: THE KEY RULE
        rule_title = Text("The Key Rule", font_size=36, color=YELLOW).to_edge(UP)
        self.play(Transform(definition_title, rule_title))
        self.wait(0.5)
        
        rule_text = VGroup(
            Text("End behavior depends on the", font_size=28),
            Text("DEGREES of the polynomials", font_size=32, color=GREEN, weight=BOLD),
            Text("", font_size=20),
        ).arrange(DOWN, center=True, buff=0.3)
        
        rule_text1 = VGroup(    
            Text("degree of P(x) = n", font_size=26, color=BLUE),
            Text("degree of Q(x) = m", font_size=26, color=RED)
        ).arrange(DOWN, center=True, buff=0.3).shift(DOWN * 3)
        
        self.play(Write(rule_text), run_time=3, lag_ratio=0.3)
        self.play(Write(rule_text1))
        self.wait(2)
        self.play(FadeOut(rule_text, rule_text1))
        
        # CASE 1: n < m (Degree of numerator < denominator)
        case1_title = Text("Case 1: Degree of Top < Degree of Bottom", font_size=32, color=YELLOW).to_edge(UP)
        self.play(Transform(definition_title, case1_title))
        
        # Show the function
        func1_text = Text("f(x) = 3x / (x² + 1)", font_size=32, color=BLUE).to_edge(UP).shift(DOWN * 0.8)
        degree_info1 = VGroup(
            Text("Numerator degree: 1", font_size=24, color=GREEN),
            Text("Denominator degree: 2", font_size=24, color=RED)
        ).arrange(DOWN, buff=0.2).to_corner(UL).shift(DOWN * 0.5)
        
        self.play(Write(func1_text))
        self.play(Write(degree_info1))
        self.wait(1)
        
        # Create axes for graphing
        axes1 = Axes(
            x_range=[-10, 10, 2],
            y_range=[-2, 2, 1],
            x_length=10,
            y_length=5,
            axis_config={"color": GRAY, "include_numbers": True},
            tips=True
        ).scale(0.7).shift(DOWN * 0.5)
        
        axes1_labels = axes1.get_axis_labels(x_label="x", y_label="f(x)")
        
        self.play(Create(axes1), Write(axes1_labels))
        
        # Plot the function
        graph1 = axes1.plot(
            lambda x: 3 * x / (x**2 + 1),
            x_range=[-10, 10],
            color=BLUE,
            use_smoothing=True
        )
        
        self.play(Create(graph1), run_time=2)
        self.wait(1)
        
        # Show horizontal asymptote
        h_asymptote1 = DashedLine(
            axes1.c2p(-10, 0),
            axes1.c2p(10, 0),
            color=YELLOW,
            stroke_width=3
        )
        asymptote_label1 = Text("y = 0", font_size=24, color=YELLOW).next_to(h_asymptote1, RIGHT)
        
        self.play(Create(h_asymptote1), Write(asymptote_label1))
        self.wait(1)
        
        # Conclusion for case 1
        conclusion1 = Text("End behavior: f(x) → 0", font_size=28, color=GREEN).to_corner(UR).shift(DOWN * 0.5)
        self.play(Write(conclusion1))
        self.wait(2)
        
        # Cleanup
        self.play(
            *[FadeOut(mob) for mob in [func1_text, degree_info1, axes1, axes1_labels, 
                                        graph1, h_asymptote1, asymptote_label1, conclusion1]]
        )
        
        # CASE 2: n = m (Degrees are equal)
        case2_title = Text("Case 2: Degree of Top = Degree of Bottom", font_size=32, color=YELLOW).to_edge(UP)
        self.play(Transform(definition_title, case2_title))
        
        # Show the function
        func2_text = Text("f(x) = (2x² + 3) / (x² + 1)", font_size=32, color=BLUE).to_edge(UP).shift(DOWN * 0.8)
        degree_info2 = VGroup(
            Text("Numerator degree: 2", font_size=24, color=GREEN),
            Text("Denominator degree: 2", font_size=24, color=RED),
            Text("", font_size=10)
        ).arrange(DOWN, buff=0.2).to_corner(UL).shift(DOWN * 0.5)
        
        degree_info22 = VGroup(
            Text("Leading coefficients:", font_size=20, color=GRAY).shift(DOWN*3),
            Text("Top: 2, Bottom: 1", font_size=20, color=GRAY).shift(DOWN*4)
        ).arrange(DOWN, buff=0.2).to_corner(UL).shift(DOWN * 4)
        
        self.play(Write(func2_text))
        self.play(Write(degree_info2))
        self.play(Write(degree_info22))
        self.wait(1)
        
        # Create axes
        axes2 = Axes(
            x_range=[-10, 10, 2],
            y_range=[-1, 5, 1],
            x_length=10,
            y_length=5,
            axis_config={"color": GRAY, "include_numbers": True},
            tips=True
        ).scale(0.7).shift(DOWN * 0.5)
        
        axes2_labels = axes2.get_axis_labels(x_label="x", y_label="f(x)")
        
        self.play(Create(axes2), Write(axes2_labels))
        
        # Plot the function
        graph2 = axes2.plot(
            lambda x: (2 * x**2 + 3) / (x**2 + 1),
            x_range=[-10, 10],
            color=BLUE,
            use_smoothing=True
        )
        
        self.play(Create(graph2), run_time=2)
        self.wait(1)
        
        # Show horizontal asymptote at y = 2/1 = 2
        h_asymptote2 = DashedLine(
            axes2.c2p(-10, 2),
            axes2.c2p(10, 2),
            color=YELLOW,
            stroke_width=3
        )
        asymptote_label2 = Text("y = 2", font_size=24, color=YELLOW).next_to(h_asymptote2, RIGHT)
        
        self.play(Create(h_asymptote2), Write(asymptote_label2))
        self.wait(1)
        
        # Conclusion for case 2
        conclusion2 = VGroup(
            Text("End behavior:", font_size=24, color=GREEN),
            Text("f(x) → 2/1 = 2", font_size=24, color=GREEN)
        ).arrange(DOWN, buff=0.2).to_corner(UR).shift(DOWN * 0.5)
        self.play(Write(conclusion2))
        self.wait(2)
        
        # Cleanup
        self.play(
            *[FadeOut(mob) for mob in [func2_text, degree_info2, degree_info22, axes2, axes2_labels, 
                                        graph2, h_asymptote2, asymptote_label2, conclusion2]]
        )
        
        # CASE 3: n > m (Degree of numerator > denominator)
        case3_title = Text("Case 3: Degree of Top > Degree of Bottom", font_size=32, color=YELLOW).to_edge(UP)
        self.play(Transform(definition_title, case3_title))
        
        # Show the function
        func3_text = Text("f(x) = (x³ + 2) / (x + 1)", font_size=32, color=BLUE).to_edge(UP).shift(DOWN * 0.8)
        degree_info3 = VGroup(
            Text("Numerator degree: 3", font_size=24, color=GREEN),
            Text("Denominator degree: 1", font_size=24, color=RED)
        ).arrange(DOWN, buff=0.2).to_corner(UL).shift(DOWN * 0.5)
        
        self.play(Write(func3_text))
        self.play(Write(degree_info3))
        self.wait(1)
        
        # Create axes
        axes3 = Axes(
            x_range=[-5, 5, 1],
            y_range=[-20, 20, 5],
            x_length=10,
            y_length=5,
            axis_config={"color": GRAY, "include_numbers": True},
            tips=True
        ).scale(0.7).shift(DOWN * 0.5)
        
        axes3_labels = axes3.get_axis_labels(x_label="x", y_label="f(x)")
        
        self.play(Create(axes3), Write(axes3_labels))
        
        # Plot the function (avoiding x = -1)
        graph3_left = axes3.plot(
            lambda x: (x**3 + 2) / (x + 1),
            x_range=[-5, -1.2],
            color=BLUE,
            use_smoothing=True
        )
        graph3_right = axes3.plot(
            lambda x: (x**3 + 2) / (x + 1),
            x_range=[-0.8, 5],
            color=BLUE,
            use_smoothing=True
        )
        
        self.play(Create(graph3_left), Create(graph3_right), run_time=2)
        self.wait(1)
        
        # Show vertical asymptote
        v_asymptote = DashedLine(
            axes3.c2p(-1, -20),
            axes3.c2p(-1, 20),
            color=RED,
            stroke_width=3
        )
        v_asymptote_label = Text("x = -1", font_size=20, color=RED).next_to(v_asymptote, UP)
        
        self.play(Create(v_asymptote), Write(v_asymptote_label))
        self.wait(1)
        
        # Conclusion for case 3
        conclusion3 = VGroup(
            Text("End behavior:", font_size=24, color=GREEN),
            Text("f(x) → +∞ as x → +∞", font_size=22, color=GREEN),
            Text("f(x) → -∞ as x → -∞", font_size=22, color=GREEN)
        ).arrange(DOWN, buff=0.2).to_corner(UR).shift(DOWN * 0.5)
        self.play(Write(conclusion3))
        self.wait(2)
        
        # Cleanup
        self.play(
            *[FadeOut(mob) for mob in [func3_text, degree_info3, axes3, axes3_labels, 
                                        graph3_left, graph3_right, v_asymptote, 
                                        v_asymptote_label, conclusion3, definition_title]]
        )
        
        # SUMMARY: All Three Cases
        summary_title = Text("Summary: End Behavior Rules", font_size=40, color=YELLOW).to_edge(UP)
        self.play(Write(summary_title))
        self.wait(0.5)
        
        summary_box = VGroup(
            VGroup(
                Text("Case 1: n < m", font_size=28, color=BLUE, weight=BOLD),
                Text("Horizontal asymptote: y = 0", font_size=24)
            ).arrange(DOWN, buff=0.2),
            
            VGroup(
                Text("Case 2: n = m", font_size=28, color=GREEN, weight=BOLD),
                Text("Horizontal asymptote: y = a/b", font_size=24),
                Text("(ratio of leading coefficients)", font_size=20, color=GRAY)
            ).arrange(DOWN, buff=0.2),
            
            VGroup(
                Text("Case 3: n > m", font_size=28, color=ORANGE, weight=BOLD),
                Text("No horizontal asymptote", font_size=24),
                Text("Function grows without bound", font_size=20, color=GRAY)
            ).arrange(DOWN, buff=0.2)
        ).arrange(DOWN, buff=0.8, aligned_edge=LEFT).shift(DOWN * 0.3)
        
        # Create boxes around each case
        box1 = SurroundingRectangle(summary_box[0], color=BLUE, buff=0.3)
        box2 = SurroundingRectangle(summary_box[1], color=GREEN, buff=0.3)
        box3 = SurroundingRectangle(summary_box[2], color=ORANGE, buff=0.3)
        
        self.play(
            Write(summary_box[0]),
            Create(box1),
            run_time=1.5
        )
        self.wait(1)
        
        self.play(
            Write(summary_box[1]),
            Create(box2),
            run_time=1.5
        )
        self.wait(1)
        
        self.play(
            Write(summary_box[2]),
            Create(box3),
            run_time=1.5
        )
        self.wait(2)
        
        # FINALE
        self.play(
            *[FadeOut(mob) for mob in [summary_title, summary_box, box1, box2, box3]]
        )
        
        finale_text = VGroup(
            Text("End Behavior of Rational Functions", font_size=40, color=BLUE),
            Text("Compare the degrees!", font_size=32, gradient=(PURPLE, PINK))
        ).arrange(DOWN, buff=0.5)
        
        self.play(Write(finale_text[0]), run_time=1.5)
        self.play(FadeIn(finale_text[1], shift=UP))
        self.wait(3)
        self.play(FadeOut(finale_text))