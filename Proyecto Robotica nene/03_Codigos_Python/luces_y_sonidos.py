# 🌈 El Robot de Colores
# Vamos a usar las luces LED para darle personalidad al coche.

import machine
import neopixel
import time

# El kit Freenove suele traer una tira de LEDs WS2812 (NeoPixels)
# Normalmente conectada al Pin 22. Cambia el 4 por el número de LEDs que tengas.
NUM_LEDS = 10 
pin_leds = machine.Pin(22)
np = neopixel.NeoPixel(pin_leds, NUM_LEDS)

def color_total(r, g, b):
    for i in range(NUM_LEDS):
        np[i] = (r, g, b)
    np.write()

print("Iniciando luces...")

# 1. Flash de Policía
print("¡Emergencia!")
for _ in range(5):
    color_total(255, 0, 0) # Rojo
    time.sleep(0.3)
    color_total(0, 0, 255) # Azul
    time.sleep(0.3)

# 2. Modo Relax
print("Modo tranquilo...")
color_total(0, 255, 0) # Verde
time.sleep(2)

# 3. Apagar
color_total(0, 0, 0)
print("Luces fuera.")
