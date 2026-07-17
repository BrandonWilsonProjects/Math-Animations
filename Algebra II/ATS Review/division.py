from manim import *

# ------------------------------------------------------------------
# Global look & feel
# ------------------------------------------------------------------
config.background_color = "#0e1117"

DIVIDEND_COLOR = "#5B8DEF"   # blue -- the total being divided
DIVISOR_COLOR = "#F5C147"    # gold -- the size (or number) of groups
QUOTIENT_COLOR = "#4ADE80"   # green -- the result
ACCENT_COLOR = "#F472B6"     # pink, used sparingly for emphasis
MUTED_COLOR = "#8B8FA3"

TITLE_FONT_SIZE = 48
SUBTITLE_FONT_SIZE = 30
LABEL_FONT_SIZE = 34

# NOTE on LaTeX: this file deliberately avoids MathTex, Tex, and any Manim
# helper that secretly wraps them (e.g. Brace.get_text(), NumberLine's
# include_numbers=True / DecimalNumber). Everything text-based here uses
# plain Text so the scene only needs FFmpeg to render, not a LaTeX install.
#
# All three sections use numbers that divide evenly (default 12 / 3).
# Fair_sharing and repeated_subtraction assume `a % b == 0`; pick factor
# pairs accordingly if you change the defaults in construct().


def make_unit_square(color, side=0.5):
    """A single unit square used as a discrete 'countable' object."""
    return Square(side_length=side, color=color, fill_color=color,
                  fill_opacity=0.85, stroke_width=2)


