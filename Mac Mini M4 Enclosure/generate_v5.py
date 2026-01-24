import math

def generate_enclosure_v5(filename):
    # Dimensions (mm)
    side = 130.0
    inner_side = 127.5
    radius = 22.0
    total_height = 80.0
    wall = 3.2
    points_per_corner = 24 # High resolution for Fusion 360
    
    # Panoramic Window Constraints
    # Front: access for Hub + Mini
    front_win = {"x": [-50, 50], "z": [8, 48]}
    # Rear: total access
    rear_win = {"x": [-55, 55], "z": [20, 65]}

    def get_squircle_points(z, s, r):
        pts = []
        h = s / 2
        inner = h - r
        corners = [(inner, inner, 0), (-inner, inner, 90), (-inner, -inner, 180), (inner, -inner, 270)]
        for dx, dy, start in corners:
            for i in range(points_per_corner + 1):
                angle = math.radians(start + (i * 90 / points_per_corner))
                pts.append((dx + r * math.cos(angle), dy + r * math.sin(angle), z))
        return pts

    # Vertical levels to define window boundaries
    z_levels = sorted(list(set([0, front_win["z"][0], front_win["z"][1], rear_win["z"][0], rear_win["z"][1], total_height])))
    n = len(get_squircle_points(0, side, radius))
    triangles = []

    def add_quad(p1, p2, p3, p4, reverse=False):
        if reverse:
            triangles.append((p1, p3, p2))
            triangles.append((p1, p4, p3))
        else:
            triangles.append((p1, p2, p3))
            triangles.append((p1, p3, p4))

    # Generate Walls
    for zi in range(len(z_levels)-1):
        z_bot, z_top = z_levels[zi], z_levels[zi+1]
        o_bot = get_squircle_points(z_bot, side, radius)
        o_top = get_squircle_points(z_top, side, radius)
        i_bot = get_squircle_points(z_bot, inner_side, radius - wall)
        i_top = get_squircle_points(z_top, inner_side, radius - wall)
        
        mid_z = (z_bot + z_top) / 2
        
        for i in range(n):
            next_i = (i + 1) % n
            # Determine face side (0: Front, 1: Left, 2: Back, 3: Right)
            angle = (i / n) * 360
            side_type = int((angle + 45) % 360 / 90)
            
            is_hole = False
            if side_type == 0 and front_win["x"][0] <= o_bot[i][0] <= front_win["x"][1] and front_win["z"][0] <= mid_z <= front_win["z"][1]:
                is_hole = True
            elif side_type == 2 and rear_win["x"][0] <= o_bot[i][0] <= rear_win["x"][1] and rear_win["z"][0] <= mid_z <= rear_win["z"][1]:
                is_hole = True
                
            if not is_hole:
                # Normal manifold wall segment
                add_quad(o_bot[i], o_bot[next_i], o_top[next_i], o_top[i]) # Outer
                add_quad(i_bot[i], i_top[i], i_top[next_i], i_bot[next_i]) # Inner (reversed)
            else:
                # Bridge walls to close the hole manifold
                # If the segment *below* or *above* was a wall, or if we are at edge of hole
                # We always close the "cut" surface
                add_quad(o_bot[i], o_bot[next_i], i_bot[next_i], i_bot[i]) # Floor of hole
                add_quad(o_top[i], i_top[i], i_top[next_i], o_top[next_i]) # Ceiling of hole
                add_quad(o_bot[i], i_bot[i], i_top[i], o_top[i]) # Left wall of hole
                add_quad(o_bot[next_i], o_top[next_i], i_top[next_i], i_bot[next_i]) # Right wall

    # Bottom Cap
    o_base = get_squircle_points(0, side, radius)
    c_bot = (0, 0, 0)
    for i in range(n):
        triangles.append((c_bot, o_base[(i+1)%n], o_base[i]))
        
    # Top Cap (Simplified Solid for Fusion 360 editing)
    o_top_final = get_squircle_points(total_height, side, radius)
    i_top_final = get_squircle_points(total_height, inner_side, radius - wall)
    for i in range(n):
        add_quad(o_top_final[i], o_top_final[(i+1)%n], i_top_final[(i+1)%n], i_top_final[i])

    with open(filename, 'w') as f:
        f.write("solid enclosure_v5\n")
        for t in triangles:
            f.write("  facet normal 0 0 0\n    outer loop\n")
            for v in t: f.write(f"      vertex {v[0]:.4f} {v[1]:.4f} {v[2]:.4f}\n")
            f.write("    endloop\n  endfacet\n")
        f.write("endsolid enclosure_v5\n")

if __name__ == "__main__":
    generate_enclosure_v5("Mac Mini M4 Enclosure/enclosure_v5_master.stl")
    print("V5 Master STL generated successfully.")
