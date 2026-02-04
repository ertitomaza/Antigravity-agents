# ⚙️ Actuators: Motors & Servos

## 1. DC Motors
*   **Drivers**: Use L298N (classic), TB6612FNG (efficient), or DRV8833 (low voltage).
*   **PWM**: Frequency usually between 500Hz and 20kHz. Higher frequency reduces "whining" noise but may increase heat in the driver.

## 2. Servos
*   **Standard PWM**: 50Hz (20ms period).
*   **Pulse Width**: 0.5ms (0°) to 2.5ms (180°). Check your specific servo datasheet!
*   **Power**: NEVER power servos directly from the 3.3V/5V pin of the MCU. Use a dedicated 5V-6V power supply with a common ground.

## 3. Stepper Motors
*   Use A4988 or TMC2208 drivers.
*   Always set the Vref (current limit) on the driver to prevent burning out the motor.

## 4. Safety & Protection
*   **Flyback Diodes**: Essential for inductive loads (motors) if not built into the driver.
*   **Decoupling Capacitors**: Use 100uF - 470uF near the motor driver power input to smooth voltage spikes.
