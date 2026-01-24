/*
    MAC MINI M4 (2025) + MINISOPURO HUB ENCLOSURE
    Parametric 3D Printable Design
    
    Instructions:
    1. Open this file in OpenSCAD.
    2. Adjust 'tolerance' based on your printer's accuracy.
    3. Press F6 to Render and F7 to Export as STL.
*/

// --- PARAMETERS ---
// Mac Mini M4 Dimensions
mini_side = 127.0; 
mini_height = 50.0;
mini_radius = 20.0; // Corner radius (squircle approximation)

// Hub Dimensions (Minisopuro for M4)
hub_height = 20.0;

// Enclosure Settings
wall_thickness = 3.0;
tolerance = 0.5; // Gap between device and walls (friction fit)
grid_hole_size = 4.0;
grid_spacing = 6.0;

// Internal calculated dimensions
inner_w = mini_side + (tolerance * 2);
inner_h = mini_height + hub_height + (tolerance * 3);
outer_w = inner_w + (wall_thickness * 2);
outer_h = inner_h + wall_thickness;

// --- MODULES ---

module rounded_box(w, h, r, height) {
    linear_extrude(height)
    offset(r = r)
    square([w - 2*r, w - 2*r], center = true);
}

module side_ventilation_grid() {
    grid_w = mini_side - 40;
    grid_h = inner_h - 20;
    
    translate([-outer_w/2 - 1, -grid_w/2, 10])
    rotate([0, 90, 0])
    for (x = [0 : grid_spacing : grid_w]) {
        for (y = [0 : grid_spacing : grid_h]) {
            translate([x, y, 0])
            cylinder(d = grid_hole_size, h = wall_thickness + 2, $fn = 6);
        }
    }
}

module port_cutouts() {
    // FRONT: Mac Mini M4 (USB-C & Jack)
    // Centered horizontally, M4 ports are roughly at the bottom of the unit
    translate([-25, -outer_w/2 - 1, 30])
    cube([50, wall_thickness + 2, 15]); // Front generic I/O slot
    
    // REAR: Main Ports
    translate([-mini_side/2 + 10, outer_w/2 - wall_thickness - 1, 25])
    cube([mini_side - 20, wall_thickness + 2, 40]);
}

// --- FINAL ASSEMBLY ---

difference() {
    // 1. Outer Shell
    rounded_box(outer_w, outer_h, mini_radius + wall_thickness, outer_h);
    
    // 2. Inner Hollow Space
    translate([0, 0, wall_thickness])
    rounded_box(inner_w, inner_h, mini_radius, inner_h + 1);
    
    // 3. Top Opening (ensure it's a stackable sleeve)
    translate([0, 0, outer_h - 0.1])
    rounded_box(inner_w, inner_h, mini_radius, 1);

    // 4. Side Grids
    side_ventilation_grid(); // Left side
    rotate([0, 0, 180]) side_ventilation_grid(); // Right side
    
    // 5. Ports
    port_cutouts();
}

// Optional: Visual aids (uncomment to see device mockup)
// %translate([0,0,wall_thickness + tolerance]) rounded_box(mini_side, mini_height, mini_radius, mini_height); // Mac Mini
// %translate([0,0,wall_thickness]) rounded_box(mini_side, hub_height, mini_radius, hub_height); // Hub
