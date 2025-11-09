from manim import *

class MeanMedianMode_NoLatex(Scene):
    def construct(self):
        # Data
        data_values = [2, 3, 3, 4, 6, 7, 8]
        min_val, max_val = 0, 10

        # Draw manual axis line
        axis = Line(LEFT * 5, RIGHT * 5, color=WHITE)
        self.play(Create(axis))

        # Create number labels using Text only
        tick_marks = VGroup()
        for x in range(min_val, max_val + 1):
            pos = interpolate(LEFT * 5, RIGHT * 5, (x - min_val) / (max_val - min_val))
            tick = Line(pos + DOWN * 0.1, pos + UP * 0.1, color=WHITE)
            label = Text(str(x), font_size=20).next_to(tick, DOWN, buff=0.15)
            tick_marks.add(tick, label)

        self.play(*[Create(obj) for obj in tick_marks])
        self.wait(0.5)

        # Helper to get position of any x-value on line
        def get_pos(x):
            alpha = (x - min_val) / (max_val - min_val)
            return interpolate(LEFT * 5, RIGHT * 5, alpha)

        # Plot data points
        data_dots = VGroup()
        for val in data_values:
            dot = Dot(get_pos(val), color=WHITE)
            data_dots.add(dot)
        self.play(*[FadeIn(dot) for dot in data_dots])
        self.wait(0.5)

        # Compute stats
        mean = sum(data_values) / len(data_values)
        median = sorted(data_values)[len(data_values) // 2]
        mode = max(set(data_values), key=data_values.count)

        # Markers for stats
        mean_marker = Triangle().scale(0.2).rotate(PI).set_color(BLUE).move_to(get_pos(mean) + DOWN * 0.3).shift(RIGHT * 0.3)
        mean_label = Text("Mean", font_size=16, color=BLUE).next_to(mean_marker, DOWN)

        median_marker = Square(0.2, color=RED, fill_opacity=1).move_to(get_pos(median) + DOWN * 0.3)
        median_label = Text("Median", font_size=16, color=RED).next_to(median_marker, DOWN)

        mode_marker = Circle(radius=0.1, color=GREEN, fill_opacity=1).move_to(get_pos(mode) + DOWN * 0.3)
        mode_label = Text("Mode", font_size=16, color=GREEN).next_to(mode_marker, DOWN)

        self.play(
            GrowFromCenter(mean_marker), Write(mean_label),
            GrowFromCenter(median_marker), Write(median_label),
            GrowFromCenter(mode_marker), Write(mode_label),
        )
        self.wait(1)

        # Explanation
        explanation = Text(
            "Mean = average   •   Median = middle   •   Mode = most frequent",
            font_size=28
        ).to_edge(DOWN)

        self.play(Write(explanation))
        self.wait(3)
