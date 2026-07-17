from manim import *

# ------------------------------------------------------------------
# Global look & feel
# ------------------------------------------------------------------
config.background_color = "#0e1117"

FACTOR_A_COLOR = "#5B8DEF"   # blue -- size of each group / rectangle width
FACTOR_B_COLOR = "#F5C147"   # gold -- number of groups / rectangle height
PRODUCT_COLOR = "#4ADE80"    # green -- the total
ACCENT_COLOR = "#F472B6"     # pink, used sparingly for emphasis
MUTED_COLOR = "#8B8FA3"

TITLE_FONT_SIZE = 48
SUBTITLE_FONT_SIZE = 30
LABEL_FONT_SIZE = 34

# NOTE on LaTeX: this file deliberately avoids MathTex, Tex, and any Manim
# helper that secretly wraps them (e.g. Brace.get_text(), NumberLine's
# include_numbers=True / DecimalNumber). Everything text-based here uses
# plain Text so the scene only needs FFmpeg to render, not a LaTeX install.


def make_unit_square(color, side=0.5):
    """A single unit square used as a discrete 'countable' object."""
    return Square(side_length=side, color=color, fill_color=color,
                  fill_opacity=0.85, stroke_width=2)


def make_group(n, color, side=0.5, buff=0.2):
    """A row of n unit squares, already arranged."""
    squares = VGroup(*[make_unit_square(color, side) for _ in range(n)])
    squares.arrange(RIGHT, buff=buff)
    return squares


