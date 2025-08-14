from manim import *

class RigidTransformations(Scene):
    def construct(self):
        # Define the original triangle
        triangle = Polygon(
            [-2, 0, 0],
            [-3, 1, 0],
            [-1, 1, 0],
            color=BLUE
        )
        triangle_label = Text("Original", font_size=24).next_to(triangle, DOWN)
        
        self.play(Create(triangle), Write(triangle_label))
        self.wait(1)

        # --- TRANSLATION ---
        translation_vector = RIGHT * 4 + UP * 1
        translated_triangle = triangle.copy().shift(translation_vector)
        translated_label = Text("Translation", font_size=24).next_to(translated_triangle, DOWN)

        self.play(
            triangle.animate.shift(translation_vector),
            FadeOut(triangle_label),
            run_time=2
        )
        self.play(Write(translated_label))
        self.wait(1)

        # --- REFLECTION across the Y-axis ---
        reflected_triangle = translated_triangle.copy().scale([-1, 1, 1])
        reflected_triangle.set_color(RED)
        reflected_label = Text("Reflection", font_size=24).next_to(reflected_triangle, DOWN)

        self.play(
            Transform(translated_triangle, reflected_triangle),
            FadeOut(translated_label),
            run_time=2
        )
        self.play(Write(reflected_label))
        self.wait(1)

        # --- ROTATION about the origin ---
        angle = PI / 3  # 60 degrees
        rotated_triangle = reflected_triangle.copy().rotate(angle, about_point=ORIGIN)
        rotated_triangle.set_color(GREEN)
        rotated_label = Text("Rotation", font_size=24).next_to(rotated_triangle, DOWN)

        self.play(
            Transform(reflected_triangle, rotated_triangle),
            FadeOut(reflected_label),
            run_time=2
        )
        self.play(Write(rotated_label))
        self.wait(2)
