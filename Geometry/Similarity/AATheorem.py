from manim import *
import numpy as np

class AngleAngleTheorem(Scene):
    """Complete demonstration of the Angle-Angle theorem for similar triangles"""
    def construct(self):
        # =====================================================================
        # INTRO: Title Sequence
        # =====================================================================
        title = Text("Angle-Angle Similarity Theorem", font_size=52, gradient=(BLUE, PURPLE))
        subtitle = Text("Two angles determine similar triangles", font_size=28, color=GRAY).next_to(title, DOWN)
        
        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle, shift=UP))
        self.wait(1.5)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # =====================================================================
        # PART 1: INTRODUCE THE FIRST TRIANGLE
        # =====================================================================
        section1_title = Text("Triangle ABC", font_size=36, color=YELLOW).to_edge(UP)
        self.play(Write(section1_title))
        self.wait(0.5)
        
        # Create first triangle (scaled down and positioned left)
        A1 = np.array([-4.5, -0.5, 0])
        B1 = np.array([-1.5, -0.5, 0])
        C1 = np.array([-3, 1.5, 0])
        
        triangle1 = Polygon(A1, B1, C1, color=BLUE, stroke_width=4)
        
        # Labels for vertices
        label_A1 = Text("A", color=BLUE, font_size=32).next_to(A1, LEFT)
        label_B1 = Text("B", color=BLUE, font_size=32).next_to(B1, RIGHT)
        label_C1 = Text("C", color=BLUE, font_size=32).next_to(C1, UP)
        
        self.play(Create(triangle1), run_time=1.5)
        self.play(Write(label_A1), Write(label_B1), Write(label_C1))
        self.wait(1)
        
        # =====================================================================
        # PART 2: HIGHLIGHT ANGLE A
        # =====================================================================
        angle_a_text = Text("Angle A", font_size=28, color=GREEN).to_corner(UL)
        self.play(Write(angle_a_text))
        
        # Create angle arc for angle A (corrected direction)
        angle_A_arc = Angle(
            Line(A1, B1), Line(A1, C1),
            radius=0.5,
            color=GREEN,
            stroke_width=3
        )
        angle_A_measure = Text("53°", font_size=24, color=GREEN).move_to(A1 + np.array([0.7, 0.3, 0]))
        
        self.play(Create(angle_A_arc), Write(angle_A_measure))
        self.wait(1)
        
        # =====================================================================
        # PART 3: HIGHLIGHT ANGLE B
        # =====================================================================
        angle_b_text = Text("Angle B", font_size=28, color=ORANGE).to_corner(UL)
        self.play(Transform(angle_a_text, angle_b_text))
        
        # Create angle arc for angle B (corrected direction)
        angle_B_arc = Angle(
            Line(B1, C1), Line(B1, A1),
            radius=0.5,
            color=ORANGE,
            stroke_width=3
        )
        angle_B_measure = Text("37°", font_size=24, color=ORANGE).move_to(B1 + np.array([-0.7, 0.3, 0]))
        
        self.play(Create(angle_B_arc), Write(angle_B_measure))
        self.wait(1.5)
        
        # =====================================================================
        # PART 4: INTRODUCE THE SECOND TRIANGLE
        # =====================================================================
        section2_title = Text("Triangle DEF", font_size=36, color=YELLOW).to_edge(UP)
        self.play(
            FadeOut(angle_a_text),
            Transform(section1_title, section2_title)
        )
        self.wait(0.5)
        
        # Create second triangle (different size, same angles) - scaled down and positioned right
        # Scale factor: 1.4 (reduced from 1.8)
        scale_factor = 1.4
        D2 = np.array([1, -0.5, 0])
        E2 = D2 + scale_factor * (B1 - A1)
        F2 = D2 + scale_factor * (C1 - A1)
        
        triangle2 = Polygon(D2, E2, F2, color=RED, stroke_width=4)
        
        # Labels for vertices
        label_D2 = Text("D", color=RED, font_size=32).next_to(D2, LEFT)
        label_E2 = Text("E", color=RED, font_size=32).next_to(E2, RIGHT)
        label_F2 = Text("F", color=RED, font_size=32).next_to(F2, UP)
        
        self.play(Create(triangle2), run_time=1.5)
        self.play(Write(label_D2), Write(label_E2), Write(label_F2))
        self.wait(1)
        
        # =====================================================================
        # PART 5: SHOW MATCHING ANGLES IN SECOND TRIANGLE
        # =====================================================================
        angle_d_text = Text("Angle D = Angle A", font_size=28, color=GREEN).to_corner(UL)
        self.play(Write(angle_d_text))
        
        # Create angle arc for angle D (corrected direction)
        angle_D_arc = Angle(
            Line(D2, E2), Line(D2, F2),
            radius=0.5,
            color=GREEN,
            stroke_width=3
        )
        angle_D_measure = Text("53°", font_size=24, color=GREEN).move_to(D2 + np.array([0.7, 0.3, 0]))
        
        self.play(Create(angle_D_arc), Write(angle_D_measure))
        self.wait(1)
        
        angle_e_text = Text("Angle E = Angle B", font_size=28, color=ORANGE).to_corner(UL)
        self.play(Transform(angle_d_text, angle_e_text))
        
        # Create angle arc for angle E (corrected direction)
        angle_E_arc = Angle(
            Line(E2, F2), Line(E2, D2),
            radius=0.5,
            color=ORANGE,
            stroke_width=3
        )
        angle_E_measure = Text("37°", font_size=24, color=ORANGE).move_to(E2 + np.array([-0.7, 0.3, 0]))
        
        self.play(Create(angle_E_arc), Write(angle_E_measure))
        self.wait(1.5)
        
        # =====================================================================
        # PART 6: BRING TRIANGLES TOGETHER FOR COMPARISON
        # =====================================================================
        comparison_text = Text("Comparing the triangles", font_size=32, color=YELLOW).to_edge(UP)
        self.play(
            FadeOut(angle_d_text),
            Transform(section1_title, comparison_text)
        )
        
        # Move triangles to better comparison positions (slight adjustments)
        triangle1_group = VGroup(triangle1, label_A1, label_B1, label_C1, 
                                angle_A_arc, angle_A_measure, angle_B_arc, angle_B_measure)
        triangle2_group = VGroup(triangle2, label_D2, label_E2, label_F2,
                                angle_D_arc, angle_D_measure, angle_E_arc, angle_E_measure)
        
        self.play(
            triangle1_group.animate.shift(LEFT * 1),
            triangle2_group.animate.shift(RIGHT * 1),
            run_time=2
        )
        self.wait(1)
        
        # =====================================================================
        # PART 7: OVERLAY TRIANGLES TO SHOW SIMILARITY
        # =====================================================================
        overlay_text = Text("Overlaying the triangles", font_size=32, color=YELLOW).to_edge(UP)
        self.play(Transform(section1_title, overlay_text))
        
        # Create a scaled copy of triangle1 to overlay on triangle2
        triangle1_scaled = triangle1.copy()
        triangle1_scaled.set_color(PURPLE)
        triangle1_scaled.set_stroke(width=3, opacity=0.7)
        
        # Move triangle1_scaled to origin first, scale it, then move to triangle2's position
        # Get the current center of triangle1_scaled
        current_center = triangle1_scaled.get_center()
        
        # Calculate target position (center of triangle2 after it was shifted)
        target_center = triangle2.get_center()
        
        self.play(
            triangle1_scaled.animate.scale(scale_factor, about_point=current_center).move_to(target_center),
            run_time=2
        )
        self.wait(1)
        
        # Highlight the perfect overlap
        flash_group = VGroup(triangle1_scaled, triangle2)
        self.play(
            flash_group.animate.set_stroke(width=6),
            run_time=0.5
        )
        self.play(
            flash_group.animate.set_stroke(width=4),
            run_time=0.5
        )
        self.wait(1)
        # =====================================================================
        # PART 8: SHOW PROPORTIONAL SIDES
        # =====================================================================
        self.play(FadeOut(triangle1_scaled))
        
        proportions_text = Text("Sides are proportional", font_size=32, color=YELLOW).to_edge(UP)
        self.play(Transform(section1_title, proportions_text))
        
        # Show side lengths for triangle 1
        side_AB = Line(A1 + LEFT * 2, B1 + LEFT * 2, color=BLUE, stroke_width=3)
        side_BC = Line(B1 + LEFT * 2, C1 + LEFT * 2, color=BLUE, stroke_width=3)
        side_CA = Line(C1 + LEFT * 2, A1 + LEFT * 2, color=BLUE, stroke_width=3)
        
        side_AB_label = Text("4", font_size=24, color=BLUE).next_to(side_AB, DOWN)
        side_BC_label = Text("3.6", font_size=24, color=BLUE).next_to(side_BC, RIGHT)
        side_CA_label = Text("3.2", font_size=24, color=BLUE).next_to(side_CA, LEFT)
        
        # Show side lengths for triangle 2
        side_DE = Line(D2 + RIGHT * 2, E2 + RIGHT * 2, color=RED, stroke_width=3)
        side_EF = Line(E2 + RIGHT * 2, F2 + RIGHT * 2, color=RED, stroke_width=3)
        side_FD = Line(F2 + RIGHT * 2, D2 + RIGHT * 2, color=RED, stroke_width=3)
        
        side_DE_label = Text("7.2", font_size=24, color=RED).next_to(side_DE, DOWN)
        side_EF_label = Text("6.5", font_size=24, color=RED).next_to(side_EF, RIGHT)
        side_FD_label = Text("5.8", font_size=24, color=RED).next_to(side_FD, LEFT)
        
        # Create brace showing measurements
        brace_ABC = Brace(triangle1_group, DOWN)
        brace_DEF = Brace(triangle2_group, DOWN)
        
        brace_ABC_text = Text("Smaller", font_size=24, color=BLUE).next_to(brace_ABC, DOWN)
        brace_DEF_text = Text("Larger (1.4x)", font_size=24, color=RED).next_to(brace_DEF, DOWN)
        
        self.play(
            GrowFromCenter(brace_ABC),
            Write(brace_ABC_text),
            GrowFromCenter(brace_DEF),
            Write(brace_DEF_text)
        )
        self.wait(2)
        
        # =====================================================================
        # PART 9: STATE THE THEOREM
        # =====================================================================
        self.play(
            *[FadeOut(mob) for mob in [
                triangle1_group, triangle2_group, 
                brace_ABC, brace_ABC_text, brace_DEF, brace_DEF_text,
                section1_title
            ]]
        )
        
        theorem_title = Text("Angle-Angle (AA) Similarity Theorem", 
                           font_size=40, color=YELLOW).to_edge(UP)
        
        theorem_statement = VGroup(
            Text("If two angles of one triangle", font_size=28),
            Text("are congruent to two angles", font_size=28),
            Text("of another triangle,", font_size=28),
            Text("then the triangles are SIMILAR", font_size=32, color=GREEN, weight=BOLD)
        ).arrange(DOWN, center=True, buff=0.3)
        
        self.play(Write(theorem_title), run_time=1.5)
        self.wait(0.5)
        self.play(Write(theorem_statement), run_time=3, lag_ratio=0.3)
        self.wait(2)
        
        self.play(FadeOut(theorem_statement))
        # =====================================================================
        # FINALE
        # =====================================================================        
        finale_text = VGroup(
            Text("AA Theorem:", font_size=44, color=BLUE),
            Text("Two Angles Determine Similarity", font_size=36, gradient=(PURPLE, PINK))
        ).arrange(DOWN, buff=0.4)
        
        self.play(Write(finale_text[0]), run_time=1.5)
        self.play(FadeIn(finale_text[1], shift=UP))
        self.wait(3)
        self.play(FadeOut(finale_text))