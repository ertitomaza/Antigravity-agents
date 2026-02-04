# 💻 Robotics Programming Standards

## 1. Non-Blocking Architecture
Robots must be responsive. Standard `time.sleep()` blocks the entire CPU.

**❌ BAD:**
```python
while True:
    move_forward()
    time.sleep(1) # CPU is dead for 1s
    stop()
```

**✅ GOOD (State Machine):**
```python
import time

start_time = time.ticks_ms()
state = "MOVING"

while True:
    current_time = time.ticks_ms()
    if state == "MOVING" and time.ticks_diff(current_time, start_time) > 1000:
        stop()
        state = "STOPPED"
```

## 2. Asynchronous Logic (asyncio)
For complex robots (Pico W / ESP32), use `uasyncio`.
*   Handle sensors, Wi-Fi, and motors in separate tasks.
*   Always keep the event loop running at a consistent frequency.

## 3. Sensor Filtering
Physical sensors are noisy. Implement simple filters:
*   **Moving Average**: Smooth out ultrasonic or accelerometer data.
*   **Hysteresis**: Prevent "fluttering" in decision making (e.g., when to turn on a light).

## 4. Error Handling
*   Watchdog timers (WDT) to reset the MCU if the code hangs.
*   Safe-states: If a sensor fails, the default action must be `STOP()`.
