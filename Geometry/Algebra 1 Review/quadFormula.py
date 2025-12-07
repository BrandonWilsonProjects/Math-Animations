from manim import *

class QuadraticFormulaIntro(Scene):
    def construct(self):
        # Title
        title = Text("The Quadratic Formula", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()
        
        # Show the general form
        general_form = Text("General Form: ax² + bx + c = 0", font_size=36)
        general_form.next_to(title, DOWN, buff=0.6)
        self.play(FadeIn(general_form))
        self.wait()
        
        # Show the quadratic formula
        formula_text = Text("The Quadratic Formula:", font_size=32)
        formula_text.next_to(general_form, DOWN, buff=0.8)
        self.play(FadeIn(formula_text))
        
        # Show the quadratic formula with proper mathematical layout
        # Create the main parts
        x_equals = Text("x =", font_size=40, color=YELLOW)
        minus_b = Text("-b ± ", font_size=36, color=YELLOW)
        sqrt_symbol = Text("√", font_size=50, color=YELLOW)

        # The radicand (what's under the square root)
        radicand = Text("b² - 4ac", font_size=32, color=YELLOW)

        # The fraction bar
        fraction_line = Line(LEFT * 1.5, RIGHT * 1.5, color=YELLOW, stroke_width=3)

        # Denominator
        denominator = Text("2a", font_size=36, color=YELLOW)

        # Position the numerator components
        numerator = VGroup(minus_b, sqrt_symbol, radicand).arrange(RIGHT, buff=0.1)
        sqrt_symbol.shift(UP * 0.05)
        radicand.next_to(sqrt_symbol, RIGHT, buff=0.1).shift(DOWN * 0.1)

        # Add overline for radicand
        overline = Line(
            radicand.get_left() + UP * 0.35 + LEFT * 0.12,
            radicand.get_right() + UP * 0.35 + RIGHT * 0.12,
            color=YELLOW,
            stroke_width=2
        )
        overline.next_to(sqrt_symbol.get_top(), RIGHT, buff=0.01, aligned_edge=UP).shift(DOWN * 0.03)

        # Position fraction parts
        fraction_line.next_to(numerator, DOWN, buff=0.2)
        denominator.next_to(fraction_line, DOWN, buff=0.2)

        # Group the entire fraction
        fraction = VGroup(numerator, overline, fraction_line, denominator)

        # Position everything
        x_equals.next_to(formula_text, DOWN*2 + LEFT*0.002, buff=0.4)
        fraction.next_to(x_equals, RIGHT, buff=0.3)

        # Animate
        self.play(Write(x_equals))
        self.play(Write(minus_b))
        self.play(Write(sqrt_symbol), Create(overline))
        self.play(Write(radicand))
        self.play(Create(fraction_line))
        self.play(Write(denominator))
        self.wait(2)
        
        # Show an example
        example_title = Text("Example:", font_size=32)
        example_title.next_to(denominator, DOWN*0.3, buff=1)
        self.play(FadeIn(example_title))
        
        example = Text("x² + 3x + 1 = 0", font_size=38, color=BLUE)
        example.next_to(example_title, DOWN, buff=0.4)
        self.play(Write(example))
        self.wait()
        
        # Identify coefficients
        coef_text = Text("Identify the coefficients:", font_size=30)
        coef_text.next_to(example, DOWN*1, buff=0.6)
        self.play(FadeIn(coef_text))
        self.wait(0.5)
        
        a_text = Text("a = 1", font_size=32, color=RED)
        b_text = Text("b = 3", font_size=32, color=GREEN)
        c_text = Text("c = 1", font_size=32, color=ORANGE)
        
        coefficients = VGroup(a_text, b_text, c_text).arrange(RIGHT, buff=1)
        coefficients.next_to(coef_text, DOWN*0.1, buff=0.4)
        
        self.play(FadeIn(a_text))
        self.wait(0.3)
        self.play(FadeIn(b_text))
        self.wait(0.3)
        self.play(FadeIn(c_text))
        self.wait(2)
        
        # Fade everything out
        self.play(
            FadeOut(title),
            FadeOut(general_form),
            FadeOut(formula_text),
            FadeOut(x_equals),
            FadeOut(minus_b),
            FadeOut(sqrt_symbol), FadeOut(overline),
            FadeOut(radicand),
            FadeOut(fraction_line),
            FadeOut(denominator),
            FadeOut(example_title),
            FadeOut(example),
            FadeOut(coef_text),
            FadeOut(coefficients)
        )
        self.wait(0.5)
        
class ImperfectSquareExample(Scene):
    def construct(self):
        
        transition_intro = Text("QUADRATIC FORMULA", font_size=50)
        self.play(FadeIn(transition_intro))
        
        transition_subtext1 = Text("Algebraic Solution", color=GREEN, font_size=36).next_to(transition_intro, DOWN*2, buff=0.3)
        transition_subtext2 = Text("Visual Solution", font_size=36).next_to(transition_subtext1, DOWN*1.2, buff=0.3)
        self.play(FadeIn(transition_subtext1, transition_subtext2))
        
        check1 = Text("✓", font_size=35)
        check1.next_to(transition_subtext1)
        self.play(FadeIn(check1))
        self.play(FadeOut(transition_subtext2))
        self.wait(2)
        self.play(FadeOut(transition_intro, transition_subtext1, check1))
        
        # Title
        title = Text("Imperfect Square: Irrational Roots", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()
        
        # Example that doesn't factor nicely
        equation = Text("x² + 3x + 1 = 0", font_size=48)
        equation.next_to(title, DOWN, buff=0.5)
        self.play(Write(equation))
        self.wait()
        
        note = Text("(This doesn't factor with integers!)", font_size=28, color=YELLOW)
        note.next_to(equation, DOWN, buff=0.3)
        self.play(Write(note))
        self.wait()
        
        # Apply quadratic formula
        formula = Text("x = (-3 ± √(9 - 4)) / 2", font_size=38)
        formula.next_to(note, DOWN, buff=0.7)
        self.play(Write(formula))
        self.wait()
        
        step1 = Text("x = (-3 ± √5) / 2", font_size=42)
        step1.move_to(formula.get_center())
        self.play(Transform(formula, step1))
        self.wait()
        
        # Show the two irrational roots
        roots_text = Text("The roots are irrational:", font_size=32)
        roots_text.next_to(formula, DOWN, buff=0.7)
        self.play(Write(roots_text))
        
        root1 = Text("x₁ = (-3 + √5) / 2 ≈ -0.382", font_size=34)
        root1.next_to(roots_text, DOWN, buff=0.4).shift(LEFT * 1.5)
        
        root2 = Text("x₂ = (-3 - √5) / 2 ≈ -2.618", font_size=34)
        root2.next_to(roots_text, DOWN*3, buff=0.4).shift(LEFT * 1.5)
        
        self.play(Write(root1), Write(root2))
        self.wait(2)
        
        # Show factored form with irrational factors
        self.play(
            FadeOut(root1),
            FadeOut(root2),
            FadeOut(roots_text)
        )
        
        factored_text = Text("Factored form (with irrational factors):", font_size=28)
        factored_text.next_to(formula, DOWN, buff=0.7)
        self.play(Write(factored_text))
        
        factored = Text("(x - (-3 + √5)/2)(x - (-3 - √5)/2) = 0", font_size=30)
        factored.next_to(factored_text, DOWN, buff=0.4)
        self.play(Write(factored))
        self.wait(3)
        
        self.play(FadeOut(factored_text, factored))
        
        # Verification box
        self.play(FadeOut(note))
        verify_box = Rectangle(
            width=11, 
            height=2.5, 
            color=GREEN,
            fill_opacity=0.1
        )
        verify_box.to_edge(DOWN, buff=0.3)
        
        verify_text = Text("Verification:", font_size=28, color=GREEN)
        verify_text.next_to(verify_box.get_top(), DOWN, buff=0.2)
        
        expand1 = Text("Expanding: x² - x(-3-√5)/2 - x(-3+√5)/2 + ((-3+√5)/2)((-3-√5)/2)", font_size=22)
        expand1.next_to(verify_text, DOWN, buff=0.2)
        
        expand2 = Text("= x² + (3x + x√5 + 3x - x√5)/2 + (9 - 5)/4", font_size=24)
        expand2.next_to(expand1, DOWN, buff=0.15)
        
        expand3 = Text("= x² + 3x + 1 ✓", font_size=26)
        expand3.next_to(expand2, DOWN, buff=0.15)
        
        check2 = Text("✓", font_size=35)
        check2.next_to(step1)
        
        self.play(Create(verify_box), Write(verify_text))
        self.wait()
        self.play(Write(expand1))
        self.wait()
        self.play(Write(expand2))
        self.wait()
        self.play(Write(expand3))
        self.wait(3)
        self.play(FadeIn(check2))
        self.wait(6)

class VisualizeImperfectFactoring(Scene):
   def construct(self):
        # Sizes for algebra tiles
        x_size = 2.0
        unit = 0.4
        
        transition_intro = Text("QUADRATIC FORMULA", font_size=50)
        self.play(FadeIn(transition_intro))
        
        transition_subtext1 = Text("Algebraic Solution", font_size=36).next_to(transition_intro, DOWN*2, buff=0.3)
        transition_subtext2 = Text("Visual Solution", color=GREEN, font_size=36).next_to(transition_subtext1, DOWN*1.2, buff=0.3)
        self.play(FadeIn(transition_subtext1, transition_subtext2))
        
        check1 = Text("✓", font_size=35)
        check1.next_to(transition_subtext2)
        self.play(FadeIn(check1))
        self.play(FadeOut(transition_subtext1))
        self.wait(2)
        self.play(FadeOut(transition_intro, transition_subtext2, check1))
        
        # Title
        title = Text("Visualization of: x² + 3x + 1", font_size=36)
        title.to_edge(UP)
        self.play(FadeIn(title))

        # Expression text
        expr = Text("x² + 3x + 1", font_size=30)
        expr.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(expr))

        # Create tiles (colors: x²=BLUE, x=GREEN, 1=YELLOW)
        x2_tile = Rectangle(width=x_size, height=x_size).set_fill(BLUE, 0.55).set_stroke(WHITE, 2)

        x_right = VGroup(*[
            Rectangle(width=unit, height=x_size).set_fill(GREEN, 0.55).set_stroke(WHITE, 2)
            for _ in range(2)
        ])
        x_bottom = VGroup(*[
            Rectangle(width=x_size, height=unit).set_fill(GREEN, 0.55).set_stroke(WHITE, 2)
            for _ in range(1)
        ])
        ones = VGroup(*[
            Square(side_length=unit).set_fill(YELLOW, 0.65).set_stroke(WHITE, 2)
            for _ in range(1)
        ])

        # Start with tiles grouped on the left and slightly UP
        all_tiles = VGroup(x2_tile, x_right, x_bottom, ones).arrange(RIGHT, buff=0.35)
        all_tiles.to_edge(LEFT, buff=0.7).shift(UP * 0.3)
        self.play(FadeIn(all_tiles, lag_ratio=0.1))
        self.wait(0.4)

        # Arrange tiles into a rectangle
        target_origin = ORIGIN + RIGHT * 1.3 + UP * 0.2
        x2_target = x2_tile.copy().move_to(target_origin)

        # Two vertical x-tiles to the RIGHT of x²
        x_right_targets = x_right.copy().arrange(RIGHT, buff=0)
        x_right_targets.next_to(x2_target, RIGHT, buff=0, aligned_edge=UP)

        # One horizontal x-tile BELOW x²
        x_bottom_targets = x_bottom.copy().arrange(DOWN, buff=0)
        x_bottom_targets.next_to(x2_target, DOWN, buff=0, aligned_edge=LEFT)

        # Single unit square at bottom-right corner
        ones_target = ones.copy()
        br_corner = x2_target.get_corner(DR)
        ones_target_center = br_corner + RIGHT * (1 * unit / 2) + DOWN * (1 * unit / 2)
        ones_target.move_to(ones_target_center)

        # Animate tiles into place
        self.play(
            x2_tile.animate.move_to(x2_target),
            Transform(x_right, x_right_targets),
            Transform(x_bottom, x_bottom_targets),
            Transform(ones, ones_target),
            run_time=2
        )
        self.wait(0.4)

        # Draw the outline of the full rectangle
        full_width = x_size + 2 * unit
        full_height = x_size + 1 * unit
        rect_outline = Rectangle(width=full_width, height=full_height).set_stroke(WHITE, 3)
        rect_outline.move_to(x2_target.get_center() + RIGHT * unit + DOWN * (unit / 2))
        self.play(Create(rect_outline))

        # Side labels using braces
        left_top = rect_outline.get_corner(UL)
        left_bot = rect_outline.get_corner(DL)
        top_left = rect_outline.get_corner(UL)
        top_right = rect_outline.get_corner(UR)

        brace_left = BraceBetweenPoints(left_bot, left_top, direction=LEFT)
        brace_top = BraceBetweenPoints(top_left, top_right, direction=UP)
        left_label = Text("(x - (-3 + √5)/2)", font_size=28).next_to(brace_left, LEFT, buff=0.2)
        top_label = Text("(x - (-3 - √5)/2)", font_size=28).next_to(brace_top, UP, buff=0.2)

        self.play(GrowFromCenter(brace_left), FadeIn(left_label))
        self.play(GrowFromCenter(brace_top), FadeIn(top_label))
        self.wait(0.4)

        # Show the factorization result
        fact_text = Text("Factor: (x - (-3 + √5)/2)(x - (-3 - √5)/2)", font_size=32).set_color(YELLOW)
        fact_text.to_edge(DOWN, buff=0.6)

        # Place the hint directly ABOVE the factor text
        hint = Text("Not a perfect square → Quadratic Formula", font_size=26)
        hint.next_to(fact_text, UP, buff=0.2)

        # Animate in this order
        self.play(FadeIn(fact_text))
        self.wait(2)
        self.play(FadeIn(hint))
        self.wait(2)
        self.bring_to_front(hint, fact_text)

        # Clean finish
        self.play(
            FadeOut(title),
            FadeOut(expr),
            FadeOut(hint),
            FadeOut(fact_text),
            FadeOut(brace_left),
            FadeOut(brace_top),
            FadeOut(left_label),
            FadeOut(top_label),
            FadeOut(x2_tile),
            FadeOut(x_right),
            FadeOut(x_bottom),
            FadeOut(ones),
            FadeOut(rect_outline)
        )
        self.wait(0.6)

        final_text = Text("The quadratic formula is used to find solutions to ANY quadratic function.", font_size = 24)
        self.play(FadeIn(final_text))
        self.wait(2)
        
        final_text2 = Text("If all other quadratic solution methods do not work, use QF!!!", color=BLUE, font_size=28).next_to(final_text, DOWN*1, buff=0.3)
        self.play(FadeIn(final_text2))
        self.wait(6)