class MechanicsOfMultiplication(Scene):
    def construct(self):
        self.show_title()
        self.repeated_groups(3, 4)
        self.repeated_jumps(3, 4)
        self.area_model(3, 4)
        self.show_outro()

    # ----------------------------------------------------------------
    # PART 1: Title
    # ----------------------------------------------------------------
    def show_title(self):
        title = Text("The Art of Multiplication", font_size=TITLE_FONT_SIZE, weight=BOLD)
        subtitle = Text("Three ways of seeing the same idea",
                         font_size=SUBTITLE_FONT_SIZE, color=MUTED_COLOR)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.35)

        self.play(FadeIn(title_group, shift=UP * 0.3), run_time=1.2)
        self.wait(1.2)
        self.play(FadeOut(title_group, shift=UP * 0.3), run_time=0.8)

    # ----------------------------------------------------------------
    # PART 2: Repeated groups -- b groups of a objects, collapsed into a grid
    # ----------------------------------------------------------------
    def repeated_groups(self, a, b):
        heading = Text("Groups of Groups", font_size=36, color=MUTED_COLOR).to_edge(UP)

        equation = VGroup(
            Text(str(a), font_size=64, color=FACTOR_A_COLOR),
            Text("x", font_size=64),
            Text(str(b), font_size=64, color=FACTOR_B_COLOR),
            Text("=", font_size=64),
            Text("?", font_size=64),
        ).arrange(RIGHT, buff=0.25)
        equation.next_to(heading, DOWN, buff=0.7)

        self.play(FadeIn(heading))
        self.play(Write(equation[:4]))

        # Build b separate rows of a squares each, stacked with visible gaps
        # so each "group" reads as its own unit before they collapse into a grid.
        rows = VGroup(*[make_group(a, FACTOR_A_COLOR) for _ in range(b)])
        rows.arrange(DOWN, buff=0.35).next_to(equation, DOWN, buff=0.6)

        self.play(
            LaggedStart(*[FadeIn(row, shift=LEFT * 0.3) for row in rows], lag_ratio=0.25)
        )
        self.wait(0.5)

        # Label each row as "one group" briefly, then collapse the gaps so the
        # b groups visibly become a single a-by-b grid.
        brace_labels = VGroup(*[
            Text(f"group {i + 1}", font_size=20, color=FACTOR_B_COLOR).next_to(row, RIGHT, buff=0.3)
            for i, row in enumerate(rows)
        ])
        self.play(LaggedStart(*[FadeIn(lbl) for lbl in brace_labels], lag_ratio=0.2))
        self.wait(0.8)
        self.play(FadeOut(brace_labels))

        self.play(
            rows.animate.arrange(DOWN, buff=0.2).move_to(DOWN * 0.3),
            run_time=1.2,
        )
        self.wait(0.3)

        answer = Text(str(a * b), font_size=64, color=PRODUCT_COLOR)
        answer.move_to(equation[4].get_center())
        self.play(
            Transform(equation[4], answer),
            Indicate(rows, color=PRODUCT_COLOR, scale_factor=1.05),
        )
        self.wait(1.5)

        self.play(FadeOut(VGroup(heading, equation, rows)))

    # ----------------------------------------------------------------
    # PART 3: Repeated jumps -- multiplication as repeated addition on a line
    # ----------------------------------------------------------------
    def repeated_jumps(self, a, b):
        heading = Text("Repeated Addition", font_size=36, color=MUTED_COLOR).to_edge(UP)
        self.play(FadeIn(heading))

        total = a * b
        nl = NumberLine(
            x_range=[0, total + 2, 1],
            length=10.5,
            color=WHITE,
            include_numbers=False,
        ).shift(DOWN * 0.5)

        # Build tick labels ourselves with plain Text -- see the LaTeX note
        # at the top of the file for why we don't use include_numbers=True.
        nl_labels = VGroup(*[
            Text(str(n), font_size=22).next_to(nl.number_to_point(n), DOWN, buff=0.2)
            for n in range(0, total + 3, max(1, total // 10 or 1))
        ])

        self.play(Create(nl), run_time=1.2)
        self.play(FadeIn(nl_labels), run_time=0.6)

        dot = Dot(nl.number_to_point(0), color=ACCENT_COLOR, radius=0.09)
        self.play(FadeIn(dot, scale=0.5))

        # b hops of size a, each one alternating slightly in arc direction
        # so consecutive arcs don't visually overlap.
        arrows = VGroup()
        for i in range(b):
            start_val = i * a
            end_val = (i + 1) * a
            p_start = nl.number_to_point(start_val) + UP * 0.55
            p_end = nl.number_to_point(end_val) + UP * 0.55
            arc = ArcBetweenPoints(p_start, p_end, angle=-TAU / 10, color=FACTOR_A_COLOR)
            arc.add_tip(tip_length=0.15)
            arrows.add(arc)

            self.play(
                Create(arc),
                dot.animate.move_to(nl.number_to_point(end_val)),
                run_time=0.9,
            )

        count_label = Text(f"{a} added {b} times", font_size=24, color=FACTOR_B_COLOR)
        count_label.next_to(nl, UP, buff=1.1)
        self.play(FadeIn(count_label))
        self.wait(0.3)

        result_label = Text(str(total), font_size=LABEL_FONT_SIZE, color=PRODUCT_COLOR)
        result_label.next_to(dot, DOWN, buff=0.5)
        self.play(Write(result_label))
        self.play(Flash(dot, color=PRODUCT_COLOR, flash_radius=0.3))
        self.wait(1.5)

        self.play(FadeOut(VGroup(
            heading, nl, nl_labels, dot, arrows, count_label, result_label
        )))

    # ----------------------------------------------------------------
    # PART 4: Area model -- multiplication as the area of a rectangle
    # ----------------------------------------------------------------
    def area_model(self, a, b):
        heading = Text("The Area Underneath", font_size=36, color=MUTED_COLOR).to_edge(UP)
        self.play(FadeIn(heading))

        cell = 0.6
        grid = VGroup(*[
            Square(side_length=cell, stroke_width=1.5, stroke_color=WHITE,
                   fill_color=FACTOR_A_COLOR, fill_opacity=0.0)
            for _ in range(a * b)
        ])
        grid.arrange_in_grid(rows=b, cols=a, buff=0)
        grid.move_to(ORIGIN + DOWN * 0.2)

        width_brace = Brace(grid, DOWN, color=FACTOR_A_COLOR)
        width_label = Text(str(a), font_size=LABEL_FONT_SIZE, color=FACTOR_A_COLOR)
        width_label.next_to(width_brace, DOWN, buff=0.15)

        height_brace = Brace(grid, LEFT, color=FACTOR_B_COLOR)
        height_label = Text(str(b), font_size=LABEL_FONT_SIZE, color=FACTOR_B_COLOR)
        height_label.next_to(height_brace, LEFT, buff=0.15)

        outline = SurroundingRectangle(grid, color=WHITE, buff=0)

        self.play(Create(outline))
        self.play(GrowFromCenter(width_brace), Write(width_label))
        self.play(GrowFromCenter(height_brace), Write(height_label))
        self.wait(0.4)

        # Fill in the grid cell by cell, row by row, so the a*b unit squares
        # visibly accumulate into the rectangle's area.
        self.play(
            LaggedStart(
                *[cell_sq.animate.set_fill(opacity=0.85) for cell_sq in grid],
                lag_ratio=0.03,
            ),
            run_time=2.0,
        )
        self.wait(0.3)

        area_label = Text(f"{a} x {b} = {a * b}", font_size=LABEL_FONT_SIZE, color=PRODUCT_COLOR)
        area_label.next_to(outline, UP, buff=0.5)
        self.play(Write(area_label))
        self.wait(1.5)

        self.play(FadeOut(VGroup(
            heading, grid, outline, width_brace, width_label,
            height_brace, height_label, area_label
        )))

    # ----------------------------------------------------------------
    # PART 5: Outro
    # ----------------------------------------------------------------
    def show_outro(self):
        outro = Text(
            "Multiplication is addition, folded into area.",
            font_size=40, color=FACTOR_A_COLOR, weight=BOLD
        )
        self.play(Write(outro), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(outro, scale=1.1), run_time=1)