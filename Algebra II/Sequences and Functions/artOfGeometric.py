from manim import *

class GeometricSequence25Spread(Scene):
    def construct(self):
        # Title
        title = Text("Geometric Sequence: 25 * 5^n", font_size=46, color=YELLOW).to_edge(UP)
        self.play(Write(title))

        # Formula
        formula = Text("an = 25 * 5^n", font_size=38, color=BLUE).next_to(title, DOWN)
        self.play(Write(formula))

        # Example
        a1, r = 25, 5
        example = Text(f"Example: a1 = {a1}, r = {r}", font_size=28, color=WHITE).next_to(formula, DOWN)
        self.play(Write(example))
        self.wait(1)

        # --- Custom number line ---
        line_start = LEFT * 5
        line_end = RIGHT * 5
        number_line = Line(line_start, line_end, color=WHITE)
        self.play(Create(number_line))

        # Add ticks for "steps" (not scaled by value, just evenly spaced)
        num_terms = 5
        ticks = VGroup()
        for n in range(num_terms):
            pos = line_start + (n / (num_terms - 1)) * (line_end - line_start)
            tick = Line(pos + UP*0.1, pos + DOWN*0.1, color=WHITE)
            label = Text(f"n={n}", font_size=20, color=WHITE).next_to(tick, DOWN)
            ticks.add(VGroup(tick, label))
        self.play(LaggedStart(*[Create(t[0]) for t in ticks], *[Write(t[1]) for t in ticks], lag_ratio=0.1))

        # Sequence values
        values = [a1 * (r ** n) for n in range(num_terms)]  # 25,125,625,3125,15625
        terms = VGroup()
        arrows = VGroup()
        labels = VGroup()

        for n, an in enumerate(values):
            pos = line_start + (n / (num_terms - 1)) * (line_end - line_start)  # evenly spaced positions
            dot = Dot(pos, color=RED, radius=0.1)

            # Stagger labels (above/below with tweaks)
            if n % 2 == 0:  # even index
                label = Text(f"a{n}={an}", font_size=24, color=RED).next_to(dot, DOWN*4)  # pushed further down
            else:
                label = Text(f"a{n}={an}", font_size=24, color=RED).next_to(dot, UP*1.2)

            self.play(FadeIn(dot, scale=0.5), Write(label))
            terms.add(dot)
            labels.add(label)

            # Arrows with ×r
            if n > 0:
                prev_dot = terms[n-1]
                arrow = Arrow(prev_dot.get_center(), dot.get_center(), buff=0.1, color=GREEN)
                step_label = Text(f"×{r}", font_size=20, color=GREEN).next_to(arrow, UP if n % 2 == 0 else DOWN)
                self.play(GrowArrow(arrow), Write(step_label))
                arrows.add(arrow)
                labels.add(step_label)

        self.wait(2)

        # --- Graph view ---
        self.play(
            FadeOut(example),
            FadeOut(number_line),
            FadeOut(ticks),
            FadeOut(terms),
            FadeOut(arrows),
            FadeOut(labels),
        )
        self.play(formula.animate.to_edge(DOWN*6))

        # Axes for graph
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 17000, 2000],
            x_length=6,
            y_length=4,
            axis_config={"color": WHITE}
        ).to_edge(DOWN)
        x_label = Text("n", font_size=28).next_to(axes.x_axis.get_end(), DOWN)
        y_label = Text("an", font_size=28).next_to(axes.y_axis.get_end(), LEFT)
        self.play(Create(axes), Write(x_label), Write(y_label))

        # Plot graph points
        graph_points = VGroup()
        for n, an in enumerate(values):
            dot = Dot(axes.c2p(n, an), color=RED)
            label = Text(f"({n},{an})", font_size=20, color=RED)
            if n % 2 == 0:
                label.next_to(dot, DOWN*1.2)
            else:
                label.next_to(dot, UP*1.2)
            self.play(FadeIn(dot), Write(label))
            graph_points.add(dot, label)

        # Connect curve
        seq_curve = axes.plot_line_graph(
            x_values=list(range(len(values))),
            y_values=values,
            line_color=BLUE,
            add_vertex_dots=False
        )
        self.play(Create(seq_curve))
        self.wait(1)

        # Conclusion
        conclusion = Text(
            "Explosive Growth of 25 * 5^n",
            font_size=36, color=YELLOW
        ).next_to(axes, UP*2)
        self.play(Write(conclusion))
        self.wait(2)
