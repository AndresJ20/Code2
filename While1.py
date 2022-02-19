"""op = -1
while op != 0:
    print("<1> Sumar")
    print("<2> Restar")
    print("<3> Multiplicar")
    print("<4> Dividir")
    print("<0> Sair")

    op = int(input("Ingrese opción: "))

    if op != 0:
        num1 = int(input("Ingrese num1: "))
        num2 = int(input("Ingrese num2: "))

    if op == 1:
        print("Suma: ", num1+num2)
    elif op == 2:
        print("Resta: ", num1-num2)
    elif op == 3:
        print("Multiplicación: ", num1 * num2)
    elif op == 4: 
        print("División: ", num1/num2)
    else:
        print("No existe esa opción")"""

import random
# 1 = piedra
# 2 = papel
# 3 = tijera
# <1> Jugar
    # Elegir una opción
# <2> Resultados
    # ¿Gané? ¿Perdí? ¿Empaté?
# <0> Salir

opcion = -1
while opcion != 0:
    print("<1> Jugar")
    print("<2> Resultados")
    print("<0> Salir")
    opcion = int(input("Ingrese opción: "))
    if opcion == 1:
        print("¡Juguemos!")
    elif opcion == 0:
        print ("Salir")
    
    if opcion == 2:
        print("Resultados: ")

    eleccion_mia = int(input("Ingrese elección: 1. piedra, 2. papel, 3. tijera: "))
    numero_computadora = random.randint(1,3)
    if eleccion_mia == numero_computadora:
        print("Empate")
    elif eleccion_mia == 1:
        if numero_computadora == 2:
            print("Pierdo: ", eleccion_mia, "vs", numero_computadora)
        elif numero_computadora == 3:
            print("Gano: ", eleccion_mia, "vs", numero_computadora)
    elif eleccion_mia == 2:
        if numero_computadora == 1:
            print("Gano: ", eleccion_mia, "vs", numero_computadora)
        elif numero_computadora == 3:
            print("Pierdo: ", eleccion_mia, "vs", numero_computadora)
    elif eleccion_mia == 3:
        if numero_computadora == 2:
            ("Gano: ", eleccion_mia, "vs", numero_computadora)
        elif numero_computadora == 1:
            print("Pierdo: ", eleccion_mia, "vs", numero_computadora)
