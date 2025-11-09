from manim import *
import numpy as np

class SequentialPatterns(Scene):
    def construct(self):
        title = Text("The Beauty of Sequences", font_size=40, color=YELLOW).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # --- Arithmetic Sequence ---
        arithmetic_text = Text("Arithmetic Sequence: 2, 4, 6, 8, ...", font_size=28, color=BLUE)
        arithmetic_text.next_to(title, DOWN, buff=0.6)
        arith_points = VGroup(*[Dot([n*0.8, 0, 0], color=BLUE) for n in range(1, 8)])

        self.play(Write(arithmetic_text))
        self.play(FadeIn(arith_points, shift=DOWN))
        self.wait(2)
        self.play(FadeOut(arithmetic_text), FadeOut(arith_points))

        # --- Geometric Sequence ---
        geo_text = Text("Geometric Sequence: 1, 2, 4, 8, ...", font_size=28, color=GREEN)
        geo_text.next_to(title, DOWN, buff=0.6)
        # Shift points lower by scaling y down
        geo_points = VGroup(*[
            Dot([n*0.8, np.log2(n+1) * 0.3 - 1, 0], color=GREEN) for n in range(1, 8)
        ])

        self.play(Write(geo_text))
        self.play(FadeIn(geo_points, shift=UP))
        self.wait(2)
        self.play(FadeOut(geo_text), FadeOut(geo_points))

        # --- Triangular Numbers ---
        tri_text = Text("Triangular Numbers: 1, 3, 6, 10, ...", font_size=28, color=RED)
        tri_text.next_to(title, DOWN, buff=0.6)
        # Shift points lower by scaling y down
        tri_points = VGroup(*[
            Dot([n*0.8, (n*(n+1))/8.0 - 1, 0], color=RED) for n in range(1, 7)
        ])

        self.play(Write(tri_text))
        self.play(FadeIn(tri_points, shift=RIGHT))
        self.wait(2)
        self.play(FadeOut(tri_text), FadeOut(tri_points))

        # --- Fibonacci Growth ---
        fib_text = Text("Fibonacci Growth: 1, 1, 2, 3, 5, 8, ...", font_size=28, color=ORANGE)
        fib_text.next_to(title, DOWN, buff=0.6)
        fib_seq = [1, 1, 2, 3, 5, 8, 13]
        fib_dots = VGroup(*[
            Dot([n*0.8, fib_seq[n-1]*0.2 - 1, 0], color=ORANGE) for n in range(1, len(fib_seq))
        ])

        self.play(Write(fib_text))
        self.play(FadeIn(fib_dots, shift=LEFT))
        self.wait(2)
        self.play(FadeOut(fib_text), FadeOut(fib_dots))

        # --- Closing statement ---
        closing = Text("Patterns in Numbers Create Harmony", font_size=34, color=YELLOW).to_edge(DOWN)
        self.play(Write(closing))
        self.wait(3)
