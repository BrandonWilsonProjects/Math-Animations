from manim import *

class ExponentialGrowthDecayPlain(Scene):
    def construct(self):
        # Axes
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 20, 5],
            x_length=9,
            y_length=5,
            axis_config={"color": GREY},
            tips=False
        )
        axes.add_coordinates(label_constructor=Text)

        # Title
        title = Text("Exponential Growth and Decay", font_size=32).to_edge(UP)

        # Graphs
        growth_curve = axes.plot(lambda x: 2**x, color=BLUE, x_range=[-4, 4])
        decay_curve = axes.plot(lambda x: 0.5**x, color=RED, x_range=[-4, 4])

        # Labels
        growth_label = Text("y = 2^x", font_size=24, color=BLUE).next_to(growth_curve, UR, buff=0.3)
        decay_label = Text("y = 0.5^x", font_size=24, color=RED).next_to(decay_curve, UL, buff=0.3)

        # Explanatory text at bottom
        growth_explain = Text("Exponential Growth (Base > 1)", font_size=20, color=BLUE).to_edge(DOWN).shift(LEFT * 2)
        decay_explain = Text("Exponential Decay (0 < Base < 1)", font_size=20, color=RED).to_edge(DOWN).shift(RIGHT * 2)

        # Animate scene
        self.play(Write(title))
        self.play(Create(axes))
        self.wait(0.5)
        self.play(Create(growth_curve), Write(growth_label))
        self.wait(0.5)
        self.play(Create(decay_curve), Write(decay_label))
        self.wait(0.5)
        self.play(Write(growth_explain), Write(decay_explain))
        self.wait(2)
