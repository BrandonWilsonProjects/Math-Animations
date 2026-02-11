from manim import *

class RightTriangleTrigIntro(Scene):
    def construct(self):
        # Title
        title = Text("Right Triangle Ratios", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(3)
        self.play(FadeOut(title))
        
        # Question text
        question = VGroup(
            Text("In a right triangle, which ratios stay the same", font_size=28),
            Text("when the triangle gets bigger?", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT)
        question.to_edge(UP, buff=0.5)
        self.play(FadeIn(question))
        self.wait(2)
        
        # Fade out question
        self.play(FadeOut(question))
        self.wait(0.5)
        
        # Create the first small triangle
        scale1 = 1.5
        base1 = 3 * scale1
        height1 = 2 * scale1
        
        triangle1 = self.create_right_triangle(base1, height1, BLUE)
        triangle1.shift(LEFT * 2 + DOWN * 0.5)
        
        # Create labels for first triangle
        labels1 = self.create_labels(triangle1, base1, height1)
        
        self.play(Create(triangle1), run_time=2)
        self.wait(0.5)
        self.play(Write(labels1))
        self.wait(1)
        
        # Calculate and display measurements for first triangle
        hyp1 = np.sqrt(base1**2 + height1**2)
        measurements1, ratios1 = self.create_measurements(base1, height1, hyp1, triangle1, "Small Triangle")
        measurements1.to_edge(RIGHT).shift(UP * 1.5)
        ratios1.to_edge(LEFT).shift(UP * 1.5)
        
        self.play(FadeIn(measurements1), FadeIn(ratios1))
        self.wait(2)
        
        # Fade out measurements before transforming triangle
        self.play(FadeOut(measurements1), FadeOut(ratios1), FadeOut(labels1))
        self.wait(0.5)
        
        # Now create a larger similar triangle
        scale2 = 2.5
        base2 = 3 * scale2
        height2 = 2 * scale2
        
        triangle2 = self.create_right_triangle(base2, height2, GREEN)
        triangle2.shift(LEFT * 2 + DOWN * 0.5)
        
        labels2 = self.create_labels(triangle2, base2, height2)
        
        # Transform to larger triangle
        self.play(
            Transform(triangle1, triangle2),
            run_time=2
        )
        self.wait(0.5)
        self.play(Write(labels2))
        self.wait(1)
        
        # Show both measurements and ratios side by side
        # Recreate measurements for small triangle
        measurements1_display, ratios1_display = self.create_measurements(base1, height1, hyp1, None, "Small Triangle")
        measurements1_display.to_corner(DR).shift(LEFT * 7)
        ratios1_display.to_edge(LEFT).shift(UP * 1.5)
        
        # Create measurements for large triangle
        hyp2 = np.sqrt(base2**2 + height2**2)
        measurements2, ratios2 = self.create_measurements(base2, height2, hyp2, None, "Large Triangle")
        measurements2.to_corner(DR)
        
        self.play(FadeIn(measurements1_display), FadeIn(ratios1_display))
        self.wait(1)
        self.play(FadeIn(measurements2))
        self.wait(2)
        
        # Highlight the ratios section
        ratio_highlight = SurroundingRectangle(
            VGroup(ratios1_display, ratios2),
            color=RED,
            stroke_width=4,
            buff=0.3
        )
        
        self.play(Create(ratio_highlight))
        self.wait(1)
        
        # Create revelation text
        revelation = VGroup(
            Text("The RATIOS stay the same!", font_size=36, color=YELLOW),
            Text("The LENGTHS change!", font_size=30, color=WHITE)
        ).arrange(DOWN, buff=0.3)
        revelation.move_to(ORIGIN + RIGHT * 1)
        
        self.play(Write(revelation))
        self.wait(3)
        
        # Fade everything out
        self.play(
            FadeOut(triangle1),
            FadeOut(labels2),
            FadeOut(measurements1_display),
            FadeOut(ratios1_display),
            FadeOut(measurements2),
            FadeOut(ratio_highlight),
            FadeOut(revelation)
        )
        self.wait(0.5)
        
        # Final concept introduction - one line at a time
        concept_lines = [
            Text("This is the birth of TRIGONOMETRY", font_size=40, color=BLUE),
            Text("These constant ratios have special names:", font_size=28),
            Text("• height ÷ hypotenuse = SINE", font_size=26, color=GREEN),
            Text("• base ÷ hypotenuse = COSINE", font_size=26, color=ORANGE),
            Text("• height ÷ base = TANGENT", font_size=26, color=PURPLE)
        ]
        
        concept = VGroup(*concept_lines).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        concept.move_to(ORIGIN)
        
        # Show first line
        self.play(Write(concept_lines[0]))
        self.wait(1.5)
        
        # Show second line
        self.play(Write(concept_lines[1]))
        self.wait(1)
        
        # Show each ratio definition one at a time
        self.play(Write(concept_lines[2]))
        self.wait(1)
        self.play(Write(concept_lines[3]))
        self.wait(1)
        self.play(Write(concept_lines[4]))
        self.wait(3)
    
    def create_right_triangle(self, base, height, color):
        """Create a right triangle with given dimensions"""
        # Points of the triangle
        A = ORIGIN
        B = RIGHT * base
        C = UP * height
        
        triangle = Polygon(A, B, C, color=color, stroke_width=3, fill_opacity=0)
        
        # Add right angle marker at point A (origin) where the right angle is
        square_size = 0.3
        right_angle = Square(side_length=square_size, color=color, stroke_width=2, fill_opacity=0)
        right_angle.move_to(A + RIGHT * square_size/2 + UP * square_size/2)
        
        return VGroup(triangle, right_angle)
    
    def create_labels(self, triangle, base, height):
        """Create labels for the triangle sides"""
        # Get the triangle vertices
        vertices = triangle[0].get_vertices()
        
        # Base label
        base_label = MathTex(f"\\text{{base}} = {base:.1f}", font_size=24)
        base_label.next_to(
            Line(vertices[0], vertices[1]).get_center(),
            DOWN,
            buff=0.3
        )
        
        # Height label
        height_label = MathTex(f"\\text{{height}} = {height:.1f}", font_size=24)
        height_label.next_to(
            Line(vertices[2], vertices[0]).get_center(),
            LEFT,
            buff=0.3
        )
        
        # Hypotenuse label
        hyp = np.sqrt(base**2 + height**2)
        hyp_label = MathTex(f"\\text{{hyp}} = {hyp:.1f}", font_size=24)
        hyp_label.next_to(
            Line(vertices[1], vertices[2]).get_center(),
            UR,
            buff=0.2
        )
        
        return VGroup(base_label, height_label, hyp_label)
    
    def create_measurements(self, base, height, hyp, triangle, name):
        """Create measurements display and separate ratios display"""
        # Measurements box (on the right)
        measurements = VGroup(
            Text(name, font_size=28, weight=BOLD),
            Text(f"Base: {base:.1f}", font_size=22),
            Text(f"Height: {height:.1f}", font_size=22),
            Text(f"Hypotenuse: {hyp:.2f}", font_size=22),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        
        measurements_box = SurroundingRectangle(measurements, color=WHITE, buff=0.2)
        measurements_group = VGroup(measurements, measurements_box)
        
        # Ratios box (on the left)
        ratios = VGroup(
            Text("Ratios:", font_size=24, weight=BOLD, color=YELLOW),
            MathTex(f"\\frac{{\\text{{height}}}}{{\\text{{base}}}} = {height/base:.2f}", font_size=22, color=YELLOW),
            MathTex(f"\\frac{{\\text{{height}}}}{{\\text{{hyp}}}} = {height/hyp:.2f}", font_size=22, color=YELLOW),
            MathTex(f"\\frac{{\\text{{base}}}}{{\\text{{hyp}}}} = {base/hyp:.2f}", font_size=22, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        
        ratios_box = SurroundingRectangle(ratios, color=YELLOW, buff=0.2)
        ratios_group = VGroup(ratios, ratios_box)
        
        # Return both groups separately so they can be positioned independently
        return measurements_group, ratios_group


class RightTriangleScaling(Scene):
    """Alternative version with continuous scaling"""
    def construct(self):
        # Title
        title = Text("What Stays the Same?", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()
        
        # Create initial triangle
        angle = 33.69  # arctan(2/3) in degrees
        base_tracker = ValueTracker(3)
        
        # Create triangle that updates with tracker
        triangle = always_redraw(
            lambda: self.create_triangle_with_labels(base_tracker.get_value(), angle)
        )
        
        # Create ratio display
        ratio_display = always_redraw(
            lambda: self.create_ratio_display(base_tracker.get_value(), angle)
        )
        ratio_display.to_edge(RIGHT).shift(UP * 0.5)
        
        self.play(Create(triangle))
        self.play(FadeIn(ratio_display))
        self.wait()
        
        # Scale the triangle up and down
        self.play(base_tracker.animate.set_value(6), run_time=3, rate_func=smooth)
        self.wait()
        self.play(base_tracker.animate.set_value(2), run_time=3, rate_func=smooth)
        self.wait()
        self.play(base_tracker.animate.set_value(4.5), run_time=3, rate_func=smooth)
        self.wait(2)
        
        # Key insight
        insight = Text("The ratios never change!", font_size=40, color=YELLOW)
        insight.to_edge(DOWN)
        self.play(Write(insight))
        self.wait(3)
    
    def create_triangle_with_labels(self, base, angle_deg):
        """Create triangle with labels that scales based on base"""
        height = base * np.tan(angle_deg * DEGREES)
        
        A = ORIGIN
        B = RIGHT * base
        C = UP * height
        
        triangle = Polygon(A, B, C, color=BLUE, stroke_width=3)
        
        # Right angle marker
        square_size = 0.3
        right_angle = Square(side_length=square_size, color=BLUE, stroke_width=2)
        right_angle.move_to(B + UP * square_size/2 + LEFT * square_size/2)
        
        # Angle arc
        arc = Arc(
            radius=0.5,
            start_angle=0,
            angle=angle_deg * DEGREES,
            color=YELLOW,
            stroke_width=2
        )
        arc.shift(B)
        
        angle_label = MathTex("\\theta", font_size=24, color=YELLOW)
        angle_label.next_to(arc, UP + LEFT, buff=0.1)
        
        result = VGroup(triangle, right_angle, arc, angle_label)
        result.move_to(LEFT * 2.5 + DOWN * 0.5)
        
        return result
    
    def create_ratio_display(self, base, angle_deg):
        """Create display of current measurements and ratios"""
        height = base * np.tan(angle_deg * DEGREES)
        hyp = np.sqrt(base**2 + height**2)
        
        display = VGroup(
            Text("Measurements:", font_size=28, weight=BOLD),
            Text(f"Base: {base:.2f}", font_size=24),
            Text(f"Height: {height:.2f}", font_size=24),
            Text(f"Hypotenuse: {hyp:.2f}", font_size=24),
            Text("", font_size=20),
            Text("Ratios:", font_size=28, weight=BOLD, color=YELLOW),
            Text(f"h ÷ b = {height/base:.3f}", font_size=24, color=YELLOW),
            Text(f"h ÷ hyp = {height/hyp:.3f}", font_size=24, color=YELLOW),
            Text(f"b ÷ hyp = {base/hyp:.3f}", font_size=24, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        
        box = SurroundingRectangle(display, color=WHITE, buff=0.2)
        
        return VGroup(display, box)