from manim import *
import numpy as np

class LogarithmArt(Scene):
    def construct(self):
        # Title
        title = Text("The Power of Logarithmic Scaling", weight=BOLD).scale(0.9)
        self.play(Write(title))
        self.wait(1)
        
        # ============ PART 1: Overwhelming Linear Data ============
        subtitle1 = Text("Original Data (Linear Scale)", font_size=28).next_to(title, DOWN, buff=0.3)
        self.play(Write(subtitle1))
        self.wait(2)
        self.play(FadeOut(title, subtitle1))
        
        # Create linear axes - very tall to show the problem
        linear_axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10000, 2000],
            x_length=7,
            y_length=5,
            axis_config={"include_numbers": False, "include_ticks": True, "stroke_width": 2},
            tips=True,
        ).shift(DOWN*0.5)
        
        # Manual y-axis labels for linear
        y_labels_linear = VGroup()
        for yv in [0, 2000, 4000, 6000, 8000, 10000]:
            lbl = Text(str(yv), font_size=18)
            lbl.next_to(linear_axes.c2p(0, yv), LEFT, buff=0.15)
            y_labels_linear.add(lbl)
        
        # X-axis labels
        x_labels = VGroup()
        for xv in range(1, 11):
            lbl = Text(str(xv), font_size=18)
            lbl.next_to(linear_axes.c2p(xv, 0), DOWN, buff=0.15)
            x_labels.add(lbl)
        
        self.play(Create(linear_axes), FadeIn(y_labels_linear), FadeIn(x_labels))
        
        # Data points with exponential growth (simulating real-world data)
        data_values = [1, 10, 100, 1000, 2000, 3000, 5000, 7000, 8500, 10000]
        
        data_points_linear = VGroup()
        data_labels = VGroup()
        
        for i, val in enumerate(data_values):
            x_pos = i + 1
            point = Dot(linear_axes.c2p(x_pos, val), color=RED, radius=0.08)
            data_points_linear.add(point)
            
            # Add value label
            label = Text(str(val), font_size=14, color=RED)
            label.next_to(point, UP, buff=0.1)
            data_labels.add(label)
        
        self.play(FadeIn(data_points_linear), run_time=2)
        self.play(Write(data_labels), run_time=2)
        self.wait(1)
        
        # Problem annotation
        problem_text = Text(
            "Problem: Small values are invisible!",
            font_size=21,
            color=YELLOW,
            weight=BOLD
        ).to_corner(UR).shift(DOWN*5)
        
        # Highlight the crushed small values
        small_region = Rectangle(
            width=3.5,
            height=0.5,
            color=YELLOW,
            stroke_width=3
        ).move_to(linear_axes.c2p(2.5, 50))
        
        self.play(Create(small_region), Write(problem_text))
        self.wait(2)
        
        # Clear the screen
        self.play(
            FadeOut(linear_axes),
            FadeOut(y_labels_linear),
            FadeOut(x_labels),
            FadeOut(data_points_linear),
            FadeOut(data_labels),
            FadeOut(small_region),
            FadeOut(problem_text),
        )
        self.wait(0.5)
        
        # ============ PART 2: Apply Logarithm ============
        subtitle2 = Text("Apply log10 Transformation", font_size=28).next_to(title, DOWN, buff=0.3)
        self.play(Write(subtitle2))
        
        # Show the transformation
        transform_text = Text("For each value: y_new = log10(y_original)", font_size=22)
        transform_text.next_to(subtitle2, DOWN, buff=0.4)
        self.play(Write(transform_text))
        self.wait(1)
        
        # Show examples of transformation
        examples = VGroup()
        example_pairs = [
            ("1", "0"),
            ("10", "1"),
            ("100", "2"),
            ("1000", "3"),
            ("10000", "4")
        ]
        
        for i, (orig, log_val) in enumerate(example_pairs):
            example = Text(
                f"{orig} → {log_val}",
                font_size=20
            )
            examples.add(example)
        
        examples.arrange(RIGHT, buff=0.4).next_to(transform_text, DOWN, buff=0.3)
        self.play(Write(examples), run_time=2)
        self.wait(2)
        
        self.play(FadeOut(transform_text, examples, subtitle2))
        
        # ============ PART 3: Logarithmic Scale ============
        
        # Create log axes
        log_axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 4.5, 1],
            x_length=7,
            y_length=5,
            axis_config={"include_numbers": False, "include_ticks": True, "stroke_width": 2},
            tips=True,
        ).shift(DOWN*0.5)
        
        # Y-axis labels for log scale
        y_labels_log = VGroup()
        for yv in range(0, 5):
            lbl = Text(str(yv), font_size=18)
            lbl.next_to(log_axes.c2p(0, yv), LEFT, buff=0.15)
            y_labels_log.add(lbl)
        
        # X-axis labels
        x_labels2 = VGroup()
        for xv in range(1, 11):
            lbl = Text(str(xv), font_size=18)
            lbl.next_to(log_axes.c2p(xv, 0), DOWN, buff=0.15)
            x_labels2.add(lbl)
        
        y_axis_label = Text("log10(value)", font_size=20).next_to(log_axes.y_axis, UP, buff=0.2)
        
        self.play(Create(log_axes), FadeIn(y_labels_log), FadeIn(x_labels2), Write(y_axis_label))
        
        # Log-transformed data points
        log_data_values = [np.log10(max(val, 0.1)) for val in data_values]
        
        data_points_log = VGroup()
        
        for i, val in enumerate(log_data_values):
            x_pos = i + 1
            point = Dot(log_axes.c2p(x_pos, val), color=GREEN, radius=0.08)
            data_points_log.add(point)
        
        self.play(FadeIn(data_points_log), run_time=2)
        self.wait(1)
        
        # Show relationships between points
        relationship_text = Text(
            "Each unit up = 10× the original value",
            font_size=24,
            color=YELLOW,
            weight=BOLD
        ).to_corner(UR).shift(DOWN*5)
        self.play(Write(relationship_text))
        
        # Highlight relationships with arrows
        # From log10(1)=0 to log10(10)=1
        arrow1 = Arrow(
            data_points_log[0].get_center(),
            data_points_log[1].get_center(),
            color=YELLOW,
            buff=0.1,
            stroke_width=3
        )
        label1 = Text("10× jump", font_size=16, color=YELLOW).next_to(arrow1, LEFT, buff=0.1)
        
        self.play(Create(arrow1), Write(label1))
        self.wait(1)
        
        # From log10(10)=1 to log10(100)=2
        arrow2 = Arrow(
            data_points_log[1].get_center(),
            data_points_log[2].get_center(),
            color=YELLOW,
            buff=0.1,
            stroke_width=3
        )
        label2 = Text("10× jump", font_size=16, color=YELLOW).next_to(arrow2, LEFT, buff=0.1)
        
        self.play(Create(arrow2), Write(label2))
        self.wait(1)
        
        # From log10(100)=2 to log10(1000)=3
        arrow3 = Arrow(
            data_points_log[2].get_center(),
            data_points_log[3].get_center(),
            color=YELLOW,
            buff=0.1,
            stroke_width=3
        )
        label3 = Text("10× jump", font_size=16, color=YELLOW).next_to(arrow3, LEFT, buff=0.1)
        
        self.play(Create(arrow3), Write(label3))
        self.wait(2)
        
        # Clear arrows
        self.play(
            FadeOut(arrow1), FadeOut(arrow2), FadeOut(arrow3),
            FadeOut(label1), FadeOut(label2), FadeOut(label3),
        )
        
        # ============ PART 4: Show the Logarithmic Curve ============
        curve_text = Text(
            "The pattern follows y = log10(x)",
            font_size=24,
            color=BLUE,
            weight=BOLD
        ).to_corner(UR).shift(DOWN*3)
        self.play(Transform(relationship_text, curve_text))
        
        # Draw the log curve through the points
        log_curve = log_axes.plot(
            lambda x: np.log10(x),
            x_range=[0.1, 10],
            color=BLUE,
            stroke_width=4
        )
        
        curve_label = Text("y = log10(x)", font_size=20, color=BLUE)
        curve_label.next_to(log_axes.c2p(8, np.log10(8)), UR, buff=0.2)
        
        self.play(Create(log_curve), Write(curve_label))
        self.wait(2)
        
        self.play(
            FadeOut(log_axes),
            FadeOut(y_labels_log),
            FadeOut(x_labels2),
            FadeOut(y_axis_label),
            FadeOut(data_points_log),
            FadeOut(log_curve),
            FadeOut(curve_label),
            FadeOut(relationship_text)
        )
        self.wait(1)
        
        # Final explanation
        final_text = Text(
            "Logarithms compress large ranges into manageable scales!",
            font_size=26,
            weight=BOLD
        )
        
        self.play(FadeIn(final_text))
        self.wait(3)