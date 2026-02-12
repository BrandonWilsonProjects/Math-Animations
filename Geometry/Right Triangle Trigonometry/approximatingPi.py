from manim import *
import numpy as np

class ArchimedesPolygonMethod(Scene):
    def construct(self):
        # Title
        title = Text("Archimedes' Method for Approximating π", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))
        
        # Introduction text
        intro = Text(
            "Using inscribed and circumscribed polygons",
            font_size=28
        ).next_to(title, DOWN)
        self.play(FadeIn(intro))
        self.wait(2)
        self.play(FadeOut(intro))
        
        # Create circle
        circle_radius = 2
        circle = Circle(radius=circle_radius, color=BLUE)
        circle.move_to(ORIGIN)
        
        # Label for circle
        circle_label = MathTex(r"\text{Circle with radius } r = 1", font_size=32)
        circle_label.next_to(circle, DOWN, buff=0.8)
        
        self.play(Create(circle), Write(circle_label))
        self.wait()
        
        # Create display for approximations
        approximation_display = VGroup()
        n_text = MathTex(r"n = ", font_size=32)
        perimeter_inscribed = MathTex(r"P_{\text{in}} = ", font_size=28)
        perimeter_circumscribed = MathTex(r"P_{\text{out}} = ", font_size=28)
        pi_lower = MathTex(r"\pi \approx ", font_size=32, color=GREEN)
        pi_upper = MathTex(r"\pi \approx ", font_size=32, color=RED)
        
        approximation_display.add(n_text, perimeter_inscribed, 
                                 perimeter_circumscribed, pi_lower, pi_upper)
        approximation_display.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        approximation_display.to_corner(UR + DOWN * 2, buff=0.5)
        
        # Iterate through different polygon sizes
        n_values = [6, 12, 24, 48, 96]
        
        for i, n in enumerate(n_values):
            # Calculate inscribed polygon
            inscribed_vertices = [
                circle_radius * np.array([np.cos(2*np.pi*k/n), np.sin(2*np.pi*k/n), 0])
                for k in range(n)
            ]
            inscribed_polygon = Polygon(*inscribed_vertices, color=GREEN, fill_opacity=0.2)
            
            # Calculate circumscribed polygon
            circumscribed_vertices = []
            for k in range(n):
                angle = 2*np.pi*k/n
                # Tangent point on circle
                tangent_angle = angle
                # Normal at this point
                normal = np.array([np.cos(tangent_angle), np.sin(tangent_angle), 0])
                
                # Find intersection of two adjacent tangent lines
                angle_next = 2*np.pi*(k+1)/n
                
                # For a regular polygon circumscribed around a circle,
                # the radius to the midpoint of each side equals the circle radius
                # Distance from center to vertex is r/cos(π/n)
                radius_to_vertex = circle_radius / np.cos(np.pi/n)
                vertex = radius_to_vertex * np.array([
                    np.cos(angle + np.pi/n), 
                    np.sin(angle + np.pi/n), 
                    0
                ])
                circumscribed_vertices.append(vertex)
            
            circumscribed_polygon = Polygon(*circumscribed_vertices, color=RED, fill_opacity=0.1)
            
            # Calculate perimeters
            # Inscribed: perimeter = 2nr*sin(π/n)
            p_inscribed = 2 * n * circle_radius * np.sin(np.pi/n)
            # Circumscribed: perimeter = 2nr*tan(π/n)
            p_circumscribed = 2 * n * circle_radius * np.tan(np.pi/n)
            
            # π bounds (for r=1, so divide by 2r=2)
            pi_lower_bound = p_inscribed / 2
            pi_upper_bound = p_circumscribed / 2
            
            # Update text
            n_value = MathTex(r"n = " + str(n), font_size=32)
            p_in_value = MathTex(
                r"P_{\text{in}} = " + f"{p_inscribed:.4f}", 
                font_size=28
            )
            p_out_value = MathTex(
                r"P_{\text{out}} = " + f"{p_circumscribed:.4f}", 
                font_size=28
            )
            pi_low_value = MathTex(
                r"\pi > " + f"{pi_lower_bound:.5f}", 
                font_size=32, 
                color=GREEN
            )
            pi_high_value = MathTex(
                r"\pi < " + f"{pi_upper_bound:.5f}", 
                font_size=32, 
                color=RED
            )
            
            new_display = VGroup(n_value, p_in_value, p_out_value, 
                                pi_low_value, pi_high_value)
            new_display.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            new_display.to_corner(UR, buff=0.5)
            
            if i == 0:
                self.play(
                    Create(inscribed_polygon),
                    Create(circumscribed_polygon),
                    Write(new_display),
                    run_time=2
                )
                # Save references for next iteration
                inscribed_polygon_prev = inscribed_polygon
                circumscribed_polygon_prev = circumscribed_polygon
                approximation_display = new_display
            else:
                self.play(
                    Transform(inscribed_polygon_prev, inscribed_polygon),
                    Transform(circumscribed_polygon_prev, circumscribed_polygon),
                    FadeOut(approximation_display),
                    run_time=0.5
                )
                self.play(
                    FadeIn(new_display),
                    run_time=0.5
                )
                # Update the reference
                approximation_display = new_display
            
            self.wait(2)
        
        # Final conclusion
        conclusion = Text(
            "As n → ∞, both bounds converge to π ≈ 3.14159...",
            font_size=30,
            color=YELLOW
        )
        conclusion.next_to(circle, DOWN, buff=1.2)
        
        self.play(Write(conclusion))
        self.wait(3)
        
        # Fade out
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        self.wait()

