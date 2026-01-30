# LEDs: Faro de Policía
# ¡Atención! El robot patrulla la zona.

import machine
import neopixel
import time

NUM_LEDS = 10 
np = neopixel.NeoPixel(machine.Pin(22), NUM_LEDS)

def patrulla():
    print("¡PI-PO-PI-PO! Sirenas activadas.")
    for _ in range(10): # Repetir 10 veces
        # Mitad rojos, mitad azules
        for i in range(5): np[i] = (255, 0, 0)
        for i in range(5, 10): np[i] = (0, 0, 255)
        np.write()
        time.sleep(0.2)
        
        # Intercambiar
        for i in range(5): np[i] = (0, 0, 255)
        for i in range(5, 10): np[i] = (255, 0, 0)
        np.write()
        time.sleep(0.2)
    
    # Apagar al terminar
    for i in range(NUM_LEDS): np[i] = (0,0,0)
    np.write()

patrulla()
