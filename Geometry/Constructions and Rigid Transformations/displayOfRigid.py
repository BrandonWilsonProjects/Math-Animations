from manim import *
import numpy as np

# Utility helpers
def angle_between(v1, v2):
    """Signed angle from v1 to v2 in the plane (z=0), using atan2 of cross & dot."""
    x1, y1 = v1[0], v1[1]
    x2, y2 = v2[0], v2[1]
    dot = x1 * x2 + y1 * y2
    cross = x1 * y2 - y1 * x2  # z-component of 2D cross
    return np.arctan2(cross, dot)

def reflect_points_across_line(points, P, Q):
    """
    Reflect an array of 2D points across the line through P->Q.
    P, Q are 3D numpy vectors (z=0). Returns an array of reflected points (3D).
    """
    # Shift so P is origin
    u = (Q - P)[:2]
    u = u / np.linalg.norm(u)  # unit direction vector along the line
    ux, uy = u[0], u[1]
    # Reflection matrix across a unit vector direction u in 2D:
    # R = [[2*ux^2 - 1, 2*ux*uy],
    #      [2*ux*uy,    2*uy^2 - 1]]
    R = np.array([[2*ux*ux - 1, 2*ux*uy],
                  [2*ux*uy,     2*uy*uy - 1]])
    out = []
    for pt in points:
        v = (pt - P)[:2]
        rv = R @ v
        new2 = rv + P[:2]
        out.append(np.array([new2[0], new2[1], 0.0]))
    return np.array(out)

def orientation(A, B, C):
    """Positive if ABC is counterclockwise, negative if clockwise, ~0 if collinear."""
    return np.sign((B[0]-A[0])*(C[1]-A[1]) - (B[1]-A[1])*(C[0]-A[0]))

def triangle_with_labels(A, B, C, label_prefix="", color=BLUE):
    tri = Polygon(A, B, C, color=color, stroke_width=4)
    dA, dB, dC = Dot(A, color=color), Dot(B, color=color), Dot(C, color=color)
    tA = Text(f"{label_prefix}A", font_size=28).next_to(dA, UL, buff=0.15)
    tB = Text(f"{label_prefix}B", font_size=28).next_to(dB, UR, buff=0.15)
    tC = Text(f"{label_prefix}C", font_size=28).next_to(dC, DOWN, buff=0.15)
    group = VGroup(tri, dA, dB, dC, tA, tB, tC)
    return group

def get_points_from_group(group):
    # group: [Polygon, DotA, DotB, DotC, labelA, labelB, labelC]
    poly = group[0]
    A = poly.get_vertices()[0]
    B = poly.get_vertices()[1]
    C = poly.get_vertices()[2]
    return A, B, C

