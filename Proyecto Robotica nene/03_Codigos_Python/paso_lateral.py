# Movimiento: Paso Lateral
# ¡La magia de las ruedas Mecanum! Moverse de lado sin girar.

import time

def lado_derecha():
    print("Deslizándose a la DERECHA...")
    # Rueda FL adelante, FR atrás, RL atrás, RR adelante

def lado_izquierda():
    print("Deslizándose a la IZQUIERDA...")
    # Rueda FL atrás, FR adelante, RL adelante, RR atrás

lado_derecha()
time.sleep(2)
lado_izquierda()
time.sleep(2)
print("¡Cangrejo robótico fuera!")
