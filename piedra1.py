import random
operacion = -1 ; eleccion = -1 ; empates = 0 ; ganados = 0 ; perdidos = 0
def menu ():
    print("Opción <1>: Jugar")
    print("Opción <2>: Resultados")
    print("Opción <3>: Salir")    
while operacion != 0:
    menu ()
    operacion = int(input("Ingrese una opción: "))
    if operacion == 1:
        while eleccion != 0:
            print("Opción <1>: Piedra")
            print("Opción <2>: Papel")
            print("Opción <3>: Tijera")
            print("Opción <0>: Regresar")
            eleccion = int(input("Ingrese el número de juego: "))
            if eleccion == 0:
                menu()
            numero = random.randint(1,3)
                
            if eleccion==1:
                if numero==2:
                    print ("Pierde:", "Piedra", "vs", "Papel")
                    perdidos+=1
                elif numero ==3:
                    print ("Ganó:", "Piedra", "vs","Tijera")
                    ganados+=1
                elif eleccion== numero:
                    print ("Empate:", "Piedra", "vs", "Piedra")
                    empates+=1
                
            if eleccion==2:
                if numero==1:
                    print ("Ganó:", "Papel", "vs", "Piedra")
                    ganados+=1
                elif numero==3:
                    print ("Pierde:", "Papel", "vs", 'Tijera')
                    perdidos+=1
                elif eleccion ==numero:
                    print ("Empate:", "Papel", "vs", 'Papel')
                    empates+=1

                
            if eleccion==3:
                if numero==1:
                    print ("Pierde:", "Tijera", "vs", "Piedra")
                    perdidos+=1
                elif numero==2:
                    print ("Ganó:", "Tijera", "vs", "Papel")
                    ganados=+1
                elif eleccion ==numero:
                    print ("Empate:", "Tijera", "vs", "Tijera")
                    empates+=1
                else:
                    print("Ingrese una opcion correcta")
    elif operacion == 2:
        print("Partidas ganadas: ",ganados)
        print("Partidas perdidas: ", perdidos)
        print("Partidas empatados: ",empates)
    elif operacion == 3:
        quit()
    else:
        print("Ingrese la opción correcta")
