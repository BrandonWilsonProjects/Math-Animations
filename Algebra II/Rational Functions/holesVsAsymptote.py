from manim import *

class HolesVsAsymptotes(Scene):
    def construct(self):
        # Title
        title = Text("Holes vs Asymptotes", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()
        
        # Create axes
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=6,
            y_length=6,
            axis_config={"color": BLUE}
        )
        axes.shift(DOWN * 0.5)
        
        self.play(Create(axes))
        self.wait()
        
        # Part 1: Show a function with a HOLE
        hole_label = Text("Function with a HOLE", font_size=32, color=YELLOW)
        hole_label.to_edge(UP)
        
        self.play(Transform(title, hole_label))
        self.wait()
        
        # Function: f(x) = (x^2 - 4)/(x - 2) = (x+2)(x-2)/(x-2) = x+2 with hole at x=2
        def func_with_hole(x):
            if abs(x - 2) < 0.01:
                return None
            return x + 2
        
        # Plot the line y = x + 2 (but with a hole)
        graph_hole = axes.plot(
            lambda x: x + 2,
            x_range=[-4, 1.9, 0.01],
            color=GREEN
        )
        graph_hole2 = axes.plot(
            lambda x: x + 2,
            x_range=[2.1, 4, 0.01],
            color=GREEN
        )
        
        # Mark the hole at (2, 4)
        hole_point = axes.coords_to_point(2, 4)
        hole_circle = Circle(radius=0.15, color=RED, fill_opacity=0)
        hole_circle.move_to(hole_point)
        hole_dot = Dot(hole_point, color=RED, radius=0.05)
        
        self.play(Create(graph_hole), Create(graph_hole2))
        self.play(Create(hole_circle), Create(hole_dot))
        self.wait()
        
        # Label the hole
        hole_text = Text("Hole at x=2", font_size=24, color=RED)
        hole_text.next_to(hole_circle, RIGHT)
        arrow_to_hole = Arrow(
            hole_text.get_left(),
            hole_circle.get_right(),
            color=RED,
            buff=0.1
        )
        
        self.play(Write(hole_text), GrowArrow(arrow_to_hole))
        self.wait(2)
        
        # Clear for next example
        self.play(
            FadeOut(graph_hole),
            FadeOut(graph_hole2),
            FadeOut(hole_circle),
            FadeOut(hole_dot),
            FadeOut(hole_text),
            FadeOut(arrow_to_hole)
        )
        
        # Part 2: Show a function with a VERTICAL ASYMPTOTE
        asymptote_label = Text("Function with ASYMPTOTE", font_size=32, color=YELLOW)
        asymptote_label.to_edge(UP)
        
        self.play(Transform(title, asymptote_label))
        self.wait()
        
        # Function: f(x) = 1/(x - 1) with vertical asymptote at x=1
        graph_asymptote_left = axes.plot(
            lambda x: 1 / (x - 1),
            x_range=[-4, 0.85, 0.01],
            color=PURPLE
        )
        graph_asymptote_right = axes.plot(
            lambda x: 1 / (x - 1),
            x_range=[1.15, 4, 0.01],
            color=PURPLE
        )
        
        # Draw the vertical asymptote line
        asymptote_line = DashedLine(
            axes.coords_to_point(1, -5),
            axes.coords_to_point(1, 5),
            color=RED,
            dash_length=0.2
        )
        
        self.play(Create(asymptote_line))
        self.play(Create(graph_asymptote_left), Create(graph_asymptote_right))
        self.wait()
        
        # Label the asymptote
        asymptote_text = Text("Vertical Asymptote at x=1", font_size=24, color=RED)
        asymptote_text.next_to(asymptote_line, RIGHT, buff=0.3)
        asymptote_text.shift(UP * 2)
        arrow_to_asymptote = Arrow(
            asymptote_text.get_bottom(),
            axes.coords_to_point(1, 2),
            color=RED,
            buff=0.1
        )
        
        self.play(Write(asymptote_text), GrowArrow(arrow_to_asymptote))
        self.wait(2)
        
        # Clear for comparison
        self.play(
            FadeOut(graph_asymptote_left),
            FadeOut(graph_asymptote_right),
            FadeOut(asymptote_line),
            FadeOut(asymptote_text),
            FadeOut(arrow_to_asymptote)
        )
        
        # Part 3: Side-by-side comparison
        comparison_title = Text("Key Difference", font_size=36, color=YELLOW)
        comparison_title.to_edge(UP).shift(DOWN * 0.8)
        self.play(Transform(title, comparison_title))
        
        # Shrink axes and create two side by side
        axes_left = Axes(
            x_range=[-3, 5, 1],
            y_range=[-3, 7, 1],
            x_length=4.5,
            y_length=4.5,
            axis_config={"color": BLUE}
        ).shift(LEFT * 3.5 + DOWN * 0.8)
        
        axes_right = Axes(
            x_range=[-3, 5, 1],
            y_range=[-5, 5, 1],
            x_length=4.5,
            y_length=4.5,
            axis_config={"color": BLUE}
        ).shift(RIGHT * 3.5 + DOWN * 0.8)
        
        self.play(Transform(axes, axes_left))
        self.play(Create(axes_right))
        
        # Left: Hole
        graph_hole_l = axes_left.plot(lambda x: x + 2, x_range=[-3, 1.9], color=GREEN)
        graph_hole_r = axes_left.plot(lambda x: x + 2, x_range=[2.1, 4.5], color=GREEN)
        hole_circ = Circle(radius=0.12, color=RED, fill_opacity=0)
        hole_circ.move_to(axes_left.coords_to_point(2, 4))
        
        hole_title_text = Text("HOLE", font_size=28, color=GREEN)
        hole_title_text.next_to(axes_left, UP, buff=0.3)
        
        # Right: Asymptote
        graph_asym_l = axes_right.plot(lambda x: 1/(x-1), x_range=[-3, 0.85], color=PURPLE)
        graph_asym_r = axes_right.plot(lambda x: 1/(x-1), x_range=[1.15, 4.5], color=PURPLE)
        asym_line = DashedLine(
            axes_right.coords_to_point(1, -5),
            axes_right.coords_to_point(1, 5),
            color=RED,
            dash_length=0.15
        )
        
        asymp_title_text = Text("ASYMPTOTE", font_size=28, color=PURPLE)
        asymp_title_text.next_to(axes_right, UP, buff=0.3)
        
        self.play(
            Write(hole_title_text),
            Write(asymp_title_text),
            Create(graph_hole_l),
            Create(graph_hole_r),
            Create(hole_circ),
            Create(asym_line),
            Create(graph_asym_l),
            Create(graph_asym_r)
        )
        self.wait()
        
        # Explanation text
        explanation = Text(
            "Hole: Removable discontinuity\nAsymptote: Function approaches infinity",
            font_size=20,
            line_spacing=1.2
        )
        explanation.to_edge(DOWN, buff=0.3)
        
        self.play(Write(explanation))
        self.wait(3)