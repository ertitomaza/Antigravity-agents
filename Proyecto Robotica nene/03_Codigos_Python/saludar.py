# Truco: Saludar
# El robot es muy educado.

import time

def saludar():
    print("¡Hola, amigo humano!")
    for _ in range(3):
        # Moverse un poquito adelante y atrás rápido
        print("(Inclinación...)")
        time.sleep(0.2)
        print("(Vuelve...)")
        time.sleep(0.2)
    print("¡Listo!")

saludar()