class UniquenessOfIsometries(Scene):
    """
    This scene demonstrates (an essential version of) the uniqueness of the rigid transformation (isometry)
    that maps one non-degenerate triangle ΔABC to another ΔA'B'C' with a specified correspondence.
    Steps:
      1) Translate so A -> A'
      2) Rotate about A' so AB -> A'B'
      3) If orientation mismatches, reflect across line A'B'
    The final image coincides with ΔA'B'C'.
    """
    def construct(self):
        # Define two non-degenerate triangles
        A = np.array([-4.0, -1.0, 0.0])
        B = np.array([-2.0,  2.0, 0.0])
        C = np.array([-1.0, -1.5, 0.0])

        # Construct target triangle by an isometry (unknown to the viewer):
        # We'll generate a rotated + translated (possibly reflected) version.
        theta = 0.7  # radians
        R = np.array([[np.cos(theta), -np.sin(theta)],
                      [np.sin(theta),  np.cos(theta)]])
        T = np.array([3.0, 1.0])  # translation vector
        reflect_flag = False      # set True to include a reflection in the "unknown" mapping

        def apply_transform(P):
            v = P[:2]
            v2 = R @ v + T
            if reflect_flag:
                v2 = np.array([v2[0], -v2[1]])  # reflect across x-axis as example
            return np.array([v2[0], v2[1], 0.0])

        Aprime = apply_transform(A)
        Bprime = apply_transform(B)
        Cprime = apply_transform(C)

        # Draw the source and target triangles
        src = triangle_with_labels(A, B, C, label_prefix="", color=BLUE_D)
        tgt = triangle_with_labels(Aprime, Bprime, Cprime, label_prefix="'", color=GREEN_D)

        # Guide lines for AB and A'B'
        line_AB = Line(A, B, color=BLUE_D, stroke_width=3)
        line_ApBp = Line(Aprime, Bprime, color=GREEN_D, stroke_width=3)

        self.play(Create(src), run_time=1.5)
        self.play(Create(tgt), run_time=1.5)
        self.play(Create(line_AB), Create(line_ApBp))
        self.wait(0.5)

        # Step labels
        step1 = Text("Step 1: Translate A onto A'", font_size=30, color=YELLOW).to_edge(DOWN)
        step2 = Text("Step 2: Rotate about A' to align AB with A'B'", font_size=30, color=YELLOW).to_edge(DOWN)
        step3 = Text("Step 3: Reflect across line A'B' if orientation differs", font_size=30, color=YELLOW).to_edge(DOWN)
        complete = Text("Result: ΔABC matches ΔA'B'C' (Isometry essentially unique)", font_size=30, color=YELLOW).to_edge(DOWN)

        # --- Step 1: Translate A to A' ---
        self.play(ReplacementTransform(step1.copy().set_opacity(0), step1))
        shift_vec = Aprime - A
        self.play(src.animate.shift(shift_vec), line_AB.animate.shift(shift_vec), run_time=1.5)
        self.wait(0.5)

        # Update current positions
        A1, B1, C1 = get_points_from_group(src)

        # --- Step 2: Rotate about A' (which equals A1 now) to align AB with A'B' ---
        self.play(ReplacementTransform(step1, step2))

        v1 = (B1 - A1)[:2]
        v2 = (Bprime - Aprime)[:2]
        ang = angle_between(v1, v2)  # signed angle to rotate v1 into v2

        # Rotate the entire src group and the AB line about A' by angle 'ang'
        self.play(
            src.animate.rotate(ang, about_point=Aprime),
            line_AB.animate.rotate(ang, about_point=Aprime),
            run_time=1.5
        )
        self.wait(0.5)

        # Update positions after rotation
        A2, B2, C2 = get_points_from_group(src)

        # --- Step 3: Orientation check & possible reflection across A'B' ---
        self.play(ReplacementTransform(step2, step3))

        ori_src = orientation(A2, B2, C2)
        ori_tgt = orientation(Aprime, Bprime, Cprime)

        if ori_src != 0 and ori_tgt != 0 and ori_src != ori_tgt:
            # Reflect across the target line A'B'
            P, Q = Aprime, Bprime
            # Reflect polygon vertices and dots
            poly = src[0]
            dA, dB, dC = src[1], src[2], src[3]
            tA, tB, tC = src[4], src[5], src[6]

            verts = poly.get_vertices()
            new_verts = reflect_points_across_line(verts, P, Q)

            new_A = reflect_points_across_line(np.array([dA.get_center()]), P, Q)[0]
            new_B = reflect_points_across_line(np.array([dB.get_center()]), P, Q)[0]
            new_C = reflect_points_across_line(np.array([dC.get_center()]), P, Q)[0]

            # Animate polygon vertex movement using Transform to new polygon
            poly_new = Polygon(*new_verts, color=BLUE_D, stroke_width=4)
            self.play(Transform(poly, poly_new), run_time=1.2)

            # Move dots & labels
            self.play(
                dA.animate.move_to(new_A),
                dB.animate.move_to(new_B),
                dC.animate.move_to(new_C),
                run_time=1.0
            )
            # Reposition labels near their points to keep them readable
            tA.next_to(dA, UL, buff=0.15)
            tB.next_to(dB, UR, buff=0.15)
            tC.next_to(dC, DOWN, buff=0.15)

        self.wait(0.3)
        self.play(ReplacementTransform(step3, complete))
        self.wait(0.6)

        # Emphasize correspondence arrows
        arrowA = Arrow(Aprime + LEFT*0.8, Aprime + RIGHT*0.8, buff=0.05, color=YELLOW)
        arrowB = Arrow(Bprime + DOWN*0.8, Bprime + UP*0.8, buff=0.05, color=YELLOW)
        arrowC = Arrow(Cprime + LEFT*0.8, Cprime + RIGHT*0.8, buff=0.05, color=YELLOW)

        gmatch = VGroup(arrowA, arrowB, arrowC)
        self.play(Create(gmatch), run_time=0.8)

        box = SurroundingRectangle(tgt, color=YELLOW, buff=0.2)
        self.play(Create(box))
        self.wait(1.0)