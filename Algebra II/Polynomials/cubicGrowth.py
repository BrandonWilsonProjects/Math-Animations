from manim import *

class ExpandingCubicGrowth(ThreeDScene):
    def construct(self):
        # Set camera
        self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES, zoom=1)

        # Title
        title = Text("Cubic Growth = x³ Expansion", font_size=36).to_edge(UP)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))

        # Function to create a unit cube at (x,y,z)
        def unit_cube(x, y, z, color=BLUE):
            cube = Cube(side_length=1, fill_opacity=0.7, fill_color=color, stroke_color=WHITE)
            cube.shift(RIGHT*x + UP*y + OUT*z)
            return cube

        # Function to build cubes up to n³
        def build_to_n(n, start_count=1, color_list=[BLUE, GREEN, RED]):
            cubes = VGroup()
            counter = start_count
            for x in range(n):
                for y in range(n):
                    for z in range(n):
                        cube = unit_cube(x, y, z, color=color_list[(x+y+z) % 3])
                        cubes.add(cube)
                        label = Text(f"Total Cubes = {counter}", font_size=28).to_corner(DOWN+RIGHT)
                        self.add_fixed_in_frame_mobjects(label)
                        self.play(FadeIn(cube, shift=OUT*0.3), run_time=0.05)
                        self.remove(label)
                        counter += 1
            return cubes, counter

        # Step 1: Build 3³ = 27
        cubes3, count = build_to_n(3)
        final_text1 = Text("3³ = 27 Cubes", font_size=28, color=YELLOW).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(final_text1)
        self.play(Write(final_text1))
        self.wait(2)

        # Step 2: Zoom out before 6³
        self.play(FadeOut(final_text1))
        self.move_camera(phi=60 * DEGREES, theta=45 * DEGREES, zoom=0.5, run_time=2)

        # Now build 6³ = 216
        cubes6, count = build_to_n(6, start_count=28)  # continue from 27
        final_text2 = Text("6³ = 216 Cubes", font_size=28, color=YELLOW).to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(final_text2)
        self.play(Write(final_text2))
        self.wait(2)
 