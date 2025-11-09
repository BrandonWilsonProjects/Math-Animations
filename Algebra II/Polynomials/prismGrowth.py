from manim import *

class CubicVolumeGrowth(ThreeDScene):
    def construct(self):
        # Set camera (affects only 3D objects like the cube)
        self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES, zoom=0.8)

        # Title
        title = Text("Cubic Growth of Volume (x^3)", font_size=36).to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))

        # Axes for cubic function (kept flat, 2D) - scaled down and shifted left
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 70, 10]
        ).scale(0.7).to_edge(LEFT*5.5).shift(DOWN*1)

        # Labels (flat 2D text)
        label_x = Text("x", font_size=24).next_to(axes.x_axis.get_end(), DOWN)
        label_y = Text("Volume = x^3", font_size=24).next_to(axes.y_axis.get_end(), LEFT)

        # Keep graph and labels flat
        self.add_fixed_in_frame_mobjects(axes, label_x, label_y)

        # Graph of cubic function
        cubic_graph = axes.plot(lambda t: t**3, x_range=[0,4], color=YELLOW)
        graph_label = Text("x^3", font_size=24).next_to(cubic_graph.get_end(), UP)
        self.add_fixed_in_frame_mobjects(cubic_graph, graph_label)

        # Animate graph appearing
        self.play(Create(axes), Write(label_x), Write(label_y))
        self.play(Create(cubic_graph), FadeIn(graph_label))

        # 3D cube (on the right side, affected by camera)
        prism = Cube(side_length=0.01, fill_color=BLUE, fill_opacity=0.6, stroke_color=WHITE)
        prism.shift(RIGHT*3 + DOWN*1)  # move cube to right side
        self.add(prism)

        # Animate growth of the cube while plotting points on graph
        for x in [0.5, 1, 1.5, 2, 2.5, 3]:
            new_prism = Cube(side_length=x, fill_color=BLUE, fill_opacity=0.6, stroke_color=WHITE)
            new_prism.shift(LEFT*3 + DOWN*3)  # keep cube anchored on right
            self.play(Transform(prism, new_prism), run_time=1.5)

            # Add dot on 2D graph
            dot = Dot(axes.c2p(x, x**3), color=RED)
            self.add_fixed_in_frame_mobjects(dot)
            self.play(FadeIn(dot), run_time=0.5)
            self.wait(0.3)

        self.wait(2)
