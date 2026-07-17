from manim import *

# ------------------------------------------------------------------
# Global look & feel
# ------------------------------------------------------------------
config.background_color = "#0e1117"

MINUEND_COLOR = "#5B8DEF"    # blue -- the starting amount
SUBTRAHEND_COLOR = "#F5C147"  # gold -- the amount being taken away
DIFF_COLOR = "#4ADE80"        # green -- what's left
ACCENT_COLOR = "#F472B6"      # pink, used sparingly for emphasis
MUTED_COLOR = "#8B8FA3"
GHOST_COLOR = "#3A3F4B"       # dimmed squares that have been removed

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


class MechanicsOfSubtraction(Scene):
    def construct(self):
        self.show_title()
        self.discrete_removal(5, 2)
        self.linear_translation(5, 2)
        self.vector_composition(5, 2)
        self.show_outro()

    # ----------------------------------------------------------------
    # PART 1: Title
    # ----------------------------------------------------------------
    def show_title(self):
        title = Text("The Art of Subtraction", font_size=TITLE_FONT_SIZE, weight=BOLD)
        subtitle = Text("Three ways of seeing the same idea",
                         font_size=SUBTITLE_FONT_SIZE, color=MUTED_COLOR)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.35)

        self.play(FadeIn(title_group, shift=UP * 0.3), run_time=1.2)
        self.wait(1.2)
        self.play(FadeOut(title_group, shift=UP * 0.3), run_time=0.8)

    # ----------------------------------------------------------------
    # PART 2: Discrete removal -- taking objects away from a group
    # ----------------------------------------------------------------
    def discrete_removal(self, a, b):
        heading = Text("Taking Away", font_size=36, color=MUTED_COLOR).to_edge(UP)

        equation = VGroup(
            Text(str(a), font_size=64, color=MINUEND_COLOR),
            Text("-", font_size=64),
            Text(str(b), font_size=64, color=SUBTRAHEND_COLOR),
            Text("=", font_size=64),
            Text("?", font_size=64),
        ).arrange(RIGHT, buff=0.25)
        equation.next_to(heading, DOWN, buff=0.8)

        group = make_group(a, MINUEND_COLOR).shift(DOWN * 0.5)

        self.play(FadeIn(heading))
        self.play(Write(equation[:4]))
        self.play(
            LaggedStart(*[FadeIn(sq, shift=DOWN * 0.3) for sq in group], lag_ratio=0.15)
        )
        self.wait(0.5)

        # The mechanic: mark the last b squares as the "subtrahend" group,
        # then physically remove them -- ghosting them out and sliding them
        # away rather than deleting them instantly, so the act of taking-away
        # is visible rather than implied.
        to_remove = VGroup(*group[a - b:])
        to_keep = VGroup(*group[:a - b])

        self.play(to_remove.animate.set_color(SUBTRAHEND_COLOR))
        self.wait(0.3)

        self.play(
            to_remove.animate.shift(DOWN * 1.5).set_opacity(0.15),
            run_time=1.2,
        )
        self.wait(0.3)

        # Close the gap left behind so the remaining group reads as one tidy set.
        self.play(
            to_keep.animate.arrange(RIGHT, buff=0.2).move_to(DOWN * 0.5),
            run_time=0.8,
        )

        answer = Text(str(a - b), font_size=64, color=DIFF_COLOR)
        answer.move_to(equation[4].get_center())
        self.play(
            Transform(equation[4], answer),
            Indicate(to_keep, color=DIFF_COLOR, scale_factor=1.1),
        )
        self.wait(1.5)

        self.play(FadeOut(VGroup(heading, equation, to_keep, to_remove)))

    # ----------------------------------------------------------------
    # PART 3: Linear translation -- subtraction as backward movement
    # ----------------------------------------------------------------
    def linear_translation(self, a, b):
        heading = Text("Addition in Reverse", font_size=36, color=MUTED_COLOR).to_edge(UP)
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
            Text(str(n), font_size=24).next_to(nl.number_to_point(n), DOWN, buff=0.2)
            for n in range(0, a + 3)
        ])

        self.play(Create(nl), run_time=1.2)
        self.play(FadeIn(nl_labels), run_time=0.6)

        dot = Dot(nl.number_to_point(a), color=ACCENT_COLOR, radius=0.09)
        self.play(FadeIn(dot, scale=0.5))

        # Start at a, hop backward by b.
        pa = nl.number_to_point(a) + UP * 0.55
        pab = nl.number_to_point(a - b) + UP * 0.55
        arrow = ArcBetweenPoints(pa, pab, angle=TAU / 8, color=SUBTRAHEND_COLOR)
        arrow.add_tip(tip_length=0.2)
        label = Text(f"-{b}", color=SUBTRAHEND_COLOR, font_size=LABEL_FONT_SIZE)
        label.next_to(arrow, UP, buff=0.1)

        self.play(
            Create(arrow),
            Write(label),
            dot.animate.move_to(nl.number_to_point(a - b)),
            run_time=1.2,
        )
        self.wait(0.3)

        result_label = Text(str(a - b), font_size=LABEL_FONT_SIZE, color=DIFF_COLOR)
        result_label.next_to(dot, DOWN, buff=0.4)

        self.play(Write(result_label))
        self.play(Flash(dot, color=DIFF_COLOR, flash_radius=0.3))
        self.wait(1.5)

        self.play(FadeOut(VGroup(
            heading, nl, nl_labels, dot, arrow, label, result_label
        )))

    # ----------------------------------------------------------------
    # PART 4: Vector composition -- subtracting is adding the opposite
    # ----------------------------------------------------------------
    def vector_composition(self, a, b):
        heading = Text("Adding the Opposite", font_size=36, color=MUTED_COLOR).to_edge(UP)
        self.play(FadeIn(heading))

        plane = NumberPlane(
            x_range=[-1, 8, 1],
            y_range=[-1, 5, 1],
            x_length=9,
            y_length=5,
            background_line_style={
                "stroke_color": MUTED_COLOR,
                "stroke_width": 1,
                "stroke_opacity": 0.3,
            },
        ).shift(DOWN * 0.3)
        self.play(Create(plane), run_time=1)

        origin = plane.c2p(0, 0)
        tip_a = plane.c2p(a, 1)
        # The subtrahend vector points "backward" (down-left) to visualize
        # -b as the opposite of +b, tip-to-tail from where +a left off.
        tip_ab = plane.c2p(a - b, 1 - b * 0.4)

        vec_a = Arrow(origin, tip_a, buff=0, color=MINUEND_COLOR, stroke_width=6)
        vec_b = Arrow(tip_a, tip_ab, buff=0, color=SUBTRAHEND_COLOR, stroke_width=6)
        vec_diff = Arrow(origin, tip_ab, buff=0, color=DIFF_COLOR, stroke_width=6)

        self.play(GrowArrow(vec_a))
        self.wait(0.3)
        self.play(GrowArrow(vec_b))
        self.wait(0.5)

        self.play(TransformFromCopy(VGroup(vec_a, vec_b), vec_diff), run_time=1.3)
        self.wait(1.5)

        self.play(FadeOut(VGroup(heading, plane, vec_a, vec_b, vec_diff)))

    # ----------------------------------------------------------------
    # PART 5: Outro
    # ----------------------------------------------------------------
    def show_outro(self):
        outro = Text(
            "Subtraction is addition, walked backward.",
            font_size=40, color=SUBTRAHEND_COLOR, weight=BOLD
        )
        self.play(Write(outro), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(outro, scale=1.1), run_time=1)