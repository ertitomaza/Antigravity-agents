# 🚀 Guía de Inicio: ¡Despertando a tu Robot!

¡Hola, equipo de ingenieros! Aquí tenéis los pasos para que vuestra Raspberry Pi Pico W (el cerebro del coche) esté lista para la acción.

## 1. Instalar Thonny (Tu Centro de Mando)

Para hablar con el robot, usaremos un programa llamado **Thonny**.

- Descárgalo en [thonny.org](https://thonny.org/).
- Es como un traductor: tú escribes en Python y él se lo explica a la Pico W.

## 2. Ponerle el "Sistema Operativo" (MicroPython)

La Pico W necesita saber hablar Python. Sigue estos pasos:

1. Mantén pulsado el botón blanco **BOOTSEL** de la placa.
2. Conéctala al ordenador por USB mientras lo pulsas.
3. Aparecerá en tu ordenador como si fuera un pendrive llamado `RPI-RP2`.
4. Abre Thonny, vete a la esquina inferior derecha y selecciona **"MicroPython (Raspberry Pi Pico)"**.
5. ¡Listo! Thonny instalará lo necesario automáticamente.

## 3. Tu Primera Prueba: "Hola Mundo Robótico"

Escribe esto en la pantalla blanca de Thonny:

```python
import machine
import time

led = machine.Pin("LED", machine.Pin.OUT) # El LED de la placa

while True:
    led.on()  # Enciende
    time.sleep(0.5)
    led.off() # Apaga
    time.sleep(0.5)
```

Dale al botón **PLAY** (el círculo verde). Si el LED de la placa parpadea... **¡ENHORABUENA!** El cerebro está vivo.

## 4. ¿Qué puede hacer esta placa?

- **WiFi:** ¡Puede conectarse a internet o a tu móvil!
- **Pines:** Tiene un montón de "patas" para controlar motores y sensores.
- **MicroPython:** Es el lenguaje más divertido para aprender robótica.
