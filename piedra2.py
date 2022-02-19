"""for i in range(10):
    print(i)
print(".......")
i = 0
while i < 10:
    print(i)
    i += 1"""

import random

op = 1
valor = 0
victorias = derrotas = empates = 0; 

while op != 0:
    print("Opción <1>: Jugar")
    print("Opción <2>: Resultados")
    print("Opción <0>: Salir")

    op = int(input("Ingrese opcion: "))

    if op == 1:
        while valor<1 or valor>3:
            valor = int(input("Ingrese un valor: <1>.Piedra, <2>.Papel , <3>.Tijera: "))
            num = random.randint(1,3)

        if valor == num:
            print("Empate:" , "Piedra", "vs", "Piedra")
            empates += 1
        elif valor == 1:
            if num == 2:
                print("Pierde: ", "Piedra", "vs", "Papel")
                derrotas += 1
            elif num == 3:
                print("Ganó: ","Piedra","vs","Tijera")
                victorias += 1
        elif valor == 2:
            if num == 1:
                print("Ganó: ", "Papel", "vs", "Piedra")
                victorias += 1
            elif num == 3:
                print("Pierde: ","Papel", ' vs ',"Tijera")
                derrotas += 1
        elif valor == 3:
            if num == 1:
                print("Pierde:", "Tijera", "vs", "Piedra")
                derrotas += 1
            elif num == 2:
                print("Ganó:","Tijera", "vs", "Papel")
                victorias += 1
    elif op == 2:
        print('Empates:', empates)
        print('Victorias:', victorias)
        print('Derrotas:', derrotas)