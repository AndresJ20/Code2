import random

from Code.piedra import menu
opcion = -1
huguemos = 1
ganados = 0
empatados = 0
perdidos = 0
piedra = 1
papel = 2
tijera = 3
print("<1> Jugar")
print("<2> Resultados")
print("<3> Regresar")
print("<0> Salir")

menu()

while opcion != 0:
    opcion = int(input("Ingrese opción: "))
if opcion == 1:
    print("¡Juguemos!")
if opcion == 2:
    print("Resultados: ")

    eleccion_mia = int(input("Ingrese elección: 1. piedra, 2. papel, 3. tijera: "))
    numero_computadora = random.randint(1,3)
    if eleccion_mia == numero_computadora:
        print("Empate")
    elif eleccion_mia == 1:
        if numero_computadora == 2:
            print("Pierdo: ",eleccion_mia,"vs",numero_computadora)
        elif numero_computadora == 3:
            print("Gano: ",eleccion_mia,"vs",numero_computadora)
    elif eleccion_mia == 2:
        if numero_computadora == 1:
            print("Gano: ", eleccion_mia, "vs", numero_computadora)
        elif numero_computadora == 3:
            print("Pierdo: ", eleccion_mia, "vs", numero_computadora)
    elif eleccion_mia == 3:
        if numero_computadora == 2:
            print("Gano: ", eleccion_mia, "vs", numero_computadora)
        elif numero_computadora == 1:
            print("Pierdo: ", eleccion_mia, "vs", numero_computadora)
