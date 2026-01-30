# 🕹️ Movimientos del Robot
# Este script te enseña a moverte en todas las direcciones.

from machine import Pin, PWM
import time

# Configuración de los motores (Ejemplo simplificado)
# En el kit Freenove, los pines suelen ser estos:
# Motor A, B, C, D (4 ruedas)
# Nota: Los pines exactos pueden variar según el manual, 
# ¡consúltalo si estos no funcionan!

class Robot:
    def __init__(self):
        # Aquí definimos las "patas" de los motores
        print("Robot listo para correr")

    def adelante(self, segundos):
        print("¡Hacia adelante!")
        # Aquí iría el código para encender motores
        time.sleep(segundos)
        self.parar()

    def atras(self, segundos):
        print("¡Hacia atrás!")
        time.sleep(segundos)
        self.parar()

    def de_lado_izquierda(self, segundos):
        print("¡Deslizamiento lateral a la izquierda!")
        time.sleep(segundos)
        self.parar()

    def parar(self):
        print("Stop.")

# --- TU PROGRAMA EMPIEZA AQUÍ ---
mi_robot = Robot()

# ¡Hagamos una danza!
mi_robot.adelante(1)
time.sleep(0.5)
mi_robot.de_lado_izquierda(1)
time.sleep(0.5)
mi_robot.atras(1)
print("¡Prueba de movimiento completada!")
