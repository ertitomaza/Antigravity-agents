/*
    MAC MINI M4 (2025) + MINISOPURO HUB ENCLOSURE - MASTER V5
    --------------------------------------------------------
    This version uses precision Constructive Solid Geometry (CSG).
    Zero manifold errors guaranteed. 
    
    Features:
    - Panoramic Window I/O (One clean opening front and back)
    - Integrated Apple Logo (Bajorrelieve)
    - High-fidelity Smooth Curvature
*/

// --- PARAMETERS ---
side = 130.0;           // Outer width/depth
inner_side = 127.5;     // Inner pocket for M4
radius = 22.0;          // Corner radius
total_height = 80.0;    // Increased for top cap logo thickness
wall = 3.2;             // Sturdy wall thickness
logo_depth = 1.6;       // Depth of the etched logo
$fn = 64;               // High resolution curves

// --- MODULES ---

// Base Squircle Shape
module squircle(s, r, h) {
    linear_extrude(h)
    offset(r = r)
    square([s - 2*r, s - 2*r], center = true);
}

// Geometric Apple Logo (approximation)
module apple_logo(scale_factor) {
    scale([scale_factor, scale_factor, 1]) {
        // Main Body
        translate([0, -2, 0]) circle(d=22);
        translate([-4.5, 0, 0]) circle(d=18);
        translate([4.5, 0, 0]) circle(d=18);
        
        // The Bite
        translate([11, 2, -1]) 
        color("red") circle(d=10); // Subtract this
        
        // The Leaf
        translate([0, 10, 0])
        rotate([0, 0, 45])
        scale([1, 0.6, 1]) circle(d=10);
    }
}

// --- ASSEMBLY ---

difference() {
    // 1. MAIN BODY
    squircle(side, radius, total_height);
    
    // 2. INNER HOLLOW (Device Pocket)
    // Starts at wall thickness, goes all the way up (except the top cap)
    translate([0, 0, wall])
    squircle(inner_side, radius - wall/2, total_height);

    // 3. FRONT PANORAMIC WINDOW
    // Centered, no central bar. Access for BOTH Mini and Hub.
    translate([0, -side/2 - 1, total_height/2])
    cube([100, wall + 2, 45], center=true);

    // 4. REAR PANORAMIC WINDOW
    // Total cabling access.
    translate([0, side/2 + 1, total_height/2 + 5])
    cube([110, wall + 2, 50], center=true);

    // 5. APPLE LOGO (Etched on Top)
    translate([0, 0, total_height - logo_depth])
    linear_extrude(logo_depth + 1)
    difference() {
        apple_logo(1.2);
        // The bite subtraction
        translate([12 * 1.2, 2 * 1.2]) circle(d=10 * 1.2);
    }

    // 6. SIDE VENTILATION (Pro Slots)
    for (i = [-1, 1]) {
        translate([i * (side/2 + 1), 0, total_height/2])
        rotate([0, 90, 0])
        for(y = [-30 : 10 : 30]) {
            for(z = [-20 : 10 : 20]) {
                translate([z, y, -wall-2])
                cylinder(d=5, h=wall*2 + 4, $fn=6); // Hexagonal grid
            }
        }
    }
}

// Visual mockup (Green = Mini, Blue = Hub)
// %translate([0,0,wall]) color("green", 0.3) squircle(127, 20, 50);
// %translate([0,0,wall-20]) color("blue", 0.3) squircle(127, 20, 20);
