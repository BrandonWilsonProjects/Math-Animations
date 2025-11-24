from manim import *

class VerticalAsymptoteUndefined(Scene):
    def construct(self):
        # Title
        title = Text("Why Vertical Asymptotes Are Undefined", font_size=48)
        self.play(FadeIn(title))
        self.wait(3)
        self.play(title.animate.to_edge(UP))
        self.play(FadeOut(title))
        

        # Number plane
        plane = NumberPlane(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            background_line_style={"stroke_opacity": 0.4}
        ).scale(1.1)
        self.play(Create(plane))

        # Add simple axis labels (NOT latex)
        x_label = Text("x", font_size=32).next_to(plane.x_axis, RIGHT)
        y_label = Text("y", font_size=32).next_to(plane.y_axis, UP)
        self.play(FadeIn(x_label), FadeIn(y_label))

        # Vertical asymptote line
        va_line = Line(
            start=plane.c2p(0, -6),
            end=plane.c2p(0, 6),
            color=YELLOW
        )
        va_label = Text("x = 0 (Undefined)", font_size=30, color=YELLOW).next_to(va_line, RIGHT + DOWN * 1.5)

        self.play(Create(va_line), FadeIn(va_label))
        self.wait(1)

        # Function definition (pure text)
        func_text = Text("Function: (x + 3) / x", font_size=34)
        func_text.next_to(title, DOWN)
        self.play(FadeIn(func_text))

        # Define the function
        # Function
        def func(x):
            return (x + 3) / x

        # Plot left side (x from -6 to -0.1)
        left_graph = plane.plot(func, x_range=[-6, -0.1], color=BLUE)

        # Plot right side (x from 0.1 to 6)
        right_graph = plane.plot(func, x_range=[0.1, 6], color=BLUE)

        # Animate
        self.play(Create(left_graph))
        self.play(Create(right_graph))

        # Explanation
        expl1 = Text("As x gets close to 0...", font_size=34)
        expl1.next_to(func_text, DOWN + LEFT * 2)
        self.play(FadeIn(expl1))

        # Points approaching zero from the RIGHT
        right_vals = [1, 0.5, 0.25, 0.1]
        right_dots = VGroup(*[
            Dot(plane.c2p(v, func(v)), color=GREEN) for v in right_vals
        ])

        # Points approaching zero from the LEFT
        left_vals = [-1, -0.5, -0.25, -0.1]
        left_dots = VGroup(*[
            Dot(plane.c2p(v, func(v)), color=RED) for v in left_vals
        ])

        self.play(FadeIn(right_dots))
        self.play(FadeIn(left_dots))
        self.wait(1)

        # Arrows showing explosion up/down
        up_arrow = Arrow(
            start=plane.c2p(0.5, func(0.5)),
            end=plane.c2p(0.5, 6),
            color=GREEN
        )
        down_arrow = Arrow(
            start=plane.c2p(-0.5, func(-0.5)),
            end=plane.c2p(-0.5, -6),
            color=RED
        )

        self.play(Create(up_arrow), Create(down_arrow))
        self.wait(1)

        # Final explanation
        final_text = Text(
            "The outputs grow without bound.\n"
            "The function cannot produce any value at x = 0.\n"
            "THIS IS WHY VERTICAL ASYMPTOTES ARE UNDEFINED!!!",
            font_size=32
        )
        final_text.to_edge(DOWN)

        self.play(FadeIn(final_text))
        self.wait(5)

        # Clean fade-out
        self.play(
            FadeOut(expl1),
            FadeOut(final_text),
            FadeOut(right_dots),
            FadeOut(left_dots),
            FadeOut(up_arrow),
            FadeOut(down_arrow)
        )
        self.wait(1)
