from manim import *
import numpy as np

class LineSegmentPower(ThreeDScene):
    """Complete demonstration of the power of line segments"""
    def construct(self):
        # INTRO: Title Sequence
        title = Text("The Power of Line Segments", font_size=56, gradient=(BLUE, PURPLE, PINK))
        subtitle = Text("Building blocks of geometry", font_size=28, color=GRAY).next_to(title, DOWN)
        
        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle, shift=UP))
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # PART 1: VECTORS AND LINEAR TRANSFORMATIONS
        section1_title = Text("Vectors & Linear Transformations", font_size=42)
        self.play(Write(section1_title))
        self.wait(3)
        self.play(FadeOut(section1_title))
                
        # Create a beautiful coordinate system
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-4, 4, 1],
            x_length=10,
            y_length=7,
            axis_config={
                "color": BLUE_E,
                "stroke_width": 2,
                "include_tip": True,
                "tip_length": 0.2,
            }
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        # Add grid for better visualization
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
                "stroke_opacity": 0.3,
            }
        )
        
        self.play(Create(grid), run_time=1)
        self.play(Create(axes), Write(axes_labels))
        self.wait(0.5)
        
        # Create basis vectors with glow effect
        i_hat = Arrow(axes.c2p(0, 0), axes.c2p(1, 0), buff=0, color=GREEN, stroke_width=6)
        j_hat = Arrow(axes.c2p(0, 0), axes.c2p(0, 1), buff=0, color=RED, stroke_width=6)
        
        i_label = Text("i", color=GREEN, font_size=36).next_to(i_hat, DOWN)
        j_label = Text("j", color=RED, font_size=36).next_to(j_hat, LEFT)
        
        basis_text = Text("Basis Vectors", font_size=28, color=YELLOW).to_corner(UL)
        
        self.play(Write(basis_text))
        self.play(GrowArrow(i_hat), Write(i_label))
        self.play(GrowArrow(j_hat), Write(j_label))
        self.wait(1)
        
        # Create multiple vectors emanating from origin
        vectors = []
        vector_colors = [BLUE, PURPLE, ORANGE, PINK, TEAL]
        vector_endpoints = [
            axes.c2p(3, 2),
            axes.c2p(-2, 3),
            axes.c2p(2, -2),
            axes.c2p(-3, -1),
            axes.c2p(1, 3)
        ]
        
        vector_text = Text("Vectors as line segments", font_size=28, color=YELLOW).to_corner(UL)
        self.play(Transform(basis_text, vector_text))
        
        for i, (endpoint, color) in enumerate(zip(vector_endpoints, vector_colors)):
            vec = Arrow(axes.c2p(0, 0), endpoint, buff=0, color=color, stroke_width=5)
            vectors.append(vec)
            self.play(GrowArrow(vec), run_time=0.5)
        
        self.wait(1)
        
        # Show vector addition with beautiful animation
        self.play(FadeOut(basis_text), FadeOut(i_hat), FadeOut(j_hat), 
                  FadeOut(i_label), FadeOut(j_label))
        self.play(*[FadeOut(v) for v in vectors[2:]])
        
        v1 = vectors[0]
        v2 = vectors[1]
        
        # Scale down the vectors to keep them in frame
        v1_scaled_end = axes.c2p(2, 1.5)  # Reduced from (3, 2)
        v2_scaled_end = axes.c2p(-1.5, 2)  # Reduced from (-2, 3)
        
        v1_scaled = Arrow(axes.c2p(0, 0), v1_scaled_end, buff=0, color=BLUE, stroke_width=5)
        v2_scaled = Arrow(axes.c2p(0, 0), v2_scaled_end, buff=0, color=PURPLE, stroke_width=5)
        
        self.play(
            Transform(v1, v1_scaled),
            Transform(v2, v2_scaled),
            run_time=1
        )
        
        # Update the endpoints for the rest of the animation
        vector_endpoints[0] = v1_scaled_end
        vector_endpoints[1] = v2_scaled_end
        
        addition_text = Text("Vector Addition", font_size=32, color=YELLOW).to_corner(UL)
        self.play(Write(addition_text))
        
        # Animate v2 sliding to the tip of v1
        v2_copy = v2.copy()
        v2_shifted_start = v1_scaled_end
        v2_shifted_end = axes.c2p(0.5, 3.5)  # 2 + (-1.5), 1.5 + 2
        v2_shifted = Arrow(v2_shifted_start, v2_shifted_end, buff=0, color=PURPLE, stroke_width=5)
        
        # Draw parallelogram
        para_line1 = DashedLine(vector_endpoints[0], v2_shifted_end, color=YELLOW, stroke_width=2)
        para_line2 = DashedLine(vector_endpoints[1], v2_shifted_end, color=YELLOW, stroke_width=2)
        
        self.play(Transform(v2_copy, v2_shifted), run_time=1.5)
        self.play(Create(para_line1), Create(para_line2))
        
        # Show resultant
        v_sum = Arrow(axes.c2p(0, 0), v2_shifted_end, buff=0, color=GREEN, stroke_width=8)
        v_sum_label = Text("v1 + v2", color=GREEN, font_size=32).next_to(v_sum, RIGHT*6)
        
        self.play(GrowArrow(v_sum), Write(v_sum_label), run_time=1.5)
        self.wait(1.5)
        
        # Clear for transformation
        self.play(
            FadeOut(v2_copy), FadeOut(para_line1), FadeOut(para_line2),
            FadeOut(v_sum), FadeOut(v_sum_label)
        )
        
        # LINEAR TRANSFORMATION - The spectacular part
        transform_text = Text("Linear Transformation", font_size=32, color=YELLOW).to_corner(UL)
        self.play(Transform(addition_text, transform_text))
        
        matrix_text = Text("Rotation + Scaling", font_size=24, color=ORANGE).to_corner(UR)
        self.play(Write(matrix_text))
        
        # Create a grid of vectors to show transformation
        test_vectors = VGroup()
        for x in range(-4, 5, 1):
            for y in range(-3, 4, 1):
                if x == 0 and y == 0:
                    continue
                point = axes.c2p(x, y)
                dot = Dot(point, color=BLUE_B, radius=0.05)
                test_vectors.add(dot)
        
        self.play(FadeIn(test_vectors), run_time=1)
        
        # Apply transformation matrix: rotation by 45 degrees + scaling
        angle = PI / 4
        scale = 0.8
        transform_matrix = np.array([
            [scale * np.cos(angle), -scale * np.sin(angle)],
            [scale * np.sin(angle), scale * np.cos(angle)]
        ])
        
        # Transform all elements
        def apply_transform(point):
            coords = axes.p2c(point)
            new_coords = transform_matrix @ np.array([coords[0], coords[1]])
            return axes.c2p(new_coords[0], new_coords[1])
        
        # Transform vectors
        new_v1_end = apply_transform(vector_endpoints[0])
        new_v2_end = apply_transform(vector_endpoints[1])
        
        new_v1 = Arrow(axes.c2p(0, 0), new_v1_end, buff=0, color=BLUE, stroke_width=5)
        new_v2 = Arrow(axes.c2p(0, 0), new_v2_end, buff=0, color=PURPLE, stroke_width=5)
        
        # Create transformed grid
        new_test_vectors = VGroup()
        for dot in test_vectors:
            new_pos = apply_transform(dot.get_center())
            new_dot = Dot(new_pos, color=ORANGE, radius=0.05)
            new_test_vectors.add(new_dot)
        
        # Animate transformation
        self.play(
            Transform(v1, new_v1),
            Transform(v2, new_v2),
            Transform(test_vectors, new_test_vectors),
            Transform(grid, grid.copy().apply_function(lambda p: apply_transform(p))),
            run_time=3,
            rate_func=smooth
        )
        self.wait(2)
        
        # Cleanup
        self.play(
            *[FadeOut(mob) for mob in [v1, v2, test_vectors, grid, axes, axes_labels, 
                                        addition_text, matrix_text]]
        )
        self.wait(0.5)
        
        # Transition text
        transition_text = Text("Now, let's combine the concepts of vertices and line segments \nto make surfaces", color=GREEN, font_size=32)
        self.play(FadeIn(transition_text))
        self.wait(4)
        self.play(FadeOut(transition_text))
        
        # PART 2: 3D BOUNDARIES AND MODELING
        section2_title = Text("Defining Boundaries in 3D", font_size=35)
        self.add_fixed_in_frame_mobjects(section2_title)
        section2_title.to_edge(UP)
        self.play(Write(section2_title))
        self.wait(0.5)
        
        # Transition to 3D
        self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES)
        
        # Create 3D axes
        axes_3d = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            z_range=[-4, 4, 1],
            x_length=8,
            y_length=8,
            z_length=8,
            axis_config={
                "color": BLUE_E, 
                "include_tip": True,
                "include_numbers": False
            }
        )
        
        self.play(Create(axes_3d), run_time=2)
        self.wait(0.5)
        
        # Build a wireframe cube with dramatic reveal
        vertices = [
            np.array([2, 2, 2]),
            np.array([2, 2, -2]),
            np.array([2, -2, 2]),
            np.array([2, -2, -2]),
            np.array([-2, 2, 2]),
            np.array([-2, 2, -2]),
            np.array([-2, -2, 2]),
            np.array([-2, -2, -2])
        ]
        
        # Create vertices as glowing dots
        vertex_dots = VGroup(*[
            Dot3D(point=v, color=YELLOW, radius=0.1) for v in vertices
        ])
        
        self.play(FadeIn(vertex_dots), run_time=1.5)
        self.wait(1)
        
        # Create edges with labels
        edges = [
            (0, 1), (0, 2), (0, 4),
            (1, 3), (1, 5),
            (2, 3), (2, 6),
            (3, 7),
            (4, 5), (4, 6),
            (5, 7),
            (6, 7)
        ]
        
        edge_objects = VGroup()
        for start_idx, end_idx in edges:
            edge = Line3D(
                start=vertices[start_idx],
                end=vertices[end_idx],
                color=BLUE,
                thickness=0.025
            )
            edge_objects.add(edge)
        
            self.play(
            *[Create(edge) for edge in edge_objects],
            run_time=3,
            lag_ratio=0.1
        )
        self.wait(1)
        
        # Rotate to show structure
        rotation_angle = PI/3
        rotation_axis = UP
        
        # Create rotation matrix to transform vertices
        def rotate_point(point, angle, axis):
            # Rotation matrix around UP axis (z-axis)
            cos_a = np.cos(angle)
            sin_a = np.sin(angle)
            if np.allclose(axis, UP):
                rotation_matrix = np.array([
                    [cos_a, -sin_a, 0],
                    [sin_a, cos_a, 0],
                    [0, 0, 1]
                ])
            return rotation_matrix @ point
        
        # Rotate all vertex positions
        rotated_vertices = [rotate_point(v, rotation_angle, rotation_axis) for v in vertices]
        
        self.play(Rotate(VGroup(vertex_dots, edge_objects, axes_3d), angle=rotation_angle, axis=rotation_axis), run_time=2)
        self.wait(0.5)
            
        # Highlight front face edges
        front_face_edges = [0, 1, 2, 8, 9, 4]
        for idx in front_face_edges:
            self.play(
                edge_objects[idx].animate.set_color(YELLOW).set_thickness(0.04),
                run_time=0.3
            )
        
        # Create one face using rotated vertices
