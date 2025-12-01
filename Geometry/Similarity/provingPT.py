from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # Parameters - adjusted for better visibility
        a = 1.5  # shorter leg
        b = 2.0  # longer leg
        c = np.sqrt(a**2 + b**2)  # hypotenuse
        
        # Title
        title = Text("Pythagorean Theorem Visual Proof", font_size=48)
        title.to_edge(UP)
        self.play(Write(title), run_time=2)
        self.wait(2)
        
        intro = Text("First arrangement:", font_size=36)
        intro.to_edge(UP)
        self.play(Transform(title, intro))
        self.wait(1)
        
        # ===== LEFT FIGURE =====
        self.construct_left_figure(a, b, title)
        
        # ===== TRANSITION =====
        self.transition_to_right()
        
        # ===== RIGHT FIGURE =====
        self.construct_right_figure(a, b)
        
        # ===== CONCLUSION =====
        self.show_conclusion()
        
    def construct_left_figure(self, a, b, title):

        # Create outer square
        square_size = a + b
        outer_square = Square(side_length=square_size, color=WHITE, stroke_width=4)
        outer_square.move_to(ORIGIN)
        
        self.play(Create(outer_square), run_time=2)
        self.wait(1)
        
        # Label the outer square sides
        top_label = Text(f"a + b", font_size=28, color=YELLOW)
        top_label.next_to(outer_square, UP, buff=0.2)
        
        right_label = Text(f"a + b", font_size=28, color=YELLOW)
        right_label.next_to(outer_square, RIGHT, buff=0.2)
        
        self.play(Write(top_label), Write(right_label), run_time=1.5)
        self.wait(1.5)
        
        # Show that area is (a+b)²
        area_text = Text("Area = (a+b)²", font_size=32, color=YELLOW)
        area_text.next_to(outer_square, DOWN, buff=1.0)
        self.play(Write(area_text), run_time=1.5)
        self.wait(2)
        
        # Now let's break it into pieces - TRANSFORM from area_text
        break_text = Text("Let's divide this square into pieces...", font_size=32)
        break_text.next_to(outer_square, DOWN, buff=1.0)
        self.play(Transform(area_text, break_text))
        self.wait(1)
        
        # Create the four triangles ONE BY ONE
        # Triangle 1: Top-left
        tri1_points = [
            outer_square.get_corner(UL),
            outer_square.get_corner(UL) + RIGHT * b,
            outer_square.get_corner(UL) + DOWN * b,
        ]
        tri1 = Polygon(*tri1_points, fill_color="#F4A460", fill_opacity=0.8, stroke_color=BLACK, stroke_width=2)
        
        tri1_text = Text("Triangle 1", font_size=24)
        tri1_text.next_to(outer_square, LEFT, buff=0.5)
        
        self.play(FadeIn(tri1), Write(tri1_text), run_time=2)
        self.wait(1.5)
        
        # Label its sides
        label_a1 = Text("a", font_size=24, color=BLACK)
        label_a1.next_to(tri1.get_center(), UP, buff=0.3).shift(LEFT * 0.3)
        label_b1 = Text("b", font_size=24, color=BLACK)
        label_b1.next_to(tri1.get_center(), LEFT, buff=0.3).shift(UP * 0.3)
        
        self.play(Write(label_a1), Write(label_b1), run_time=1)
        self.wait(1.5)
        self.play(FadeOut(tri1_text), FadeOut(label_a1), FadeOut(label_b1), run_time=0.8)
        
        # Triangle 2: Top-right
        tri2_points = [
            outer_square.get_corner(UR),
            outer_square.get_corner(UR) + DOWN * a,
            outer_square.get_corner(UR) + LEFT * a,
        ]
        tri2 = Polygon(*tri2_points, fill_color="#F4A460", fill_opacity=0.8, stroke_color=BLACK, stroke_width=2)
        
        tri2_text = Text("Triangle 2", font_size=24)
        tri2_text.next_to(outer_square, LEFT, buff=0.5)
        
        self.play(FadeIn(tri2), Write(tri2_text), run_time=2)
        self.wait(2)
        self.play(FadeOut(tri2_text), run_time=0.8)
        
        # Triangle 3: Bottom-left
        tri3_points = [
            outer_square.get_corner(DL),
            outer_square.get_corner(DL) + UP * a,
            outer_square.get_corner(DL) + RIGHT * a,
        ]
        tri3 = Polygon(*tri3_points, fill_color="#F4A460", fill_opacity=0.8, stroke_color=BLACK, stroke_width=2)
        
        tri3_text = Text("Triangle 3", font_size=24)
        tri3_text.next_to(outer_square, LEFT, buff=0.5)
        
        self.play(FadeIn(tri3), Write(tri3_text), run_time=2)
        self.wait(2)
        self.play(FadeOut(tri3_text), run_time=0.8)
        
        # Triangle 4: Bottom-right
        tri4_points = [
            outer_square.get_corner(DR),
            outer_square.get_corner(DR) + LEFT * b,
            outer_square.get_corner(DR) + UP * b,
        ]
        tri4 = Polygon(*tri4_points, fill_color="#F4A460", fill_opacity=0.8, stroke_color=BLACK, stroke_width=2)
        
        tri4_text = Text("Triangle 4", font_size=24)
        tri4_text.next_to(outer_square, LEFT, buff=0.5)
        
        self.play(FadeIn(tri4), Write(tri4_text), run_time=2)
        self.wait(2)
        
        # TRANSFORM break_text to "Four identical triangles"
        all_tri_text = Text("Four identical triangles", font_size=28, color=ORANGE)
        all_tri_text.next_to(outer_square, DOWN, buff=1.0)
        self.play(
            Transform(area_text, all_tri_text),
            FadeOut(tri4_text),
            run_time=1.5
        )
        self.wait(2)
        
        # Now add the squares
        # Small square (a²) - top right
        small_square = Square(side_length=a, fill_color="#90EE90", fill_opacity=0.8, stroke_color=BLACK, stroke_width=2)
        small_square.move_to(outer_square.get_corner(UR) + LEFT * a/2 + DOWN * a/2)
        
        small_sq_text = Text("Small square with area a²", font_size=24)
        small_sq_text.next_to(outer_square, LEFT, buff=0.5)
        
        self.play(FadeIn(small_square), Write(small_sq_text), run_time=2)
        self.wait(2)
        
        label_a_sq = Text("a²", font_size=28, color=BLACK, weight=BOLD)
        label_a_sq.move_to(small_square)
        self.play(Write(label_a_sq), run_time=1)
        self.wait(2)
        self.play(FadeOut(small_sq_text), run_time=0.8)
        
        # Large rectangle (b²) - bottom left  
        large_square = Square(side_length=b, fill_color="#F0E68C", fill_opacity=0.8, stroke_color=BLACK, stroke_width=2)
        large_square.move_to(outer_square.get_corner(DL) + RIGHT * b/2 + UP * b/2)
        
        large_sq_text = Text("Larger square with area b²", font_size=24)
        large_sq_text.next_to(outer_square, LEFT, buff=0.5)
        
        self.play(FadeIn(large_square), Write(large_sq_text), run_time=2)
        self.wait(2)
        
        label_b_sq = Text("b²", font_size=28, color=BLACK, weight=BOLD)
        label_b_sq.move_to(large_square)
        self.play(Write(label_b_sq), run_time=1)
        self.wait(2)
        self.play(FadeOut(large_sq_text), run_time=0.8)
        
        # TRANSFORM "Four identical triangles" to "Let's calculate the total area"
        calc_intro = Text("Let's calculate the total area:", font_size=32)
        calc_intro.next_to(outer_square, DOWN, buff=1.0)
        self.play(Transform(area_text, calc_intro), run_time=1.5)
        self.wait(2)
        
        # Area breakdown
        area_calc1 = Text("Area = 4 triangles + small square + large square", font_size=28)
        area_calc1.next_to(area_text, DOWN, buff=0.4)
        self.play(Write(area_calc1), run_time=2)
        self.wait(2)
        
        area_calc2 = Text("Area = 4×(½ab) + a² + b²", font_size=28)
        area_calc2.next_to(area_calc1, DOWN, buff=0.3)
        self.play(Write(area_calc2), run_time=2)
        self.wait(2)
        
        area_calc3 = Text("Area = 2ab + a² + b²", font_size=28, color=GREEN)
        area_calc3.next_to(area_calc2, DOWN, buff=0.3)
        self.play(Write(area_calc3), run_time=2)
        self.wait(3)
        
        # Store everything for transition
        self.left_group = VGroup(
            outer_square, top_label, right_label, area_text,
            tri1, tri2, tri3, tri4,
            small_square, large_square,
            label_a_sq, label_b_sq,
            area_calc1, area_calc2, area_calc3
        )
        
        # Store title separately to keep it
        self.title = title
        
    def transition_to_right(self):
        transition_text = Text("Now let's rearrange these SAME pieces", font_size=40, color=YELLOW)
        transition_text.move_to(ORIGIN)
        
        self.play(FadeOut(self.left_group), run_time=2)
        self.wait(1)
        self.play(Write(transition_text), run_time=2)
        self.wait(3)
        self.play(FadeOut(transition_text), run_time=1.5)
        self.wait(1)
        
    def construct_right_figure(self, a, b):
        # TRANSFORM title to "Second arrangement"
        intro = Text("Second arrangement:", font_size=36)
        intro.to_edge(UP)
        self.play(Transform(self.title, intro))
        self.wait(1)
        
        # Create same outer square
        square_size = a + b
        outer_square = Square(side_length=square_size, color=WHITE, stroke_width=4)
        outer_square.move_to(ORIGIN)
        
        self.play(Create(outer_square), run_time=2)
        self.wait(1)
        
        # Label the outer square sides (same as before)
        top_label = Text(f"a + b", font_size=28, color=YELLOW)
        top_label.next_to(outer_square, UP, buff=0.2)
        
        right_label = Text(f"a + b", font_size=28, color=YELLOW)
        right_label.next_to(outer_square, RIGHT, buff=0.2)
        
        self.play(Write(top_label), Write(right_label), run_time=1.5)
        self.wait(1)
        
        # Show that area is still (a+b)²
        area_text = Text("Area = (a+b)² (same as before)", font_size=32, color=YELLOW)
        area_text.next_to(outer_square, DOWN, buff=1.0)
        self.play(Write(area_text), run_time=1.5)
        self.wait(2)
        
        # Now show the tilted square in the middle
        # Calculate the position - square rotated 45 degrees, side length c
        # The vertices are at distance 'b' from top, 'a' from right, 'b' from bottom, 'a' from left
        top_vertex = outer_square.get_corner(UP) + DOWN * b
        right_vertex = outer_square.get_corner(RIGHT) + LEFT * b
        bottom_vertex = outer_square.get_corner(DOWN) + UP * b
        left_vertex = outer_square.get_corner(LEFT) + RIGHT * b
        
        center_square = Polygon(
            top_vertex, right_vertex, bottom_vertex, left_vertex,
            fill_color="#87CEEB", fill_opacity=0.8, stroke_color=BLACK, stroke_width=3
        )
        
        center_text = Text("Tilted square with area c²", font_size=28)
        center_text.next_to(outer_square, LEFT, buff=0.5)
        
        self.play(FadeIn(center_square), Write(center_text), run_time=2)
        self.wait(2)
        
        label_c_sq = Text("c²", font_size=32, color=BLACK, weight=BOLD)  # Changed from RED to BLACK
        label_c_sq.move_to(center_square)
        self.play(Write(label_c_sq), run_time=1)
        self.wait(2)
        self.play(FadeOut(center_text), run_time=0.8)
        
        # Now add the four triangles in the corners
        corner_text = Text("Same 4 triangles in the corners", font_size=24, color=ORANGE)
        corner_text.next_to(outer_square, LEFT, buff=0.5)
        self.play(Write(corner_text), run_time=1.5)
        self.wait(2)
        
        # Top triangle
        tri_top = Polygon(
            outer_square.get_corner(UL),
            outer_square.get_corner(UR),
            top_vertex,
            fill_color="#F4A460", fill_opacity=0.8, stroke_color=BLACK, stroke_width=2
        )
        self.play(FadeIn(tri_top), run_time=1.5)
        self.wait(1)
        
        # Right triangle
        tri_right = Polygon(
            outer_square.get_corner(UR),
            outer_square.get_corner(DR),
            right_vertex,
            fill_color="#F4A460", fill_opacity=0.8, stroke_color=BLACK, stroke_width=2
        )
        self.play(FadeIn(tri_right), run_time=1.5)
        self.wait(1)
        
        # Bottom triangle
        tri_bottom = Polygon(
            outer_square.get_corner(DR),
            outer_square.get_corner(DL),
            bottom_vertex,
            fill_color="#F4A460", fill_opacity=0.8, stroke_color=BLACK, stroke_width=2
        )
        self.play(FadeIn(tri_bottom), run_time=1.5)
        self.wait(1)
        
        # Left triangle
        tri_left = Polygon(
            outer_square.get_corner(DL),
            outer_square.get_corner(UL),
            left_vertex,
            fill_color="#F4A460", fill_opacity=0.8, stroke_color=BLACK, stroke_width=2
        )
        self.play(FadeIn(tri_left), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(corner_text), run_time=0.8)
        
        # TRANSFORM area_text to "Let's calculate the total area"
        calc_intro = Text("Let's calculate the total area:", font_size=32)
        calc_intro.next_to(outer_square, DOWN, buff=1.0)
        self.play(Transform(area_text, calc_intro), run_time=1.5)
        self.wait(2)
        
        # Area breakdown
        area_calc1 = Text("Area = 4 triangles + tilted square", font_size=28)
        area_calc1.next_to(area_text, DOWN, buff=0.4)
        self.play(Write(area_calc1), run_time=2)
        self.wait(2)
        
        area_calc2 = Text("Area = 4×(½ab) + c²", font_size=28)
        area_calc2.next_to(area_calc1, DOWN, buff=0.3)
        self.play(Write(area_calc2), run_time=2)
        self.wait(2)
        
        area_calc3 = Text("Area = 2ab + c²", font_size=28, color=GREEN)
        area_calc3.next_to(area_calc2, DOWN, buff=0.3)
        self.play(Write(area_calc3), run_time=2)
        self.wait(3)
        
        # Store everything for conclusion
        self.right_group = VGroup(
            outer_square, top_label, right_label, area_text,
            center_square, label_c_sq,
            tri_top, tri_right, tri_bottom, tri_left,
            area_calc1, area_calc2, area_calc3
        )
        
    def show_conclusion(self):
        self.play(FadeOut(self.right_group), FadeOut(self.title), run_time=2)
        self.wait(1)
        
        # Title
        conclusion_title = Text("The Proof:", font_size=48, color=YELLOW)
        conclusion_title.move_to(UP * 3)
        self.play(Write(conclusion_title), run_time=2)
        self.wait(2)
        
        # Both arrangements have same area
        same_area = Text("Both arrangements have the same total area:", font_size=36)
        same_area.move_to(UP * 1.8)
        self.play(Write(same_area), run_time=2)
        self.wait(2)
        
        # First arrangement
        eq1 = Text("First: (a+b)² = 2ab + a² + b²", font_size=32, color=GREEN)
        eq1.move_to(UP * 0.8)
        self.play(Write(eq1), run_time=2)
        self.wait(2)
        
        # Second arrangement  
        eq2 = Text("Second: (a+b)² = 2ab + c²", font_size=32, color=GREEN)
        eq2.move_to(ORIGIN)
        self.play(Write(eq2), run_time=2)
        self.wait(3)
        
        # Therefore
        therefore = Text("Therefore:", font_size=36, color=YELLOW)
        therefore.move_to(DOWN * 1.2)
        self.play(Write(therefore), run_time=1.5)
        self.wait(1)
        
        # Set them equal
        eq3 = Text("2ab + a² + b² = 2ab + c²", font_size=32)
        eq3.move_to(DOWN * 2)
        self.play(Write(eq3), run_time=2)
        self.wait(3)
        
        # Subtract 2ab from both sides
        subtract = Text("Subtracting 2ab from both sides:", font_size=32, color=ORANGE)
        subtract.move_to(DOWN * 2.8)
        self.play(Write(subtract), run_time=2)
        self.wait(2)
        
        # Final result
        final = Text("a² + b² = c²", font_size=56, color=RED, weight=BOLD)
        final.move_to(DOWN * 3.5)
        self.play(Write(final), run_time=2)
        self.wait(2)
        
        # Draw box around it
        box = SurroundingRectangle(final, color=GOLD, buff=0.3, stroke_width=4)
        self.play(Create(box), run_time=1.5)
        self.wait(10)
        