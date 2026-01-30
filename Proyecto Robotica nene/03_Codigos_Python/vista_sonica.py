# Sensor: Vista Sónica (Ultrasonido)
# ¡No te choques! El robot ve con sonido.

from machine import Pin, time_pulse_us
import time

# Pines típicos para el sensor ultrasónico HC-SR04
TRIG = Pin(13, Pin.OUT)
ECHO = Pin(14, Pin.IN)

def medir_distancia():
    TRIG.low()
    time.sleep_us(2)
    TRIG.high()
    time.sleep_us(10)
    TRIG.low()
    
    # Mide cuánto tarda en volver el sonido
    duracion = time_pulse_us(ECHO, 1, 30000) # 30ms timeout
    distancia = (duracion * 0.0343) / 2 # cm
    return distancia

print("Iniciando Radar...")
try:
    while True:
        d = medir_distancia()
        print("Objeto a:", int(d), "cm")
        
        if d < 15:
            print("¡PELIGRO! ¡Muy cerca!")
            # Aquí podrías llamar a mi_robot.parar()
            
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Radar apagado.")
