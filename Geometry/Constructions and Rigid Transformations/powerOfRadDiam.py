from manim import *
import numpy as np

config.tex_template = None  # Disable LaTeX

class RadiusDiameterPower(Scene):
    """
    A comprehensive Manim animation demonstrating the relationship
    between radius and diameter in circles.
    No LaTeX/MathTex required - uses Text only.
    """
    
    def construct(self):
        # Title scene
        self.show_title()
        self.wait(1)
        
        # Introduction to circle components
        self.introduce_circle_parts()
        self.wait(1)
        
        # Show the mathematical relationship
        self.show_relationship()
        self.wait(1)
        
        # Show area and circumference formulas
        self.show_formulas()
        self.wait(1)
        
        # Interactive radius change
        self.interactive_radius_change()
        self.wait(2)
    
    def show_title(self):
        """Display the title of the presentation."""
        title = Text("The Power of Radius & Diameter", font_size=48, weight=BOLD)
        subtitle = Text("Understanding Circle Fundamentals", font_size=28)
        subtitle.next_to(title, DOWN, buff=0.3)
        
        self.play(Write(title))
        self.play(FadeIn(subtitle, shift=UP))
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))
    
    def introduce_circle_parts(self):
        """Introduce the basic parts of a circle: center, radius, and diameter."""
        # Create circle
        circle = Circle(radius=2, color=BLUE)
        center_dot = Dot(circle.get_center(), color=RED)
        center_label = Text("Center", font_size=24).next_to(center_dot, DOWN, buff=0.3)
        
        # Create radius line
        radius_line = Line(
            circle.get_center(),
            circle.point_at_angle(PI/4),
            color=GREEN,
            stroke_width=6
        )
        radius_label = Text("Radius (r)", font_size=28, color=GREEN)
        radius_label.next_to(radius_line, UP+RIGHT, buff=0.2)
        
        # Create diameter line
        diameter_line = Line(
            circle.point_at_angle(PI),
            circle.point_at_angle(0),
            color=YELLOW,
            stroke_width=6
        )
        diameter_label = Text("Diameter (d)", font_size=28, color=YELLOW)
        diameter_label.next_to(diameter_line, DOWN*2, buff=0.2)
        
        # Animate introduction
        self.play(Create(circle))
        self.play(FadeIn(center_dot), Write(center_label))
        self.wait(0.5)
        
        self.play(Create(radius_line), Write(radius_label))
        self.wait(0.5)
        
        self.play(Create(diameter_line), Write(diameter_label))
        self.wait(1)
        
        # Clean up
        self.play(
            FadeOut(circle),
            FadeOut(center_dot),
            FadeOut(center_label),
            FadeOut(radius_line),
            FadeOut(radius_label),
            FadeOut(diameter_line),
            FadeOut(diameter_label)
        )
    
    def show_relationship(self):
        """Show the mathematical relationship between radius and diameter."""
        # Create circle with measurements
        circle = Circle(radius=1.5, color=BLUE)
        
        # Radius line
        radius_line = Line(
            circle.get_center(),
            circle.point_at_angle(0),
            color=GREEN,
            stroke_width=6
        )
        radius_brace = Brace(radius_line, direction=DOWN)
        radius_text = Text("r", font_size=32, color=GREEN).next_to(radius_brace, DOWN, buff=0.1)
        
        # Diameter line
        diameter_line = Line(
            circle.point_at_angle(PI),
            circle.point_at_angle(0),
            color=YELLOW,
            stroke_width=6
        )
        diameter_brace = Brace(diameter_line, direction=UP)
        diameter_text = Text("d", font_size=32, color=YELLOW).next_to(diameter_brace, UP, buff=0.1)
        
        # Show the elements
        self.play(Create(circle))
        self.play(
            Create(radius_line),
            GrowFromCenter(radius_brace),
            Write(radius_text)
        )
        self.wait(0.5)
        
        self.play(
            Create(diameter_line),
            GrowFromCenter(diameter_brace),
            Write(diameter_text)
        )
        self.wait(1)
        
        # Show the relationship formula
        formula = Text("d = 2r", font_size=60, color=WHITE).to_edge(DOWN, buff=1)
        formula_box = SurroundingRectangle(formula, color=ORANGE, buff=0.2)
        
        self.play(Write(formula))
        self.play(Create(formula_box))
        self.wait(1)
        
        # Alternative formula
        alt_formula = Text("r = d/2", font_size=60, color=WHITE).move_to(formula)
        
        self.play(Transform(formula, alt_formula))
        self.wait(1)
        
        # Clean up
        self.play(
            FadeOut(circle),
            FadeOut(radius_line),
            FadeOut(radius_brace),
            FadeOut(radius_text),
            FadeOut(diameter_line),
            FadeOut(diameter_brace),
            FadeOut(diameter_text),
            FadeOut(formula),
            FadeOut(formula_box)
        )
    
    def show_formulas(self):
        """Display important formulas involving radius and diameter."""
        title = Text("Key Formulas", font_size=40).to_edge(UP)
        self.play(Write(title))
        
        # Circle for reference
        circle = Circle(radius=1.5, color=BLUE).shift(LEFT * 3.5)
        radius_line = Line(
            circle.get_center(),
            circle.get_right(),
            color=GREEN,
            stroke_width=6
        )
        radius_label = Text("r", color=GREEN, font_size=36).next_to(radius_line, DOWN, buff=0.1)
        
        self.play(Create(circle), Create(radius_line), Write(radius_label))
        
        # Formulas
        formulas = VGroup(
            Text("Area: A = πr²", font_size=40, color=WHITE),
            Text("Circumference: C = 2πr", font_size=40, color=WHITE),
            Text("Or: C = πd", font_size=40, color=WHITE),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT).shift(RIGHT * 2)
        
        # Animate formulas one by one
        for formula in formulas:
            box = SurroundingRectangle(formula, color=ORANGE, buff=0.15)
            self.play(Write(formula), Create(box))
            self.wait(0.5)
            self.play(FadeOut(box))
        
        self.wait(1)
        
        # Clean up
        self.play(
            FadeOut(title),
            FadeOut(circle),
            FadeOut(radius_line),
            FadeOut(radius_label),
            FadeOut(formulas)
        )
    
    def interactive_radius_change(self):
        """Create an interactive demonstration of changing radius."""
        title = Text("Interactive Demonstration", font_size=40).to_edge(UP)
        self.play(Write(title))
        
        # Create a tracker for radius
        radius_tracker = ValueTracker(1.0)
        
        # Circle that changes with tracker
        circle = always_redraw(
            lambda: Circle(
                radius=radius_tracker.get_value(),
                color=BLUE
            )
        )
        
        # Dynamic measurements
        radius_line = always_redraw(
            lambda: Line(
                circle.get_center(),
                circle.get_right(),
                color=GREEN,
                stroke_width=5
            )
        )
        
        # Dynamic labels
        measurement_group = always_redraw(
            lambda: VGroup(
                Text(
                    f"r = {radius_tracker.get_value():.2f}",
                    color=GREEN,
                    font_size=36
                ),
                Text(
                    f"d = {radius_tracker.get_value() * 2:.2f}",
                    color=YELLOW,
                    font_size=36
                ),
                Text(
                    f"A = {np.pi * radius_tracker.get_value()**2:.2f}",
                    color=RED,
                    font_size=36
                ),
                Text(
                    f"C = {2 * np.pi * radius_tracker.get_value():.2f}",
                    color=PURPLE,
                    font_size=36
                )
            ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).to_edge(RIGHT, buff=1)
        )
        
        # Add elements
        self.add(circle, radius_line, measurement_group)
        self.wait(0.5)
        
        # Animate radius changes
        radius_values = [0.5, 1.5, 2.5, 1.8, 1.0]
        
        for target_radius in radius_values:
            self.play(
                radius_tracker.animate.set_value(target_radius),
                run_time=2,
                rate_func=smooth
            )
            self.wait(0.5)
        
        # Final message
        conclusion = Text(
            "Radius determines everything!",
            font_size=36,
            color=GOLD
        ).to_edge(DOWN, buff=0.5)
        
        self.play(Write(conclusion))
        self.wait(1)
        
        # Final clean up
        self.play(
            FadeOut(title),
            FadeOut(circle),
            FadeOut(radius_line),
            FadeOut(measurement_group),
            FadeOut(conclusion)
        )


