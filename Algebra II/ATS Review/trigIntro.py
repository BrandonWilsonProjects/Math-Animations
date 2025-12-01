from manim import *
import numpy as np

class UnitCircleTrig(Scene):
    def construct(self):
        # Title
        title = Text("Unit Circle & Trigonometric Functions", weight=BOLD).scale(0.8)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))
        
        # ============ PART 1: Unit Circle with All Key Angles ============
        circle = Circle(radius=2, color=WHITE).shift(LEFT*3)
        center = circle.get_center()
        
        # Axes for unit circle
        h_line = Line(center + LEFT*2.5, center + RIGHT*2.5, color=GRAY, stroke_width=1)
        v_line = Line(center + DOWN*2.5, center + UP*2.5, color=GRAY, stroke_width=1)
        
        self.play(Create(circle), Create(h_line), Create(v_line))
        self.wait(0.5)
        
        # Key angles in radians
        angles = [0, PI/6, PI/4, PI/3, PI/2, 2*PI/3, 3*PI/4, 5*PI/6, PI, 
                  7*PI/6, 5*PI/4, 4*PI/3, 3*PI/2, 5*PI/3, 7*PI/4, 11*PI/6]
        
        angle_labels = ["0", "π/6", "π/4", "π/3", "π/2", "2π/3", "3π/4", "5π/6", 
                       "π", "7π/6", "5π/4", "4π/3", "3π/2", "5π/3", "7π/4", "11π/6"]
        
        # Create all triangles and points
        triangles = VGroup()
        points = VGroup()
        labels = VGroup()
        
        for i, angle in enumerate(angles):
            x = 2 * np.cos(angle)
            y = 2 * np.sin(angle)
            point_pos = center + RIGHT*x + UP*y
            
            # Create right triangle
            if angle not in [0, PI/2, PI, 3*PI/2]:  # Skip axes angles for cleaner triangles
                triangle = Polygon(
                    center,
                    center + RIGHT*x,
                    point_pos,
                    color=BLUE,
                    stroke_width=1,
                    fill_opacity=0.1
                )
                triangles.add(triangle)
            
            # Point on circle
            dot = Dot(point_pos, radius=0.04, color=YELLOW)
            points.add(dot)
            
            # Angle label
            label_distance = 2.5
            label_pos = center + RIGHT*(label_distance*np.cos(angle)) + UP*(label_distance*np.sin(angle))
            label = Text(angle_labels[i], font_size=20).move_to(label_pos)
            labels.add(label)
        
        self.play(Create(triangles), run_time=2)
        self.play(FadeIn(points), Write(labels), run_time=2)
        self.wait(2)
        
        # Fade out triangles and labels for transition
        self.play(FadeOut(triangles), FadeOut(labels), FadeOut(points))
        self.wait(0.5)
        
        # ============ PART 2: Animated Circle with Sin, Cos, Tan ============
        
        # Create coordinate plane on the right
        axes = Axes(
            x_range=[0, 2*PI, PI/2],
            y_range=[-1.5, 1.5, 0.5],
            x_length=6,
            y_length=4,
            axis_config={"include_tip": True, "stroke_width": 2},
        ).shift(RIGHT*3.5)
        
        # Custom x-axis labels
        
        axes_labels = VGroup(
            Text("θ", font_size=24).next_to(axes.x_axis.get_end(), RIGHT),
            Text("y", font_size=24).next_to(axes.y_axis.get_end(), UP)
        )
        
        self.play(Create(axes), Write(axes_labels))
        self.wait(0.5)
        
        # Angle tracker
        theta = ValueTracker(0)
        
        # Radius line (hypotenuse)
        radius_line = always_redraw(
            lambda: Line(
                center,
                center + RIGHT*2*np.cos(theta.get_value()) + UP*2*np.sin(theta.get_value()),
                color=WHITE,
                stroke_width=3
            )
        )
        
        # Cosine line (horizontal - adjacent)
        cos_line = always_redraw(
            lambda: Line(
                center,
                center + RIGHT*2*np.cos(theta.get_value()),
                color=BLUE,
                stroke_width=3
            )
        )
        
        # Sine line (vertical - opposite)
        sin_line = always_redraw(
            lambda: Line(
                center + RIGHT*2*np.cos(theta.get_value()),
                center + RIGHT*2*np.cos(theta.get_value()) + UP*2*np.sin(theta.get_value()),
                color=RED,
                stroke_width=3
            )
        )
        
        # Tangent line (extends from circle to tangent point)
        tan_line = always_redraw(
            lambda: Line(
                center + RIGHT*2*np.cos(theta.get_value()) + UP*2*np.sin(theta.get_value()),
                center + RIGHT*2 + UP*2*np.tan(theta.get_value()) if abs(np.cos(theta.get_value())) > 0.1 else center + RIGHT*2*np.cos(theta.get_value()) + UP*2*np.sin(theta.get_value()),
                color=GREEN,
                stroke_width=2
            )
        )
        
        # Point on circle
        circle_dot = always_redraw(
            lambda: Dot(
                center + RIGHT*2*np.cos(theta.get_value()) + UP*2*np.sin(theta.get_value()),
                color=YELLOW,
                radius=0.08
            )
        )
        
        # Labels for cos, sin, tan
        cos_label = always_redraw(
            lambda: Text("cos", font_size=20, color=BLUE).next_to(
                cos_line.get_center(), DOWN, buff=0.1
            )
        )
        
        sin_label = always_redraw(
            lambda: Text("sin", font_size=20, color=RED).next_to(
                sin_line.get_center(), RIGHT, buff=0.1
            )
        )
        
        tan_label = always_redraw(
            lambda: Text("tan", font_size=20, color=GREEN).next_to(
                tan_line.get_center(), RIGHT, buff=0.1
            ) if abs(np.cos(theta.get_value())) > 0.1 else Text("tan", font_size=20, color=GREEN).move_to(center + RIGHT*3)
        )
        
        # Create the traced paths on the coordinate plane
        sin_curve = VMobject(color=RED, stroke_width=3)
        cos_curve = VMobject(color=BLUE, stroke_width=3)
        
        sin_curve.set_points_as_corners([axes.c2p(0, 0)])
        cos_curve.set_points_as_corners([axes.c2p(0, 1)])
        
        def update_sin_curve(curve):
            t = theta.get_value()
            new_curve = VMobject(color=RED, stroke_width=3)
            points = [axes.c2p(x, np.sin(x)) for x in np.linspace(0, t, int(t*50)+1)]
            if len(points) > 1:
                new_curve.set_points_as_corners(points)
                curve.become(new_curve)
        
        def update_cos_curve(curve):
            t = theta.get_value()
            new_curve = VMobject(color=BLUE, stroke_width=3)
            points = [axes.c2p(x, np.cos(x)) for x in np.linspace(0, t, int(t*50)+1)]
            if len(points) > 1:
                new_curve.set_points_as_corners(points)
                curve.become(new_curve)
        
        sin_curve.add_updater(update_sin_curve)
        cos_curve.add_updater(update_cos_curve)
        
        # Dots on the coordinate plane
        sin_dot = always_redraw(
            lambda: Dot(
                axes.c2p(theta.get_value(), np.sin(theta.get_value())),
                color=RED,
                radius=0.06
            )
        )
        
        cos_dot = always_redraw(
            lambda: Dot(
                axes.c2p(theta.get_value(), np.cos(theta.get_value())),
                color=BLUE,
                radius=0.06
            )
        )
        
        # Add everything to the scene
        self.play(
            Create(radius_line),
            Create(cos_line),
            Create(sin_line),
            Create(tan_line),
            FadeIn(circle_dot),
            Write(cos_label),
            Write(sin_label),
            Write(tan_label)
        )
        self.wait(1)
        
        # Connecting lines from unit circle to coordinate plane
        sin_connector = always_redraw(
            lambda: DashedLine(
                center + RIGHT*2*np.cos(theta.get_value()) + UP*2*np.sin(theta.get_value()),
                axes.c2p(theta.get_value(), np.sin(theta.get_value())),
                color=RED,
                stroke_width=2,
                stroke_opacity=0.5
            )
        )
        
        cos_connector = always_redraw(
            lambda: DashedLine(
                center + RIGHT*2*np.cos(theta.get_value()) + UP*2*np.sin(theta.get_value()),
                axes.c2p(theta.get_value(), np.cos(theta.get_value())),
                color=BLUE,
                stroke_width=2,
                stroke_opacity=0.5
            )
        )
        
        # Add paths and dots
        self.add(sin_curve, cos_curve, sin_dot, cos_dot, sin_connector, cos_connector)
        
        # Rotate around the circle - TWO FULL ROTATIONS
        self.play(
            theta.animate.set_value(4*PI),
            run_time=12,
            rate_func=linear
        )
        self.wait(1)
        
        # Remove updaters
        sin_curve.remove_updater(update_sin_curve)
        cos_curve.remove_updater(update_cos_curve)
        
        # Final explanation
        explanation = Text(
            "The unit circle maps angles to sine and cosine values",
            font_size=28
        ).to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(2)
        
        # Fade out everything
        self.play(
            FadeOut(explanation),
            FadeOut(circle),
            FadeOut(h_line),
            FadeOut(v_line),
            FadeOut(radius_line),
            FadeOut(cos_line),
            FadeOut(sin_line),
            FadeOut(tan_line),
            FadeOut(circle_dot),
            FadeOut(cos_label),
            FadeOut(sin_label),
            FadeOut(tan_label),
            FadeOut(sin_curve),
            FadeOut(cos_curve),
            FadeOut(sin_dot),
            FadeOut(cos_dot),
            FadeOut(sin_connector),
            FadeOut(cos_connector),
            FadeOut(axes),
            FadeOut(axes_labels)
        )
        self.wait(1)
        
        closing_text = Text("Trigonometry is used to find unknown angles and distances in \ngeometric figures, particularly in fields like \narchitecture, engineering, astronomy, and navigation", font_size=30)
        self.play(FadeIn(closing_text))
        self.wait(8)