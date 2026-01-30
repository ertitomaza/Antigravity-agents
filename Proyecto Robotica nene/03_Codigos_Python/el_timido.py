# Personaje: El Tímido
# Si te acercas... ¡el robot se asusta y huye!

import time
# Nota: Necesita las funciones de 'vista_sonica' y 'marcha_directa'

def modo_timido():
    print("Modo Tímido activado. ¡No te acerques mucho!")
    while True:
        # 1. Medir distancia
        distancia = 20 # Supongamos que medimos 20cm
        
        if distancia < 10:
            print("¡Socorro! ¡Alguien viene!")
            # mi_robot.atras(0.5)
        
        time.sleep(0.1)

# Descomenta para probar (necesita sensores reales conectados)
# modo_timido()
print("Este código es una idea. ¡Combínalo con el sensor ultrasónico!")
