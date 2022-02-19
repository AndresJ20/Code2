"""precio = float(input("Digite el precio: "))
operacion = precio * 0.15
precio_final= precio - operacion
print(f"El precio final a pagar es de $ {precio_final:.2f}")"""

"""numero = int(input("Digite un numero: "))
if numero > 0:
    print("El numero es positivo")
elif numero == 0:
    print("El numero es 0")
else:
    print("El numero es negativo")"""

"""edad = int(input("Digite su edad: "))
if edad > 0 and edad < 100:
    print("Edad correcta")
    if edad > 18:
        print("Es mayor de edad")
else:
    print("Edad incorrecta")"""

"""numero1 = int(input("Digite un numero: "))
numero2 = int(input("Digite un numero: "))
if numero1%2 == 0 and numero2%2 == 0:
    print("Son pares")
elif numero1%2 == 0 and not numero2%2 == 0:
    print("El par es: ", numero1)
    print("El numero impar es: ", numero2)
elif numero2%2 == 0 and not numero1%2 == 0:
    print("El par es: ", numero2)
    print("El numero impar es: ", numero1)
else:
    print("Ambos son impares")"""

"""num1 = int(input("Digite un numero: "))
num2 = int(input("Digite un numero: "))
num3 = int(input("Digite un numero: "))

if num1 > num2 and num1 > num3:
    print("En numero mayor es: ",num1)
if num2 > num1 and num2 > num3:
    print("En numero mayor es: ",num2)
if num3 > num1 and num3 > num2:
    print("En numero mayor es: ",num3)"""

"""caracter = input("Digite una vocal: ").lower()
if caracter == "a" and "e" and "i" and "o" and "u":
    print("Es una vocal")"""

"""numero1 = int(input("Digite un numero: "))
numero2 = int(input("Digite un numero: "))
operacion = input("Digite una operacion: ").upper()
if operacion == "S":
    suma = numero1 + numero2
    print(suma)
elif operacion == "R":
    resta = numero1 - numero2
    print(resta)
elif operacion == "M":
    multiplicacion = numero1 * numero2
    print(multiplicacion)
elif operacion == "D":
    division = numero1 / numero2
    print(division)
else: 
    print("Se equivoco de operacion")"""

"""saldo = 1000
print("Hola soy tu cajero automatico")
print("1. Ingresar dinero en la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar dinero de la cuenta")
print("4. Salir")
operacion = int(input("¿Que operacion desea realizar?: "))
if operacion == 1:
    dinero = int(input("Digite su dinero extra: ")) 
    suma = saldo + dinero
    print(f"Su nuevo saldo es de $ {suma}")
if operacion == 2:
    dinero = int(input("¿Cuanto dinero desea retirar?: ")) 
    resta = saldo - dinero
    print(f"Su nuevo saldo es de $ {resta}")
    saldo > dinero
    print("No dispone de esa cantidad")
if operacion == 3:
    print(f"Su dinero disponible en la cuenta es de {saldo}")
if operacion == 4:
    print("Muchas gracias por su visita")"""

#LISTAS
"""lista = [1,2,4,5]
lista.append(6) #Agrega elementos al final
lista.append("Andres")
lista.insert(2,3) #Agrega elementos 1° ubicacion 2°elemento
lista.extend([7,8,9])#Concatenar elementos de la lista
lista1=[1,2,3,4,5]
lista2=[6,7,8]
lista3= lista1+lista2
print(lista3)
print(lista3.index(5)) #Ubicacion
print(8 in lista3) #Condicion True or False
lista4 = [1,2,3,4,5,"Andres",1,2,3,1,"Andres",1]
print(lista4.count("Andres")) #Contar
lista4.pop()#Elimina el ultimo elemento o ubicacion
print(lista4)
lista.remove("Andres") #Elimina directamente el elemento
lista.clear()#Elimina todos los elementos
lista.reverse()#Los valores se intercambia
lista5= [5,4,-7,9,0,1,3]
lista5.sort()#Forma ascendente
lista5.sort(reverse=True)#Forma descendente
print(lista5)
print("El numero de elementos de la lista es: ", len(lista)) #Cuenta los elementos de la lista"""

#TUPLAS SON INMUTABLES
tupla = (4,"Hola",6.78,[1,2,3],4)
lista = list(tupla)
print(tupla[0])
print(4 in tupla)
print(tupla.index("Hola"))
print(tupla.count(4))
print(len(tupla))
print(lista)

lista = [4,"hola",6.78,[1,2,3],4]
tupla = tuple(lista)
print(tupla)