from manim import *
import math

class CylinderVolumeGraph(ThreeDScene):
    def construct(self):
        # Title (Pango-rendered, no LaTeX)
        title = Text("Cylinder Volume vs Radius with Zeros", font_size=36, font="Arial").to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))

        # Axes for the volume function, centered in frame
        axes = Axes(
            x_range=[0, 10, 1],  # Includes zero at r=10
            y_range=[0, 500, 50],  # Fits max volume ≈ 465.42
            x_length=8,  # Larger for prominence
            y_length=5,
        ).move_to(ORIGIN)  # Center the axes
        labels = axes.get_axis_labels(
            Text("Radius", font_size=24, font="Arial"), 
            Text("Volume", font_size=24, font="Arial")
        )
        self.play(Create(axes), Write(labels))

        # Volume function: V(r) = pi * r^2 * (10 - r)
        volume_func = lambda r: math.pi * r**2 * (10 - r)
        graph = axes.plot(volume_func, x_range=[0.1, 10], color=BLUE)
        self.play(Create(graph))

        # Cylinder object (starts in top-right corner)
        cylinder = Cylinder(radius=0.1, height=1, direction=OUT, fill_opacity=0.6, color=GREEN)
        cylinder.move_to(RIGHT * 5 + UP * 2)  # Top-right to avoid overlapping graph
        self.add(cylinder)

        # Dot moving along the graph
        dot = Dot(color=YELLOW).move_to(axes.c2p(0.1, volume_func(0.1)))
        self.add(dot)

        # Traced path for dot
        traced_path = TracedPath(dot.get_center, stroke_color=YELLOW, stroke_width=3)
        self.add(traced_path)

        # Animate cylinder + dot along the graph, with tilt
        def updater(mob, alpha):
            r = 10 * alpha  # r goes 0 to 10
            V = volume_func(r)
            h = max((10 - r) * 0.2, 0.1)  # Scaled height
            # Tilt angle: 0 at r=0 (upright), π/2 at r=10 (flat in xy-plane)
            tilt_angle = (PI / 2) * (r / 10)
            dot.move_to(axes.c2p(r, V))
            # Create new cylinder with updated radius, height, and tilt
            new_cylinder = Cylinder(
                radius=max(r * 0.15, 0.01),  # Scale radius, min 0.01 for visibility
                height=h,
                direction=OUT,
                fill_opacity=0.6,
                color=GREEN
            ).move_to(RIGHT * 5 + UP * 2)
            # Rotate around x-axis to tilt (flat at r=10)
            new_cylinder.rotate(tilt_angle, axis=RIGHT, about_point=RIGHT * 5 + UP * 2)
            mob.become(new_cylinder)

        self.play(UpdateFromAlphaFunc(cylinder, updater), run_time=8, rate_func=linear)

        # Highlight zero at r=0
        zero_r1 = 0
        zero_v1 = volume_func(zero_r1)
        zero_dot1 = Dot(color=RED).move_to(axes.c2p(zero_r1, zero_v1))
        self.play(GrowFromCenter(zero_dot1))
        zero_label1 = Text("Zero at r=0", font_size=24, font="Arial").next_to(zero_dot1, DOWN)
        self.play(Write(zero_label1))

        # Highlight zero at r=10
        zero_r2 = 10
        zero_v2 = volume_func(zero_r2)
        zero_dot2 = Dot(color=RED).move_to(axes.c2p(zero_r2, zero_v2))
        self.play(GrowFromCenter(zero_dot2))
        zero_label2 = Text("Zero at r=10", font_size=24, font="Arial").next_to(zero_dot2, DOWN + LEFT * 0.5)
        self.play(Write(zero_label2))

        # Highlight relative minimum (r=0, V=0, coincides with zero)
        min_label = Text("Relative Min", font_size=24, font="Arial").next_to(zero_dot1, DOWN + RIGHT * 0.5)
        self.play(Write(min_label))

        # Highlight relative maximum (r=20/3, V≈465.42)
        max_r = 20 / 3  # Critical point at 6.67
        max_v = volume_func(max_r)
        max_dot = Dot(color=RED).move_to(axes.c2p(max_r, max_v))
        self.play(GrowFromCenter(max_dot))
        max_label = Text("Relative Max", font_size=24, font="Arial").next_to(max_dot, UP)
        self.play(Write(max_label))

        self.wait(3)