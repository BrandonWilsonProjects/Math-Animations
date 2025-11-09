from manim import *

class ArtOfArithmeticSequence(Scene):
    def construct(self):
        # Title
        title = Text("The Art of Arithmetic Sequences", font_size=50, color=YELLOW).to_edge(UP)
        self.play(Write(title))

        # Formula
        formula = Text("an = a1 + (n - 1) * d", font_size=40, color=BLUE).next_to(title, DOWN)
        self.play(Write(formula))
        self.wait(1)

        # Example values
        a1, d = 2, 3
        example = Text(f"Example: a1 = {a1}, d = {d}", font_size=32, color=WHITE).next_to(formula, DOWN)
        self.play(Write(example))
        self.wait(1)

        # --- Number line view ---
        line_start = LEFT * 5
        line_end = RIGHT * 5
        number_line = Line(line_start, line_end, color=WHITE)
        self.play(Create(number_line))

        # Ticks and labels
        num_ticks = 11
        ticks = VGroup()
        for i in range(num_ticks):
            pos = line_start + (i / (num_ticks - 1)) * (line_end - line_start)
            tick = Line(pos + UP*0.1, pos + DOWN*0.1, color=WHITE)
            value = int(i * 2)
            label = Text(str(value), font_size=20, color=WHITE).next_to(tick, DOWN)
            ticks.add(VGroup(tick, label))
        self.play(LaggedStart(*[Create(t[0]) for t in ticks], *[Write(t[1]) for t in ticks], lag_ratio=0.1))

        # Sequence terms appear with arrows
        terms = VGroup()
        arrows = VGroup()
        d_labels = VGroup()
        for n in range(1, 6):
            an = a1 + (n - 1) * d
            x_pos = line_start + (an / 20) * (line_end - line_start)
            dot = Dot(x_pos, color=RED, radius=0.1)
            label = Text(f"a{n}={an}", font_size=24, color=RED).next_to(dot, UP if n % 2 == 0 else DOWN*3)
            self.play(FadeIn(dot, scale=0.5), Write(label))
            terms.add(dot, label)

            # Show constant step arrow (d)
            if n > 1:
                prev_dot = terms[-4]  # previous dot (every dot+label adds 2, so -4 goes back 1 dot)
                arrow = Arrow(prev_dot.get_center(), dot.get_center(), buff=0.1, color=GREEN)
                d_label = Text(f"+{d}", font_size=20, color=GREEN).next_to(arrow, UP)
                self.play(GrowArrow(arrow), Write(d_label))
                arrows.add(arrow)
                d_labels.add(d_label)

        self.wait(1)

        # --- Transition to graph view ---
        self.play(
            FadeOut(example),
            FadeOut(number_line),
            FadeOut(ticks),
            FadeOut(terms),
            FadeOut(arrows),
            FadeOut(d_labels),
        )
        self.play(formula.animate.to_edge(DOWN*8))

        # Axes for graph
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 20, 2],
            x_length=6,
            y_length=4,
            axis_config={"color": WHITE}
        ).to_edge(DOWN)
        x_label = Text("n", font_size=28).next_to(axes.x_axis.get_end(), DOWN)
        y_label = Text("an", font_size=28).next_to(axes.y_axis.get_end(), LEFT)
        self.play(Create(axes), Write(x_label), Write(y_label))

        # Plot points of the sequence
        graph_points = VGroup()
        for n in range(1, 6):
            an = a1 + (n - 1) * d
            dot = Dot(axes.c2p(n, an), color=RED)
            label = Text(f"({n},{an})", font_size=20, color=RED).next_to(dot, UP if n % 2 == 0 else DOWN)
            self.play(FadeIn(dot), Write(label))
            graph_points.add(dot, label)

        # Connect with a straight line
        seq_line = axes.plot_line_graph(
            x_values=[1, 2, 3, 4, 5],
            y_values=[a1 + (n - 1) * d for n in range(1, 6)],
            line_color=BLUE,
            add_vertex_dots=False
        )
        self.play(Create(seq_line))
        self.wait(1)

        # --- Conclusion ---
        conclusion = Text(
            "Arithmetic Sequences = Constant Growth",
            font_size=36,
            color=YELLOW
        ).next_to(axes, UP*2)
        self.play(Write(conclusion))
        self.wait(2)
