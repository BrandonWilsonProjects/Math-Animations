from manim import *

class RigidTransformationRules(Scene):
    def construct(self):
        # -------------------------------
        # Title
        # -------------------------------
        title = Text("Rigid Transformations", font_size=42, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # ============================================================
        # REFLECTION
        # ============================================================
        reflection_header = Text("REFLECTION RULES:", font_size=36, color=BLUE).next_to(title, DOWN, buff=0.6)
        flip_word = Text("FLIP", font_size=32, color=YELLOW).next_to(reflection_header, DOWN, buff=0.3)

        reflect_rules = VGroup(
            Text("If (x, y) is reflected over the x-axis → (x, -y)", font_size=28),
            Text("If (x, y) is reflected over the y-axis → (-x, y)", font_size=28),
            Text("If (x, y) is reflected over the line y = x → (y, x)", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(flip_word, DOWN, buff=0.4)

        self.play(Write(reflection_header))
        self.play(Write(flip_word))
        self.play(LaggedStart(*[Write(rule) for rule in reflect_rules], lag_ratio=0.3))
        self.wait(3)
        self.play(FadeOut(reflection_header, flip_word, reflect_rules))

        # ============================================================
        # ROTATION
        # ============================================================
        rotation_header = Text("ROTATION RULES:", font_size=36, color=GREEN).next_to(title, DOWN, buff=0.6)
        turn_word = Text("TURN", font_size=32, color=YELLOW).next_to(rotation_header, DOWN, buff=0.3)

        rotate_rules = VGroup(
            Text("If (x, y) is rotated 90° CW or 270° CCW → (y, -x)", font_size=28),
            Text("If (x, y) is rotated 180° CW or CCW → (-x, -y)", font_size=28),
            Text("If (x, y) is rotated 270° CW or 90° CCW → (-y, x)", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(turn_word, DOWN, buff=0.4)

        self.play(Write(rotation_header))
        self.play(Write(turn_word))
        self.play(LaggedStart(*[Write(rule) for rule in rotate_rules], lag_ratio=0.3))
        self.wait(3)
        self.play(FadeOut(rotation_header, turn_word, rotate_rules))

        # ============================================================
        # TRANSLATION
        # ============================================================
        translation_header = Text("TRANSLATION RULES:", font_size=36, color=RED).next_to(title, DOWN, buff=0.6)
        shift_word = Text("SHIFT", font_size=32, color=YELLOW).next_to(translation_header, DOWN, buff=0.3)

        translate_rules = VGroup(
            Text("Can translate up and down → affects y-axis", font_size=28),
            Text("Can translate left and right → affects x-axis", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(shift_word, DOWN, buff=0.4)

        self.play(Write(translation_header))
        self.play(Write(shift_word))
        self.play(LaggedStart(*[Write(rule) for rule in translate_rules], lag_ratio=0.3))
        self.wait(3)

        # ============================================================
        # END MESSAGE
        # ============================================================
        self.play(FadeOut(translation_header, shift_word, translate_rules))
        end_text = Text(
            "All rigid transformations preserve size and shape!",
            font_size=34,
            color=YELLOW
        ).move_to(DOWN * 1)
        self.play(Write(end_text))
        self.wait(3)
