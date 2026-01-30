# Movimiento: Diagonal Ninja
# ¡Moverse en 45 grados!

import time

def diagonal_arriba_derecha():
    print("Moviendo en diagonal hacia adelante y derecha...")
    # Solo se mueven dos ruedas: FL y RR hacia adelante

def diagonal_arriba_izquierda():
    print("Moviendo en diagonal hacia adelante e izquierda...")
    # Solo se mueven FR y RL hacia adelante

diagonal_arriba_derecha()
time.sleep(2)
diagonal_arriba_izquierda()
time.sleep(2)
print("¡Ataque ninja terminado!")
