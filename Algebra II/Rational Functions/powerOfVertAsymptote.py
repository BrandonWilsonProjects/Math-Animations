from manim import *

class VerticalAsymptotePower(Scene):
    def construct(self):
        # Initial wide view
        axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[-10, 10, 2],
            x_length=10,
            y_length=6,
            tips=False,
            axis_config={"color": WHITE}
        ).shift(LEFT * 0.5)

        x_label = Text("x", font_size=36).next_to(axes.x_axis, RIGHT * 4)
        y_label = Text("y", font_size=36).next_to(axes.y_axis, DOWN * 4)
        title = Text("y = (x + 3) / x", color=YELLOW, font_size=35).to_corner(UR)

        # Graph (split to avoid x=0)
        f = lambda x: (x + 3) / x
        left = axes.plot(f, x_range=[-6, -0.01], color=YELLOW)
        right = axes.plot(f, x_range=[0.01, 6], color=YELLOW)

        # Asymptote
        asymptote = DashedLine(
            axes.c2p(0, -10), axes.c2p(0, 10),
            color=RED, stroke_width=6
        )
        asym_label = Text("Vertical Asymptote at x = 0", color=RED, font_size=20
                         ).next_to(title, DOWN * 1.5, buff=0.4)

        # Show initial graph
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(left), Create(right), Write(title))
        self.play(Create(asymptote), FadeIn(asym_label))
        self.wait(1)
        self.play(FadeOut(x_label, title, asym_label))


        # Green dot + live coordinate label (plain Text, no LaTeX)
        dot = Dot(color=GREEN, radius=0.09)
        x_tracker = ValueTracker(3.0)

        coord_label = always_redraw(lambda: Text(
            f"x = {x_tracker.get_value():.7f}\n"
            f"y = {f(x_tracker.get_value()):.1f}",
            font_size=32,
            color=GREEN
        ).next_to(dot, UR, buff=0.3))

        dot.add_updater(lambda d: d.move_to(axes.c2p(x_tracker.get_value(), f(x_tracker.get_value()))))

        self.add(dot, coord_label)
        self.play(FadeIn(dot))
        self.play(x_tracker.animate.set_value(0.1), run_time=16, rate_func=slow_into)
        self.wait(0.8)

        # ------------------- Zoom Sequence -------------------
        zoom_values = [0.025, 0.0025, 0.00025]

        for i, x_val in enumerate(zoom_values):
            y_val = f(x_val)

            # Create zoomed-in axes centered near (x_val, y_val)
        # ------------------- Zoom Sequence (with proper title fading) -------------------
        zoom_values = [0.025, 0.0025, 0.00025]
        current_zoom_title = None  # Keep track of the current title

        for i, x_val in enumerate(zoom_values):
            y_val = f(x_val)

            # Create new zoomed axes
            zoom_level = 15 if i == 0 else 80 if i == 1 else 600
            new_axes = Axes(
                x_range=[x_val - x_val*zoom_level, x_val + x_val*zoom_level, x_val/5],
                y_range=[0, y_val*1.3, y_val/10],
                x_length=10,
                y_length=6,
                tips=False,
                axis_config={"color": WHITE}
            )

            new_right = new_axes.plot(f, x_range=[x_val, x_val + x_val*zoom_level], color=YELLOW)
            new_asymptote = DashedLine(
                new_axes.c2p(0, 0), new_axes.c2p(0, y_val*1.5),
                color=RED, stroke_width=6
            )

            # New title for this zoom level
            new_zoom_title = Text(
                f"Zoom {i+1}: x = {x_val}",
                color=PURPLE,
                font_size=44
            ).to_corner(UL)

            # Animation list
            anims = [
                ReplacementTransform(axes, new_axes),
                ReplacementTransform(right, new_right),
                ReplacementTransform(asymptote, new_asymptote),
                x_tracker.animate.set_value(x_val),
            ]

            # Fade out previous title (only if it exists)
            if current_zoom_title is not None:
                anims.append(FadeOut(current_zoom_title))

            # Always fade in the new title
            anims.append(FadeIn(new_zoom_title, shift=DOWN))

            # Also fade out axis labels after first zoom (they become meaningless when zoomed)
            if i == 0:
                anims.append(FadeOut(x_label, y_label))

            # Play all together
            self.play(*anims, run_time=12)

            # Update references
            axes = new_axes
            right = new_right
            asymptote = new_asymptote
            current_zoom_title = new_zoom_title  # remember for next fade out

            self.wait(1.8)

        # Final fade out of the last zoom title before showing the conclusion
        self.play(FadeOut(current_zoom_title), run_time=1)

        # ------------------- Final Message -------------------
                # Clear everything that’s still on screen
        self.play(
            FadeOut(
                axes, right, left, asymptote, coord_label # in case any survived
            ),
            run_time=1.5
        )

        # Now show only the final message
        final = VGroup(
            Text("As x gets closer and closer to 0 from the right...", font_size=42),
            Text("y explodes to +infinity", font_size=72, color=GREEN),
            Text("That's the terrifying power", font_size=48),
            Text("of a VERTICAL ASYMPTOTE!", font_size=68, color=RED)
        ).arrange(DOWN, center=False, aligned_edge=LEFT).to_corner(DL)

        self.play(
            Write(final),
            run_time=4
        )
        self.wait(5)