# Additional scene for comparison
class RadiusComparison(Scene):
    """Compare multiple circles with different radii."""
    
    def construct(self):
        title = Text("Radius Comparison", font_size=48).to_edge(UP)
        self.play(Write(title))
        
        # Create circles with different radii
        radii = [0.5, 1.0, 1.5, 2.0]
        colors = [RED, GREEN, BLUE, YELLOW]
        circles = VGroup()
        labels = VGroup()
        
        for i, (r, color) in enumerate(zip(radii, colors)):
            circle = Circle(radius=r, color=color, stroke_width=4)
            circle.shift(LEFT * 5 + RIGHT * (i * 3))
            
            label = Text(f"r = {r}", font_size=28, color=color)
            label.next_to(circle, DOWN, buff=0.3)
            
            circles.add(circle)
            labels.add(label)
        
        # Animate circles appearing
        self.play(
            LaggedStart(*[Create(c) for c in circles], lag_ratio=0.3),
            LaggedStart(*[Write(l) for l in labels], lag_ratio=0.3)
        )
        
        self.wait(2)
        
        # Show area comparison
        area_title = Text("Area Comparison", font_size=36).to_edge(DOWN)
        area_formulas = VGroup()
        
        for i, r in enumerate(radii):
            area = np.pi * r**2
            formula = Text(f"A = {area:.2f}", font_size=24, color=colors[i])
            formula.next_to(labels[i], DOWN, buff=0.2)
            area_formulas.add(formula)
        
        self.play(Write(area_title))
        self.play(LaggedStart(*[Write(f) for f in area_formulas], lag_ratio=0.2))
        
        self.wait(2)
        
        self.play(FadeOut(title, circles, labels, area_formulas, area_title))
        self.wait(2)
        
        final_text = Text("Radius and diameter are crucial for measuring, designing, and building \nanything circular, from calculating the space in a round pool (area) or the material \nfor a circular garden (circumference/area) to ensuring tires fit wheels or MRI machines work \ncorrectly, allowing for precise material estimation, stability, and functionality in engineering, \nconstruction, medicine, and everyday tasks like baking or fitting plates.", font_size=24, color=PURE_GREEN)
        self.play(Write(final_text))
        self.wait(8)