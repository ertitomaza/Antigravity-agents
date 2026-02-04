# ⚡ Electronics & Power Management

## 1. Common Ground (GND)
*   **CRITICAL**: All components (MCU, Motor Drivers, Sensors) MUST share a common Ground pin to have a 0V reference point.

## 2. Power Supplies
*   **LiPo (Lithium Polymer)**: High power density. Requires a balanced charger and a low-voltage alarm (never go below 3.2V per cell).
*   **Voltage Regulators**: Use switching regulators (buck converters) instead of linear regulators (LM7805) for battery-powered projects to improve efficiency.

## 3. Wiring Best Practices
*   **Color Coding**: 
    *   🔴 Red: VCC / Positive
    *   ⚫ Black: GND / Negative
    *   🟡 Yellow/🟠 Orange: Data / Signal
*   **Thick Wires**: Use thicker gauge wires for high-current paths (batteries to motor drivers).

## 4. EMI & Noise Reduction
*   Keep signal wires away from high-current motor wires.
*   Twist motor wire pairs to cancel out electromagnetic fields.
*   Use logic level shifters if connecting 5V sensors to 3.3V MCUs (like the Pi Pico).
