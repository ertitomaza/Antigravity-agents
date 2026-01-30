# Personaje: El Guardián
# ¡Nadie entra en mi cuarto sin permiso!

import time

def patrullar():
    print("Modo GUARDIÁN activo.")
    while True:
        print("Escaneando sector...")
        # Girar un poquito
        # mi_robot.girar_derecha(0.2)
        
        # Si el sensor ve algo a menos de 50cm
        sensor_ve_algo = False
        if sensor_ve_algo:
            print("¡INTRUSO DETECTADO!")
            # faro_policia()
            # sonar_alarma()
        
        time.sleep(2)

print("El Guardián está listo para proteger tus tesoros.")
