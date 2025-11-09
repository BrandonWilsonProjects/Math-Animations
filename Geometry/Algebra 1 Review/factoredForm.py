from manim import *

class FactorQuadratic(Scene):
    def construct(self):
        # --- smaller sizes for "algebra tiles" (reduced so they don't block text)
        x_size = 2.0    # was 3.0
        unit   = 0.4    # was 0.6

        # Title
        title = Text("Factoring a Quadratic: x^2 + 5x + 6", font_size=36)
        title.to_edge(UP)
        self.play(FadeIn(title))

        # Expression text
        expr = Text("x^2 + 5x + 6", font_size=30)
        expr.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(expr))

        # --- Create tiles (colors: x^2=BLUE, x=GREEN, 1=YELLOW)
        x2_tile = Rectangle(width=x_size, height=x_size).set_fill(BLUE, 0.55).set_stroke(WHITE, 2)

        x_right = VGroup(*[
            Rectangle(width=unit, height=x_size).set_fill(GREEN, 0.55).set_stroke(WHITE, 2)
            for _ in range(3)
        ])
        x_bottom = VGroup(*[
            Rectangle(width=x_size, height=unit).set_fill(GREEN, 0.55).set_stroke(WHITE, 2)
            for _ in range(2)
        ])
        ones = VGroup(*[
            Square(side_length=unit).set_fill(YELLOW, 0.65).set_stroke(WHITE, 2)
            for _ in range(6)
        ])

        # Start with tiles grouped on the left and slightly UP (so they don't sit on lower text)
        all_tiles = VGroup(x2_tile, x_right, x_bottom, ones).arrange(RIGHT, buff=0.35)
        all_tiles.to_edge(LEFT, buff=0.7).shift(UP * 0.3)  # was DOWN*0.5
        self.play(FadeIn(all_tiles, lag_ratio=0.1))
        self.wait(0.4)

        # --- Arrange tiles into a rectangle of size (x+3) by (x+2)
        # Anchor the rectangle slightly higher
        target_origin = ORIGIN + RIGHT * 1.3 + UP * 0.2  # was RIGHT*1.5 + DOWN*0.5
        x2_target = x2_tile.copy().move_to(target_origin)

        # Three vertical x-tiles to the RIGHT of x^2 (forming +3 on width)
        x_right_targets = x_right.copy().arrange(RIGHT, buff=0)
        x_right_targets.next_to(x2_target, RIGHT, buff=0, aligned_edge=UP)

        # Two horizontal x-tiles BELOW x^2 (forming +2 on height)
        x_bottom_targets = x_bottom.copy().arrange(DOWN, buff=0)
        x_bottom_targets.next_to(x2_target, DOWN, buff=0, aligned_edge=LEFT)

        # 2x3 block of ones at bottom-right corner
        ones_grid = ones.copy().arrange_in_grid(rows=2, cols=3, buff=0)
        br_corner = x2_target.get_corner(DR)
        ones_target_center = br_corner + RIGHT * (3 * unit / 2) + DOWN * (2 * unit / 2)
        ones_grid.move_to(ones_target_center)

        # Animate tiles into place
        self.play(
            x2_tile.animate.move_to(x2_target),
            Transform(x_right, x_right_targets),
            Transform(x_bottom, x_bottom_targets),
            Transform(ones, ones_grid),
            run_time=2
        )
        self.wait(0.4)

        # Draw the outline of the full rectangle ( (x+3) by (x+2) )
        full_width  = x_size + 3 * unit
        full_height = x_size + 2 * unit
        rect_outline = Rectangle(width=full_width, height=full_height).set_stroke(WHITE, 3)
        rect_outline.move_to(x2_target.get_center() + RIGHT * (3 * unit / 2) + DOWN * (2 * unit / 2))
        self.play(Create(rect_outline))

        # Side labels using braces (no LaTeX, just Text)
        left_top = rect_outline.get_corner(UL)
        left_bot = rect_outline.get_corner(DL)
        top_left = rect_outline.get_corner(UL)
        top_right= rect_outline.get_corner(UR)

        brace_left = BraceBetweenPoints(left_bot, left_top, direction=LEFT)
        brace_top  = BraceBetweenPoints(top_left, top_right, direction=UP)
        left_label = Text("x + 2", font_size=28).next_to(brace_left, LEFT, buff=0.2)
        top_label  = Text("x + 3", font_size=28).next_to(brace_top,   UP,   buff=0.2)

        self.play(GrowFromCenter(brace_left), FadeIn(left_label))
        self.play(GrowFromCenter(brace_top),  FadeIn(top_label))
        self.wait(0.4)

        # Show the factorization result (kept low on screen)
        fact_text = Text("Factor: (x + 2)(x + 3)", font_size=32).set_color(YELLOW)
        fact_text.to_edge(DOWN, buff=0.6)

        # Place the hint directly ABOVE the factor text
        hint = Text("Find two numbers that multiply to 6 and add to 5 → 2 and 3", font_size=26)
        hint.next_to(fact_text, UP, buff=0.2)

        # Animate in this order and keep them on top
        self.play(FadeIn(fact_text))
        self.play(FadeIn(hint))
        self.bring_to_front(hint, fact_text)

        # Clean finish
        self.play(
            FadeOut(hint, fact_text, brace_left, brace_top, left_label, top_label),
            rect_outline.animate.set_stroke(opacity=0.3)
        )
        self.wait(0.6)
