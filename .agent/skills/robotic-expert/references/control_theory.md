# 🎯 Control Theory & Navigation

## 1. PID Control (Proportional-Integral-Derivative)
Used to keep a robot straight or maintain a specific speed.
*   **P (Proportional)**: Corrects based on current error.
*   **I (Integral)**: Corrects based on accumulated past error (removes steady-state offset).
*   **D (Derivative)**: Corrects based on predicted future error (reduces overshoot).

## 2. Odometry & Dead Reckoning
*   **Encoders**: Count motor rotations to calculate distance traveled ($Distance = \text{Ticks} \times \frac{\text{Circumference}}{\text{Ticks per Rev}}$).
*   **IMU (MPU6050/9250)**: Use gyroscopes to maintain heading (Yaw) and accelerometers for tilt.

## 3. Path Planning
*   **A*** (A-star) or **Dijkstra**: For finding the shortest path in a known map.
*   **PID Line Following**: Using IR sensors to track a path with smooth curves.

## 4. Tuning Heuristics
1. Set I and D to zero.
2. Increase P until the system oscillates.
3. Increase D to dampen the oscillation.
4. Increase I only if the system never reaches the target.