class ArchimedesExplanation(Scene):
    def construct(self):
        # Explanation of the method
        title = Text("How Does It Work?", font_size=42)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()
        
        # Key insight
        insight = VGroup(
            Text("Key Insight:", font_size=32, color=YELLOW),
            Text("• Inscribed polygon: perimeter < circumference", font_size=26),
            Text("• Circumscribed polygon: perimeter > circumference", font_size=26),
            Text("• Circumference = 2πr", font_size=26),
        )
        insight.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        insight.next_to(title, DOWN, buff=0.5)
        
        for item in insight:
            self.play(Write(item))
            self.wait(0.5)
        
        self.wait(2)
        
        # Formulas
        formulas = VGroup(
            MathTex(r"\text{For } n\text{-sided polygon:}", font_size=32),
            MathTex(r"P_{\text{inscribed}} = 2nr\sin\left(\frac{\pi}{n}\right)", font_size=28),
            MathTex(r"P_{\text{circumscribed}} = 2nr\tan\left(\frac{\pi}{n}\right)", font_size=28),
            MathTex(r"\text{Therefore:}", font_size=32),
            MathTex(r"\frac{P_{\text{inscribed}}}{2r} < \pi < \frac{P_{\text{circumscribed}}}{2r}", 
                   font_size=28, color=BLUE),
        )
        formulas.arrange(DOWN, buff=0.4)
        formulas.move_to(ORIGIN)
        
        self.play(FadeOut(insight))
        self.wait(0.5)
        
        for formula in formulas:
            self.play(Write(formula))
            self.wait(0.8)
        
        self.wait(2)
        
        # Historical note
        self.play(FadeOut(formulas), title.animate.to_edge(UP))
        
        historical = VGroup(
            Text("Historical Note:", font_size=32, color=YELLOW),
            Text("Archimedes (287-212 BCE) used 96-sided polygons", font_size=24),
            Text("to show that:", font_size=24),
            MathTex(r"3\frac{10}{71} < \pi < 3\frac{1}{7}", font_size=28),
            Text("or approximately:", font_size=24),
            MathTex(r"3.1408 < \pi < 3.1429", font_size=28, color=GREEN),
        )
        historical.arrange(DOWN, buff=0.3)
        historical.move_to(ORIGIN)
        
        for item in historical:
            self.play(Write(item))
            self.wait(0.5)
        
        self.wait(3)
        self.play(FadeOut(historical), FadeOut(title))
        self.wait()