class MechanicsOfDivision(Scene):
    def construct(self):
        self.show_title()
        self.fair_sharing(12, 3)
        self.repeated_subtraction(12, 3)
        self.area_model(12, 3)
        self.show_outro()

    # ----------------------------------------------------------------
    # PART 1: Title
    # ----------------------------------------------------------------
    def show_title(self):
        title = Text("The Art of Division", font_size=TITLE_FONT_SIZE, weight=BOLD)
        subtitle = Text("Three ways of seeing the same idea",
                         font_size=SUBTITLE_FONT_SIZE, color=MUTED_COLOR)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.35)

        self.play(FadeIn(title_group, shift=UP * 0.3), run_time=1.2)
        self.wait(1.2)
        self.play(FadeOut(title_group, shift=UP * 0.3), run_time=0.8)

    # ----------------------------------------------------------------
    # PART 2: Fair sharing -- splitting a total into b equal groups
    # ----------------------------------------------------------------
    def fair_sharing(self, a, b):
        quotient = a // b
        heading = Text("Fair Sharing", font_size=36, color=MUTED_COLOR).to_edge(UP)

        equation = VGroup(
            Text(str(a), font_size=64, color=DIVIDEND_COLOR),
            Text("/", font_size=64),
            Text(str(b), font_size=64, color=DIVISOR_COLOR),
            Text("=", font_size=64),
            Text("?", font_size=64),
        ).arrange(RIGHT, buff=0.25)
        equation.next_to(heading, DOWN, buff=0.7)

        self.play(FadeIn(heading))
        self.play(Write(equation[:4]))

        # Start as one undifferentiated pile of `a` squares.
        pile = VGroup(*[make_unit_square(DIVIDEND_COLOR) for _ in range(a)])
        pile.arrange_in_grid(rows=2, cols=(a + 1) // 2, buff=0.15)
        pile.next_to(equation, DOWN, buff=0.6)

        self.play(
            LaggedStart(*[FadeIn(sq, scale=0.6) for sq in pile], lag_ratio=0.05)
        )
        self.wait(0.4)

        # The mechanic: deal the pile out into b empty bins, one at a time,
        # round-robin -- literally "sharing fairly" rather than a static split.
        bin_width = 1.3
        bins = VGroup(*[
            Rectangle(width=bin_width, height=1.8, stroke_color=DIVISOR_COLOR, stroke_width=2)
            for _ in range(b)
        ])
        bins.arrange(RIGHT, buff=0.5).move_to(DOWN * 0.3)
        bin_labels = VGroup(*[
            Text(f"group {i + 1}", font_size=18, color=DIVISOR_COLOR).next_to(bins[i], DOWN, buff=0.15)
            for i in range(b)
        ])

        self.play(Create(bins), FadeIn(bin_labels))
        self.wait(0.3)

        # Deal each square into its bin round-robin, stacking within the bin.
        placed_counts = [0] * b
        deal_anims = []
        for i, sq in enumerate(pile):
            target_bin = i % b
            row = placed_counts[target_bin] // 3
            col = placed_counts[target_bin] % 3
            target_pos = bins[target_bin].get_corner(UL) + RIGHT * (0.25 + col * 0.35) + DOWN * (0.3 + row * 0.35)
            deal_anims.append(sq.animate.move_to(target_pos).scale(0.85))
            placed_counts[target_bin] += 1

        self.play(LaggedStart(*deal_anims, lag_ratio=0.06), run_time=2.2)
        self.wait(0.5)

        per_bin_labels = VGroup(*[
            Text(str(quotient), font_size=28, color=QUOTIENT_COLOR).next_to(bins[i], UP, buff=0.15)
            for i in range(b)
        ])
        self.play(LaggedStart(*[FadeIn(lbl, shift=UP * 0.1) for lbl in per_bin_labels], lag_ratio=0.2))
        self.wait(0.3)

        answer = Text(str(quotient), font_size=64, color=QUOTIENT_COLOR)
        answer.move_to(equation[4].get_center())
        self.play(
            Transform(equation[4], answer),
            Indicate(bins, color=QUOTIENT_COLOR, scale_factor=1.05),
        )
        self.wait(1.5)

        self.play(FadeOut(VGroup(
            heading, equation, pile, bins, bin_labels, per_bin_labels
        )))

    # ----------------------------------------------------------------
    # PART 3: Repeated subtraction -- how many times does b fit into a?
    # ----------------------------------------------------------------
    def repeated_subtraction(self, a, b):
        quotient = a // b
        heading = Text("Repeated Subtraction", font_size=36, color=MUTED_COLOR).to_edge(UP)
        self.play(FadeIn(heading))

        nl = NumberLine(
            x_range=[0, a + 2, 1],
            length=10.5,
            color=WHITE,
            include_numbers=False,
        ).shift(DOWN * 0.5)

        # Build tick labels ourselves with plain Text -- see the LaTeX note
        # at the top of the file for why we don't use include_numbers=True.
        nl_labels = VGroup(*[
            Text(str(n), font_size=22).next_to(nl.number_to_point(n), DOWN, buff=0.2)
            for n in range(0, a + 3, max(1, (a + 2) // 12 or 1))
        ])

        self.play(Create(nl), run_time=1.2)
        self.play(FadeIn(nl_labels), run_time=0.6)

        dot = Dot(nl.number_to_point(a), color=ACCENT_COLOR, radius=0.09)
        self.play(FadeIn(dot, scale=0.5))

        hop_counter = Text("0 hops", font_size=24, color=DIVISOR_COLOR)
        hop_counter.next_to(nl, UP, buff=1.1)
        self.play(FadeIn(hop_counter))

        arrows = VGroup()
        for i in range(quotient):
            start_val = a - i * b
            end_val = start_val - b
            p_start = nl.number_to_point(start_val) + UP * 0.55
            p_end = nl.number_to_point(end_val) + UP * 0.55
            arc = ArcBetweenPoints(p_start, p_end, angle=TAU / 10, color=DIVISOR_COLOR)
            arc.add_tip(tip_length=0.15)
            arrows.add(arc)

            new_counter = Text(f"{i + 1} hop{'s' if i > 0 else ''}", font_size=24, color=DIVISOR_COLOR)
            new_counter.move_to(hop_counter)

            self.play(
                Create(arc),
                dot.animate.move_to(nl.number_to_point(end_val)),
                Transform(hop_counter, new_counter),
                run_time=0.9,
            )

        result_label = Text(f"{quotient}", font_size=LABEL_FONT_SIZE, color=QUOTIENT_COLOR)
        result_label.next_to(dot, DOWN, buff=0.5)
        self.play(Write(result_label))
        self.play(Flash(dot, color=QUOTIENT_COLOR, flash_radius=0.3))
        self.wait(1.5)

        self.play(FadeOut(VGroup(
            heading, nl, nl_labels, dot, arrows, hop_counter, result_label
        )))

    # ----------------------------------------------------------------
    # PART 4: Area model -- division as finding a rectangle's missing side
    # ----------------------------------------------------------------
    def area_model(self, a, b):
        quotient = a // b
        heading = Text("The Missing Side", font_size=36, color=MUTED_COLOR).to_edge(UP)
        self.play(FadeIn(heading))

        cell = 0.55
        grid = VGroup(*[
            Square(side_length=cell, stroke_width=1.5, stroke_color=WHITE,
                   fill_color=DIVIDEND_COLOR, fill_opacity=0.85)
            for _ in range(a)
        ])
        # Start as one long strip of `a` unit cells -- the "area" we know,
        # with neither dimension fixed yet.
        grid.arrange(RIGHT, buff=0)
        grid.move_to(UP * 0.3)

        area_label = Text(f"area = {a}", font_size=LABEL_FONT_SIZE, color=DIVIDEND_COLOR)
        area_label.next_to(grid, UP, buff=0.4)

        self.play(
            LaggedStart(*[FadeIn(sq, scale=0.6) for sq in grid], lag_ratio=0.04)
        )
        self.play(Write(area_label))
        self.wait(0.5)

        # The mechanic: fold the strip into `b` rows, revealing the other
        # side length as whatever falls out of an even split.
        target_grid = VGroup(*[
            Square(side_length=cell, stroke_width=1.5, stroke_color=WHITE,
                   fill_color=DIVIDEND_COLOR, fill_opacity=0.85)
            for _ in range(a)
        ])
        target_grid.arrange_in_grid(rows=b, cols=quotient, buff=0)
        target_grid.move_to(DOWN * 0.2)

        self.play(
            *[grid[i].animate.move_to(target_grid[i].get_center()) for i in range(a)],
            area_label.animate.next_to(target_grid, UP, buff=0.4),
            run_time=1.8,
        )
        self.wait(0.3)

        outline = SurroundingRectangle(grid, color=WHITE, buff=0)
        self.play(Create(outline))

        known_side_brace = Brace(grid, LEFT, color=DIVISOR_COLOR)
        known_side_label = Text(str(b), font_size=LABEL_FONT_SIZE, color=DIVISOR_COLOR)
        known_side_label.next_to(known_side_brace, LEFT, buff=0.15)

        missing_side_brace = Brace(grid, DOWN, color=QUOTIENT_COLOR)
        missing_side_label = Text(str(quotient), font_size=LABEL_FONT_SIZE, color=QUOTIENT_COLOR)
        missing_side_label.next_to(missing_side_brace, DOWN, buff=0.15)

        self.play(GrowFromCenter(known_side_brace), Write(known_side_label))
        self.wait(0.3)
        self.play(GrowFromCenter(missing_side_brace), Write(missing_side_label))
        self.wait(1.5)

        self.play(FadeOut(VGroup(
            heading, grid, outline, area_label,
            known_side_brace, known_side_label,
            missing_side_brace, missing_side_label
        )))

    # ----------------------------------------------------------------
    # PART 5: Outro
    # ----------------------------------------------------------------
    def show_outro(self):
        outro = Text(
            "Division is area, unfolded back into a side.",
            font_size=40, color=DIVISOR_COLOR, weight=BOLD
        )
        self.play(Write(outro), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(outro, scale=1.1), run_time=1)