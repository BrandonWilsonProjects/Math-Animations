from manim import *

# ------------------------------------------------------------------
# Global look & feel
# ------------------------------------------------------------------
config.background_color = "#0e1117"

ADDEND_A_COLOR = "#5B8DEF"   # blue
ADDEND_B_COLOR = "#F5C147"   # gold
SUM_COLOR = "#4ADE80"        # green
ACCENT_COLOR = "#F472B6"     # pink, used sparingly for emphasis
MUTED_COLOR = "#8B8FA3"

TITLE_FONT_SIZE = 48
SUBTITLE_FONT_SIZE = 30
LABEL_FONT_SIZE = 34


def make_unit_square(color, side=0.5):
    """A single unit square used as a discrete 'countable' object."""
    return Square(side_length=side, color=color, fill_color=color,
                  fill_opacity=0.85, stroke_width=2)


def make_group(n, color, side=0.5, buff=0.2):
    """A row of n unit squares, already arranged."""
    squares = VGroup(*[make_unit_square(color, side) for _ in range(n)])
    squares.arrange(RIGHT, buff=buff)
    return squares


class MechanicsOfAddition(Scene):
    def construct(self):
        self.show_title()
        self.discrete_accumulation(3, 2)
        self.linear_translation(3, 2)
        self.vector_composition(3, 2)
        self.show_outro()

    # ----------------------------------------------------------------
    # PART 1: Title
    # ----------------------------------------------------------------
    def show_title(self):
        title = Text("The Art of Addition", font_size=TITLE_FONT_SIZE, weight=BOLD)
        subtitle = Text("Three ways of seeing the same idea",
                         font_size=SUBTITLE_FONT_SIZE, color=MUTED_COLOR)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.35)

        self.play(FadeIn(title_group, shift=UP * 0.3), run_time=1.2)
        self.wait(1.2)
        self.play(FadeOut(title_group, shift=UP * 0.3), run_time=0.8)

    # ----------------------------------------------------------------
    # PART 2: Discrete accumulation -- combining two groups of objects
    # ----------------------------------------------------------------
    def discrete_accumulation(self, a, b):
        heading = Text("Combining Groups", font_size=36, color=MUTED_COLOR).to_edge(UP)

        equation = VGroup(
            Text(str(a), font_size=64, color=ADDEND_A_COLOR),
            Text("+", font_size=64),
            Text(str(b), font_size=64, color=ADDEND_B_COLOR),
            Text("=", font_size=64),
            Text("?", font_size=64),
        ).arrange(RIGHT, buff=0.25)
        equation.next_to(heading, DOWN, buff=0.8)

        group_a = make_group(a, ADDEND_A_COLOR).shift(LEFT * 2.5 + DOWN * 0.5)
        group_b = make_group(b, ADDEND_B_COLOR).shift(RIGHT * 2.5 + DOWN * 0.5)

        self.play(FadeIn(heading))
        self.play(Write(equation[:4]))
        self.play(
            LaggedStart(*[FadeIn(sq, shift=DOWN * 0.3) for sq in group_a], lag_ratio=0.15),
            LaggedStart(*[FadeIn(sq, shift=DOWN * 0.3) for sq in group_b], lag_ratio=0.15),
        )
        self.wait(0.5)

        # The mechanic: physically slide group_b flush against group_a.
        # We reuse the ORIGINAL colored squares (no color information is lost)
        # so the viewer can still see which squares came from which addend.
        target_positions = VGroup(*[make_unit_square(WHITE) for _ in range(a + b)])
        target_positions.arrange(RIGHT, buff=0.2).move_to(DOWN * 0.5)

        self.play(
            group_a.animate.move_to(
                VGroup(*target_positions[:a]).get_center()
            ),
            group_b.animate.move_to(
                VGroup(*target_positions[a:]).get_center()
            ),
            run_time=1.5,
            rate_func=smooth,
        )
        self.wait(0.3)

        answer = Text(str(a + b), font_size=64, color=SUM_COLOR)
        answer.move_to(equation[4].get_center())
        self.play(
            Transform(equation[4], answer),
            Indicate(VGroup(group_a, group_b), color=SUM_COLOR, scale_factor=1.1),
        )
        self.wait(1.5)

        self.play(FadeOut(VGroup(heading, equation, group_a, group_b)))

    # ----------------------------------------------------------------
    # PART 3: Linear translation -- addition as movement along a line
    # ----------------------------------------------------------------
    def linear_translation(self, a, b):
        heading = Text("Addition as Movement", font_size=36, color=MUTED_COLOR).to_edge(UP)
        self.play(FadeIn(heading))

        nl = NumberLine(
            x_range=[0, a + b + 3, 1],
            length=10.5,
            color=WHITE,
            include_numbers=False,
        ).shift(DOWN * 0.5)

        # Build tick labels ourselves with plain Text so no LaTeX/DecimalNumber
        # machinery (which NumberLine's include_numbers=True relies on) is needed.
        nl_labels = VGroup(*[
            Text(str(n), font_size=24).next_to(nl.number_to_point(n), DOWN, buff=0.2)
            for n in range(0, a + b + 4)
        ])

        self.play(Create(nl), run_time=1.2)
        self.play(FadeIn(nl_labels), run_time=0.6)

        dot = Dot(nl.number_to_point(0), color=ACCENT_COLOR, radius=0.09)
        self.play(FadeIn(dot, scale=0.5))

        # Hop 1: magnitude a
        p0 = nl.number_to_point(0) + UP * 0.55
        pa = nl.number_to_point(a) + UP * 0.55
        arrow1 = ArcBetweenPoints(p0, pa, angle=-TAU / 8, color=ADDEND_A_COLOR)
        arrow1.add_tip(tip_length=0.2)
        label1 = Text(f"+{a}", color=ADDEND_A_COLOR, font_size=LABEL_FONT_SIZE)
        label1.next_to(arrow1, UP, buff=0.1)

        self.play(
            Create(arrow1),
            Write(label1),
            dot.animate.move_to(nl.number_to_point(a)),
            run_time=1.2,
        )
        self.wait(0.3)

        # Hop 2: magnitude b, continuing from where hop 1 ended
        pab = nl.number_to_point(a + b) + UP * 0.55
        arrow2 = ArcBetweenPoints(pa, pab, angle=-TAU / 8, color=ADDEND_B_COLOR)
        arrow2.add_tip(tip_length=0.2)
        label2 = Text(f"+{b}", color=ADDEND_B_COLOR, font_size=LABEL_FONT_SIZE)
        label2.next_to(arrow2, UP, buff=0.1)

        self.play(
            Create(arrow2),
            Write(label2),
            dot.animate.move_to(nl.number_to_point(a + b)),
            run_time=1.2,
        )
        self.wait(0.3)

        brace = Brace(VGroup(arrow1, arrow2), UP, color=SUM_COLOR, buff=0.5)
        # NOTE: Brace.get_text() is misleadingly named -- it wraps Tex (LaTeX)
        # internally, not plain Text. Build and place the label ourselves instead.
        brace_text = Text(f"+{a + b}", font_size=LABEL_FONT_SIZE, color=SUM_COLOR)
        brace_text.next_to(brace, UP, buff=0.15)

        self.play(GrowFromCenter(brace), Write(brace_text))
        self.play(Flash(dot, color=SUM_COLOR, flash_radius=0.3))
        self.wait(1.5)

        self.play(FadeOut(VGroup(
            heading, nl, nl_labels, dot, arrow1, arrow2, label1, label2, brace, brace_text
        )))

    # ----------------------------------------------------------------
    # PART 4: Vector composition -- tip-to-tail addition in the plane
    # ----------------------------------------------------------------
    def vector_composition(self, a, b):
        heading = Text("The Geometry Underneath", font_size=36, color=MUTED_COLOR).to_edge(UP)
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
        tip_ab = plane.c2p(a, 1 + b * 0.6)  # second hop, offset for a visible "tip-to-tail" bend

        vec_a = Arrow(origin, tip_a, buff=0, color=ADDEND_A_COLOR, stroke_width=6)
        vec_b = Arrow(tip_a, tip_ab, buff=0, color=ADDEND_B_COLOR, stroke_width=6)
        vec_sum = Arrow(origin, tip_ab, buff=0, color=SUM_COLOR, stroke_width=6)

        self.play(GrowArrow(vec_a))
        self.wait(0.3)
        self.play(GrowArrow(vec_b))
        self.wait(0.5)

        self.play(TransformFromCopy(VGroup(vec_a, vec_b), vec_sum), run_time=1.3)
        self.wait(1.5)

        self.play(FadeOut(VGroup(heading, plane, vec_a, vec_b, vec_sum)))

    # ----------------------------------------------------------------
    # PART 5: Outro
    # ----------------------------------------------------------------
    def show_outro(self):
        outro = Text(
            "Addition is the geometry of accumulation.",
            font_size=40, color=ADDEND_A_COLOR, weight=BOLD
        )
        self.play(Write(outro), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(outro, scale=1.1), run_time=1)