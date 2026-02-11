from manim import *

class DiscriminantImportance(Scene):
    def construct(self):
        # Title
        title = Text("The Discriminant and Imaginary Numbers", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(3)
        self.play(FadeOut(title))
        
        # Show the quadratic formula
        formula_text = Text("Quadratic Formula:", font_size=32)
        formula_text.next_to(title, DOWN, buff=0.5)
        
        quadratic_formula = MathTex(
            r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}",
            font_size=44
        )
        quadratic_formula.next_to(formula_text, DOWN, buff=0.3)
        
        self.play(Write(formula_text))
        self.play(Write(quadratic_formula))
        self.wait(2)
        
        # Highlight the discriminant
        discriminant_box = SurroundingRectangle(
            quadratic_formula[0][8:15],  # b^2 - 4ac
            color=YELLOW,
            buff=0.1
        )
        
        discriminant_label = MathTex(
            r"\Delta = b^2 - 4ac",
            color=YELLOW,
            font_size=36
        )
        discriminant_label.next_to(quadratic_formula, DOWN, buff=0.5)
        
        self.play(Create(discriminant_box))
        self.play(Write(discriminant_label))
        self.wait(2)
        
        # Move everything up to make room
        group = VGroup(formula_text, quadratic_formula, discriminant_box, discriminant_label)
        self.play(group.animate.shift(UP * 1.5))
        
        # Three cases
        cases_title = Text("Three Cases:", font_size=32)
        cases_title.move_to(DOWN * 0.5)
        self.play(Write(cases_title))
        self.wait()
        
        self.play(FadeOut(cases_title, discriminant_box, discriminant_label, quadratic_formula, formula_text))
        
        # Case 1: Two real roots (Δ > 0)
        self.show_case_one(quadratic_formula, discriminant_label)
        
        # Case 2: One real root (Δ = 0)
        self.show_case_two(quadratic_formula, discriminant_label)
        
        # Case 3: Two imaginary roots (Δ < 0)
        self.show_case_three(quadratic_formula, discriminant_label)
        
        self.wait(2)

    def show_case_one(self, formula, disc_label):
        """Case 1: Δ > 0 - Two distinct real roots"""
        case1_title = Text("Case 1: Δ > 0", font_size=32, color=GREEN)
        case1_title.to_edge(LEFT).shift(UP * 0.5 + RIGHT * 1)
        
        example1 = MathTex(r"x^2 - 5x + 6 = 0", font_size=36)
        example1.next_to(case1_title, DOWN, buff=0.3)
        
        calc1 = MathTex(
            r"\Delta = (-5)^2 - 4(1)(6) = 25 - 24 = 1 > 0",
            font_size=28,
            color=GREEN
        )
        calc1.next_to(example1, DOWN, buff=0.2)
        
        roots1 = MathTex(r"x = 2 \text{ or } x = 3", font_size=32)
        roots1.next_to(calc1, DOWN, buff=0.2)
        
        # Graph
        axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 3, 1],
            x_length=4,
            y_length=3,
            tips=False
        ).scale(0.5)
        
        parabola = axes.plot(lambda x: x**2 - 5*x + 6, color=BLUE)
        dots = VGroup(
            Dot(axes.c2p(2, 0), color=RED),
            Dot(axes.c2p(3, 0), color=RED)
        )
        
        self.play(Write(case1_title))
        self.play(Write(example1))
        self.play(Write(calc1))
        self.play(Write(roots1))
        self.play(Create(axes), Create(parabola), Create(dots))
        self.wait(3)
        
        self.play(
            FadeOut(case1_title), FadeOut(example1), FadeOut(calc1),
            FadeOut(roots1), FadeOut(axes), FadeOut(parabola), FadeOut(dots)
        )

    def show_case_two(self, formula, disc_label):
        """Case 2: Δ = 0 - One repeated real root"""
        case2_title = Text("Case 2: Δ = 0", font_size=32, color=ORANGE)
        case2_title.to_edge(LEFT).shift(UP * 0.5 + RIGHT * 1)
        
        example2 = MathTex(r"x^2 - 4x + 4 = 0", font_size=36)
        example2.next_to(case2_title, DOWN, buff=0.3)
        
        calc2 = MathTex(
            r"\Delta = (-4)^2 - 4(1)(4) = 16 - 16 = 0",
            font_size=28,
            color=ORANGE
        )
        calc2.next_to(example2, DOWN, buff=0.2)
        
        roots2 = MathTex(r"x = 2 \text{ (repeated)}", font_size=32)
        roots2.next_to(calc2, DOWN, buff=0.2)
        
        # Graph
        axes = Axes(
            x_range=[-1, 5, 1],
            y_range=[-1, 3, 1],
            x_length=4,
            y_length=3,
            tips=False
        ).scale(0.5)
        
        parabola = axes.plot(lambda x: (x-2)**2, color=BLUE)
        dot = Dot(axes.c2p(2, 0), color=RED)
        
        self.play(Write(case2_title))
        self.play(Write(example2))
        self.play(Write(calc2))
        self.play(Write(roots2))
        self.play(Create(axes), Create(parabola), Create(dot))
        self.wait(3)
        
        self.play(
            FadeOut(case2_title), FadeOut(example2), FadeOut(calc2),
            FadeOut(roots2), FadeOut(axes), FadeOut(parabola), FadeOut(dot)
        )

    def show_case_three(self, formula, disc_label):
        """Case 3: Δ < 0 - Two complex (imaginary) roots"""
        case3_title = Text("Case 3: Δ < 0", font_size=32, color=RED)
        case3_title.to_edge(LEFT).shift(UP * 0.5 + RIGHT * 1)
        
        example3 = MathTex(r"x^2 + 2x + 5 = 0", font_size=36)
        example3.next_to(case3_title, DOWN, buff=0.3)
        
        calc3 = MathTex(
            r"\Delta = (2)^2 - 4(1)(5) = 4 - 20 = -16 < 0",
            font_size=28,
            color=RED
        )
        calc3.next_to(example3, DOWN, buff=0.2)
        
        question = Text("What does this mean?", font_size=28, color=YELLOW)
        question.next_to(calc3, DOWN, buff=0.3)
        
        self.play(Write(case3_title))
        self.play(Write(example3))
        self.play(Write(calc3))
        self.play(Write(question))
        self.wait(2)
        
        # Graph showing no x-intercepts
        axes = Axes(
            x_range=[-4, 2, 1],
            y_range=[0, 8, 2],
            x_length=4,
            y_length=3,
            tips=False
        ).scale(0.5)
                
        parabola = axes.plot(lambda x: x**2 + 2*x + 5, color=BLUE)
        no_intersect = Text("No x-intercepts!", font_size=20, color=RED)
        no_intersect.next_to(axes, DOWN)
        
        self.play(Create(axes), Create(parabola))
        self.play(Write(no_intersect))
        self.wait(2)
        
        # Show the imaginary roots
        self.play(FadeOut(question), FadeOut(no_intersect))
        
        sqrt_step = MathTex(
            r"x = \frac{-2 \pm \sqrt{-16}}{2}",
            font_size=32
        )
        sqrt_step.next_to(calc3, DOWN, buff=0.3)
        
        self.play(Write(sqrt_step))
        self.wait(2)
        
        imaginary_intro = MathTex(
            r"\sqrt{-16} = \sqrt{16} \cdot \sqrt{-1} = 4i",
            font_size=32,
            color=YELLOW
        )
        imaginary_intro.next_to(sqrt_step, DOWN, buff=0.3)
        
        self.play(Write(imaginary_intro))
        self.wait(2)
        
        final_roots = MathTex(
            r"x = -1 + 2i \text{ or } x = -1 - 2i",
            font_size=32,
            color=GREEN
        )
        final_roots.next_to(imaginary_intro, DOWN, buff=0.3)
        
        self.play(Write(final_roots))
        self.wait(2)
        
        # Define i
        i_definition = MathTex(
            r"i = \sqrt{-1}",
            font_size=40,
            color=YELLOW
        )
        i_definition.move_to(ORIGIN)
        
        self.play(
            FadeOut(case3_title), FadeOut(example3), FadeOut(calc3),
            FadeOut(sqrt_step), FadeOut(imaginary_intro), FadeOut(final_roots),
            FadeOut(axes), FadeOut(parabola)
        )
        
        self.play(Write(i_definition))
        self.wait(3)


class DiscriminantSummary(Scene):
    def construct(self):
        """Summary scene showing all three cases"""
        title = Text("The Discriminant Determines Root Type", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Create a table
        table_data = [
            ["Δ > 0", "Two distinct real roots"],
            ["Δ = 0", "One repeated real root"],
            ["Δ < 0", "Two complex roots (a ± bi)"]
        ]
        
        colors = [GREEN, ORANGE, RED]
        
        y_pos = 1.5
        for i, (condition, result) in enumerate(table_data):
            cond_text = Text(condition, font_size=36, color=colors[i])
            cond_text.move_to(LEFT * 3 + UP * y_pos)
            
            arrow = Arrow(LEFT * 1.5 + UP * y_pos, RIGHT * 0 + UP * y_pos, buff=0.1)
            
            result_text = Text(result, font_size=28)
            result_text.move_to(RIGHT * 3 + UP * y_pos)
            
            self.play(Write(cond_text), Create(arrow), Write(result_text))
            self.wait()
            
            y_pos -= 1.5
        
        # Final message
        conclusion = Text(
            "Imaginary numbers extend our number system\nto solve ALL quadratic equations!",
            font_size=28,
            color=YELLOW
        )
        conclusion.to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(3)