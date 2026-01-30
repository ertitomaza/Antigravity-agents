# LEDs: Arcoíris
# ¡Colores mágicos que fluyen!

import machine, neopixel, time, math

np = neopixel.NeoPixel(machine.Pin(22), 10)

def rueda(pos):
    # Genera un color basado en una posición de 0 a 255
    if pos < 0 or pos > 255: return (0, 0, 0)
    if pos < 85: return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

print("Mostrando arcoíris...")
for j in range(255): # Ciclo de colores
    for i in range(10): # Cada LED
        rc_index = (i * 256 // 10) + j
        np[i] = rueda(rc_index & 255)
    np.write()
    time.sleep(0.01)

# Apagar
for i in range(10): np[i] = (0,0,0)
np.write()
