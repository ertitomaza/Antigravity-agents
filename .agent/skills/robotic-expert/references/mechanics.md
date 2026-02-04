# 🏗️ Mechanical Design & Chassis

## 1. Structural Rigidity
*   Avoid cantilevers for heavy components (batteries, large motors).
*   Use triangles (trusses) in 3D design for maximum strength with minimum plastic.
*   **Infill**: 15-25% Gyroid infill is usually sufficient for chassis; use 50%+ for motor mounts.

## 2. Weight Distribution
*   **Center of Mass (CoM)**: Keep it low and between the drive wheels for stability.
*   In 2-wheel + caster robots, place 70% of the weight over the drive wheels to ensure traction.

## 3. Fasteners & Mounting
*   Threaded inserts (M3/M4) are superior to screwing directly into plastic.
*   Leave 0.2mm to 0.4mm tolerance for interlocking 3D printed parts.
*   Cable pathways: Include clips or tunnels in your chassis design to avoid "spaghetti wiring".

## 4. Materials
*   **PLA**: Good for prototyping and rigid frames.
*   **PETG**: Better for parts near motors (heat resistance) and outdoor use.
*   **TPU**: Excellent for bumpers and flexible grippers.
