# Movimiento: Marcha Directa
# ¡Ir adelante y atrás!

from machine import Pin, PWM
import time

# Definición de motores (ejemplo de pines comunes en Freenove)
# Rueda delantera-izquierda (FL), delantera-derecha (FR), trasera-izquierda (RL), trasera-derecha (RR)
# En un coche mecanum, para ir adelante, todas giran en el mismo sentido.

def adelante():
    print("Moviendo ADELANTE...")
    # Aquí configurarías los pines de velocidad (PWM) y dirección
    # fl_motor.speed(100)
    # fr_motor.speed(100)
    # rl_motor.speed(100)
    # rr_motor.speed(100)

def atras():
    print("Moviendo ATRÁS...")
    # fl_motor.speed(-100)
    # ...

def parar():
    print("¡STOP!")

# Prueba: 2 segundos adelante, 2 atrás
adelante()
time.sleep(2)
parar()
time.sleep(1)
atras()
time.sleep(2)
parar()
