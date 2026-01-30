# LEDs: Semáforo
# ¡Enseña al robot las reglas de tráfico!

import machine, neopixel, time

np = neopixel.NeoPixel(machine.Pin(22), 10)

def set_color(r, g, b):
    for i in range(10): np[i] = (r, g, b)
    np.write()

print("SEMÁFORO EN MARCHA")
print("ROJO: ¡Párate!")
set_color(255, 0, 0)
time.sleep(3)

print("AMARILLO: ¡Prepárate!")
set_color(255, 150, 0)
time.sleep(1)

print("VERDE: ¡Adelante!")
set_color(0, 255, 0)
time.sleep(3)

set_color(0, 0, 0)