# Create one face using rotated vertices (invisible first)
        face1_vertices = [rotated_vertices[0], rotated_vertices[4], rotated_vertices[6], rotated_vertices[2]]
        face1 = Polygram(
            *face1_vertices,
            fill_color=BLUE,
            fill_opacity=0,
            stroke_width=0
        )
        
        # Create all faces for a complete solid using rotated vertices (invisible first)
        all_faces = VGroup()
        face_definitions = [
            ([rotated_vertices[0], rotated_vertices[1], rotated_vertices[3], rotated_vertices[2]], RED),
            ([rotated_vertices[4], rotated_vertices[5], rotated_vertices[7], rotated_vertices[6]], GREEN),
            ([rotated_vertices[0], rotated_vertices[1], rotated_vertices[5], rotated_vertices[4]], ORANGE),
            ([rotated_vertices[2], rotated_vertices[3], rotated_vertices[7], rotated_vertices[6]], PURPLE),
            ([rotated_vertices[1], rotated_vertices[3], rotated_vertices[7], rotated_vertices[5]], PINK),
            ([rotated_vertices[0], rotated_vertices[2], rotated_vertices[6], rotated_vertices[4]], TEAL),
        ]
                
        for face_verts, color in face_definitions[1:]:  
            face = Polygram(
                *face_verts,
                fill_color=color,
                fill_opacity=0,
                stroke_width=0
            )
            all_faces.add(face)
        
        # Add faces to scene
        self.add(face1, all_faces)
        
        # Show first face
        self.play(face1.animate.set_opacity(0.4), run_time=1)
        self.wait(1)
        
        # Reset edge colors
        self.play(*[edge_objects[idx].animate.set_color(BLUE).set_thickness(0.025) 
                    for idx in front_face_edges])
        
        # Show all faces
        self.play(*[face.animate.set_opacity(0.4) for face in all_faces], run_time=2)
        self.wait(1)
        
        # Spectacular rotation with all faces
        self.begin_ambient_camera_rotation(rate=0.4)
        self.wait(4)
        self.stop_ambient_camera_rotation()
        
        # Create more complex shape - a pyramid inside
        
        pyramid_vertices = [
            np.array([0, 0, 3]),      # apex
            np.array([1.5, 1.5, -1]),
            np.array([1.5, -1.5, -1]),
            np.array([-1.5, -1.5, -1]),
            np.array([-1.5, 1.5, -1]),
        ]
        
        pyramid_edges = [
            (0, 1), (0, 2), (0, 3), (0, 4),  # apex to base
            (1, 2), (2, 3), (3, 4), (4, 1)   # base
        ]
        
        pyramid_edge_objects = VGroup()
        for start_idx, end_idx in pyramid_edges:
            edge = Line3D(
                start=pyramid_vertices[start_idx],
                end=pyramid_vertices[end_idx],
                color=GOLD,
                thickness=0.03
            )
            pyramid_edge_objects.add(edge)
        
        pyramid_faces = VGroup()
        pyramid_face_defs = [
            ([pyramid_vertices[0], pyramid_vertices[1], pyramid_vertices[2]], GOLD),
            ([pyramid_vertices[0], pyramid_vertices[2], pyramid_vertices[3]], GOLD),
            ([pyramid_vertices[0], pyramid_vertices[3], pyramid_vertices[4]], GOLD),
            ([pyramid_vertices[0], pyramid_vertices[4], pyramid_vertices[1]], GOLD),
            ([pyramid_vertices[1], pyramid_vertices[2], pyramid_vertices[3], pyramid_vertices[4]], ORANGE),
        ]
        
        for face_verts, color in pyramid_face_defs:
            face = Polygram(
                *face_verts,
                fill_color=color,
                fill_opacity=0.5,
                stroke_width=0
            )
            pyramid_faces.add(face)
        
        self.play(
            *[Create(edge) for edge in pyramid_edge_objects],
            run_time=2,
            lag_ratio=0.15
        )
        self.play(*[FadeIn(face) for face in pyramid_faces], run_time=1.5)
        self.wait(1)
        
        # Final rotation showcasing both objects
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        
        # =====================================================================
        # FINALE
        # =====================================================================
        self.play(*[FadeOut(mob) for mob in [face1, all_faces, edge_objects, vertex_dots, 
                                              pyramid_faces, pyramid_edge_objects, 
                                              axes_3d]])
        
        # Reset camera
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES)
        
        finale_title = Text("Line Segments:", font_size=48, color=BLUE)
        finale_subtitle = Text("The Foundation of All Geometry", font_size=36, 
                              gradient=(PURPLE, PINK)).next_to(finale_title, DOWN, buff=0.5)
        finale_group = VGroup(finale_title, finale_subtitle)
        
        self.play(Write(finale_title), run_time=1.5)
        self.play(FadeIn(finale_subtitle, shift=UP))
        self.wait(3)
        self.play(FadeOut(finale_group))