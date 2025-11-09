from manim import *

class CongruencyScaling(Scene):
    def construct(self):
        # Title
        title = Text("Congruency ≠ Size, Congruency = Same Shape & Size", font_size=32).to_edge(UP)
        self.play(Write(title))

        # Step 1: Tiny congruent triangles
        tri1 = Polygon([-0.5, -0.3, 0], [0, 0.3, 0], [0.5, -0.3, 0],
                       color=BLUE, fill_opacity=0.7)
        tri2 = tri1.copy().shift(RIGHT * 2).set_color(GREEN)

        self.play(FadeIn(tri1), FadeIn(tri2))

        # Step 2: Congruence symbol between them
        congruent_text = Text("≅", font_size=48, color=YELLOW).move_to([1, 0.2, 0])
        self.play(Write(congruent_text))
        self.wait(2)

        # Step 3: Scale both larger but preserve congruence
        self.play(tri1.animate.scale(2).shift(LEFT*2),
                  tri2.animate.scale(2).shift(RIGHT*2),
                  run_time=2)
        self.wait(1)

        # Step 4: Even bigger scaling
        self.play(tri1.animate.scale(1.5).shift(LEFT*1),
                  tri2.animate.scale(1.5).shift(RIGHT*1),
                  run_time=2)
        self.wait(1)

        # Step 5: Overlap them to prove congruence
        self.play(tri1.animate.move_to(tri2.get_center()), run_time=2)
        self.wait(1)

        # Closing message
        closing = Text("Congruence ignores placement & scale — only shape & size matter",
                       font_size=28, color=YELLOW).to_edge(DOWN)
        self.play(Write(closing))
        self.wait(3)
