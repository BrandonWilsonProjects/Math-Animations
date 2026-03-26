from manim import *

class QuotientPropertyOfLogarithms(Scene):
    def construct(self):
        # ==================== TITLE ====================
        title = Text("Quotient Property of Logarithms", 
                     font_size=48, 
                     gradient=(BLUE, PURPLE))
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # ==================== MAIN PROPERTY ====================
        property_tex = MathTex(
            r"\log_b \left( \frac{x}{y} \right) = \log_b x - \log_b y",
            font_size=52,
            color=YELLOW
        ).next_to(title, DOWN, buff=0.8)
        
        self.play(Write(property_tex))
        self.wait(5)
        self.play(FadeOut(property_tex))

        # ==================== DERIVATION ====================
        deriv_title = Text("Derivation (Mechanics)", 
                           font_size=36, 
                           color=WHITE).next_to(property_tex, DOWN, buff=1.0)
        self.play(Write(deriv_title))
        self.play(FadeOut(deriv_title))

        steps = [
            r"1.\quad \text{Let } k = \log_b \left( \frac{x}{y} \right)",
            r"2.\quad \implies b^k = \frac{x}{y}",
            r"3.\quad \implies x = b^k \cdot y",
            r"4.\quad \text{Substitute } y = b^{\log_b y}",
            r"5.\quad \implies x = b^k \cdot b^{\log_b y} = b^{k + \log_b y}",
            r"6.\quad \implies k + \log_b y = \log_b x",
            r"7.\quad \implies k = \log_b x - \log_b y",
        ]

        for i, step_text in enumerate(steps):
            # Create the current step
            current_step = MathTex(step_text, font_size=42)
            current_step.move_to(ORIGIN)   # Perfectly centered

            # Add a small step number indicator
            step_num = Text(f"Step {i+1}/7", font_size=28, color=GRAY).next_to(current_step, UP, buff=0.8)
            
            # Show the step
            self.play(
                FadeIn(current_step, shift=UP*0.3),
                FadeIn(step_num),
                run_time=0.8
            )
            
            self.wait(4.0)   # Hold for 4 seconds as requested
            
            # Fade out before next step
            self.play(
                FadeOut(current_step),
                FadeOut(step_num),
                run_time=0.6
            )

        # After all steps, show the final result prominently
        final_result = MathTex(
            r"\log_b x - \log_b y = \log_b \left( \frac{x}{y} \right)",
            font_size=52,
            color=GREEN_B
        )
        final_label = Text("Final Result: Quotient Rule for Logarithms", 
                          font_size=36, color=GOLD).next_to(final_result, UP, buff=0.7)

        self.play(
            FadeIn(final_result),
            FadeIn(final_label),
            run_time=1.2
        )
        self.wait(4)
        
        self.play(FadeOut(final_label, final_result))

        # ==================== NUMERICAL EXAMPLE ====================
        self.play(
            FadeOut(deriv_title))

        example_title = Text("Numerical Example", 
                             font_size=36, 
                             color=ORANGE).next_to(title, DOWN, buff=1.2)
        self.play(Write(example_title))

        left = MathTex(r"\log_2 \left( \frac{16}{4} \right)").scale(1.1)
        right = MathTex(r"\log_2 16 - \log_2 4").scale(1.1)
        
        equation = VGroup(left, MathTex("="), right).arrange(RIGHT, buff=0.5)
        equation.next_to(example_title, DOWN, buff=0.8)

        self.play(Write(equation))
        self.wait(1.5)

        # Calculation
        calc1 = MathTex(r"= 4 - 2").next_to(equation, DOWN, buff=0.6)
        calc2 = MathTex(r"= 2").next_to(calc1, DOWN, buff=0.4)
        
        self.play(Write(calc1))
        self.wait(0.8)
        self.play(Write(calc2))
        self.wait(1)