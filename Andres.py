#pi = 3.14
#radio = 5**2
#area = (pi * radio)
#print("El area es:", area)

#num1 = int(input("Ingrese num 1: "))
#num2 = int(input("Ingrese num 2: ")) 
#resultado = num1**2 + num2**2
#resultado = (num1+num2)**2
#resultado = int (num1**(1/3) + 34)
#resultado = (num1 + 34 * num2)**(1/3)
#print("Su resultado es:", resultado)

#nombre = input("Registre su nombre: ")
#print("Su nombre es:", nombre)

#Numero = int(input("Registe un valor: "))
#if Numero == 0:
    #print("El valor es cero")
#elif Numero > 0:
    #print("El valor es positivo")
#else:
    #print("El valor es negativo")

#num1 = int(input("Registe un valor: "))
#num2 = int(input("Registe un valor: "))
#num3 = int(input("Registe un valor: "))
#if num2 < num1 > num3:    
    #print("El numero mayor es el numero:", num1)
#elif num1 < num2 > num3:
    #print("El numero mayor es el numero:", num2)
#elif num1 < num3 > num2:
    #print("El numero mayor es el numero:", num3)
#if num2 == num1 or num1 == num3:    
    #print("Los numeros son iguales:", num1)   
#elif num1 == num2 or num2 == num3:
    #print("Los numeros son iguales:", num2)
#elif num1 == num3 or num3 == num2:
    #print("Los numeros son iguales:", num3)

#num1 = int(input("Registre el año: "))
#if(num1%4 == 0):
    #print("El año es bisiesto")
#elif(num1%100 > 0):
    #print("No es año bisiesto")
#a = 10
#b = 8
#print(((3+5*8)) < 3 and (((-6/3)*4)+2 < 2) or (a > b ))

"""a = input("a -> ")
b = input("b -> ")
a, b = b, a
print("El nuevo valor de a es: ",a)
print("El nuevo valor de b es: ", b)"""

"""import math
radio = int(input("Registre el numero del radio: "))
area = math.pi * radio**2
longitud = 2 * math.pi * radio
print("El area es: ", area)
print("La longitud de la circunferencia es: ", longitud)"""

"""zapatos = float(input("Registe el valor de los zapatos: "))
operacion = zapatos * 0.15
operacion1 = zapatos - operacion
print(f"El precio final es de $ {operacion1:.2f}")"""

#Condicionales
"""numero = int(input("Registre un numero: "))
if numero > 0:
    print("El numero es positivo")
elif numero == 0:
    print("El numero es 0")
else:
    print("El numero es negativo")"""

"""edad = int(input("Digite su edad: "))
if 0 < edad < 100:
    print("Edad correcta")
    if edad >= 18:
        print("Es mayor de edad")
else:
    print("Edad incorrecta")"""

"""numero = int(input("Registre un numero: "))
numero1 = int(input("Registre un numero: "))
if numero%2==0 and numero1%2 ==0:
    print("Ambos son numeros pares")
elif numero%2 == 0 and numero1%2!= 0:
    print(f"{numero} es par")
elif numero1%2 == 0 and numero1%2!= 0:
    print(f"{numero1} es par")
else:
    print("Ambos numeros son impares")"""

"""num1 = int(input("Digite un numero: "))
num2 = int(input("Digite un numero: "))
num3 = int(input("Digite un numero: "))
if num1 >= num2 and num1 >= num3:
    print(f"El numero mayor es: ", num1)
elif num2 >= num1 and num2 >= num3:
    print(f"El numero mayor es: ", num2)
elif num3 >= num1 and num3 >= num2:
    print(f"El numero mayor es: ",num3)"""

"""vocal = input("Ingrese una vocal: ").lower()
if vocal == "a" and "e" and "i" and "o" and "u":
    print("Si es vocal")
else:
    print("No es vocal")"""

"""num1 = float(input("Registe un numero: "))
num2 = float(input("Registe un numero: "))
operacion = input("Digite la operación: ").upper()
if operacion == "S":
    suma = int(num1 + num2)
    print(f"\n La suma es: ",suma)
elif operacion == "R":
    resta = int(num1 - num2)
    print(f"\n La resta es: ",resta)
elif operacion == "M":
    multiplicacion = int (num1 * num2)
    print(f"\n La multiplicacion es: ",multiplicacion)
elif operacion == "D":
    division = int(num1 / num2)
    print(f"\n La division es: ",division)
else:
    print(f"\n Se equivocó de operacion")"""

"""saldo = 1000
print("\t.: MENU:")
print("1. Ingresar dinero en la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar dinero disponible")
print("4. Salir")
opcion = int(input("Digite una opcion de menu: "))

print()

if opcion == 1:
    extra = float(input("¿Cuanto dinero desea ingresar?: "))
    saldo += extra
    print(f"Dinero en la cuenta: {saldo}")
elif opcion ==2:
    retirar = float(input("¿Cuanto dinero desea retirar?: "))
    if retirar > saldo:
        print("No tiene esa cantidad de dinero")
    else:
        saldo -= retirar
        print(f"Dinero en la cuenta: {saldo}")
elif opcion == 3:
    print(f"Dinero en la cuenta: {saldo}")
elif opcion == 4:
    print("Gracias por utilizar su cajero automatico")
else:
    print("Error, se equivocó de opción de menú")"""

#Listas, arreglos o vectores
"""lista = [1,2,3,4,5,"Andrés"]*2
lista = [5,4,-7,9,0,1,3]
lista.sort(reverse=True)
lista.sort()
lista.reverse()
lista.clear()
lista.remove(5)
lista.pop(3)
print(lista)
print(lista.count(2))
print(lista.index(5))
lista1 = [6,7,8]
lista2 = lista + lista1
lista.append(6) Agregar al final
lista.append("Andrés")
lista.insert(2,3) Agregar al principio
lista.extend([6,7,8])
print("Paul" in lista)"""

#Tuplas
"""tupla = (4, "Hola" , 6.78 , [1,2,3] , 4)
lista = list(tupla)
print(lista)"""

#Conjuntos
#conjunto = set()
#conjunto = {1,2,3,"Hola",4.56}
#conjunto.clear()
#conjunto.discard("Hola")
#conjunto.add(5)
#conjunto.add("Adios")
#conjunto.add("a")
#print(4.56 not in conjunto)

#Conjuntos
#a = set()
#a = {}
#a.add(2)
#a = frozenset({1,2,3})
#b = {3,4,5}
#c = {1,2,3,4,5}
#print()(conjuntos inmutables)
#print(a.isdisjoint(b)) (Conexon y disconexon)
# print(c.issuperset(a)) (Superconjunto))
#print(a.issubset(c)) (subconjuntos)
#c = a ^ b (Diferencia simetrica)
#c = a - b (Diferencia de conjuntos)
#c = a & b (Interseccion de conjuntos)
#c = a | b (Union de conjuntos) 
#print(c)

"""#Diccionario
diccionario = {"Alejandro":{"edad":22, "estatura": 1.68},"Jose":[23,1.90],"Maria":[19,1.89]}
#diccionario = {"azul":"blue","rojo":"red" , "verde":"green"}
#diccionario["amarillo"] = "yellow"
#diccionario["azul"] = "BLUE"
#del(diccionario["verde"])
print(diccionario["Alejandro"])"""

"""#Diccionario
equipo = {10:"Luka Modric", 9:"Karim Benzema" , 8: "Toni Kroos" , 20:"O'Rey Vini"}
#equipo.clear()
#print(len(equipo))
#print(equipo.items())
#print(equipo.values())
#print(equipo.keys())
#print(equipo.get(11,"No existe un jugador con ese dorsal"))"""

#Pilas
#pila = [1,2,3]
#Agregando elementos por el final
#pila.append(4)
#pila.append(5)
#pila.append(6)
#print(pila)
#Sacando elemntos por el final
#n = pila.pop()
#print("Sacando el elemento" ,n)
#n = pila.pop()
#print("Sacando el elemento" ,n)
#print(pila)

"""#Cola
cola = ["Maria" , "Alejandro" , "Jose" , "Mario"]
#Agregar elementos al final
cola.append("Karla")
cola.append("Flor")
print(cola)

#Sacar elemento principios de la cola
n = cola.pop(0)
print(f"Estan atendiendo a {n}")
print(cola)"""

"""#1. Eliminar elementos repetidos de una lista
lista = [1,2,3, "Alejandro" ,2,2,1,"Alejandro",3]
lista = list(set(lista))
#conjunto = set(lista)#Eliminar conjuntos repetido
#lista = list(conjunto)
#print(conjunto)
print(lista)"""

#Lista ejercicio 2
"""lista1 = [1,2,3,4,5,4,3,2,2,1,5]
lista2 = [4,5,6,7,8,4,5,6,7,7,8]
#Eliminar elementos repetidos de ambas listas
a = set(lista1)
b = set(lista2)

union = list(a | b)
soloA = list(a - b)
soloB = list(b - a)
interseccion = list(a & b)

print("Lista de elementos que aparecen en las dos listas: ",union)
print("Lista de elementos que aparecen en la primera lista pero no en la segunda: ", soloA)
print("Lista de elementos que aparecen en la segunda lista pero no en la primera: ", soloB)
print("Lista de elementos que aparecen en ambas listas: ", interseccion)"""

#Ejercicio 3
"""personajes = [] #Creando una lista vacía
p = {"Nombre":"Aragorn" , "Clase":"Guerrero" , "Raza":"Dunadan del Norte"}
personajes.append(p)
p = {"Nombre":"Gandalf" , "Clase":"Mago" , "Raza":"Istar"}
personajes.append(p)
p = {"Nombre":"Legolas" , "Clase":"Arquero" , "Raza":"Elfo Sindar"}
personajes.append(p)
print(personajes)"""

#Bucles (Se repite)
# Bucle While
"""import math
numero = int(input("Digite un numero: "))
while numero < 0:
    print("Error -> Deberia ser un numero positivo")
    numero = int(input("Digite un numero: "))
print(f"\nSu raiz cuadrada es: {(math.sqrt(numero)):.2f}")
i = 0
while i < 10:
    print("Hola mundo")
    i += 1"""

# Bucle for (Numero determinado, cuantas veces se repite)
coleccion = "Andres"
for i in coleccion:
    #print(f"Hola")
    print(f"{i}",end=" ")

#coleccion = {"Alejandro":22, "Maria": 23,"Jose": 45,"Luis": 12}
#for clave,valor in coleccion.items():
    #print(f"{clave}->{valor}")
#for i in coleccion:
    #print(f"{i}-> {coleccion[i]}")
#coleccion = [2,10,3,4, "Alejandro"]
#for i in [1,2,3,4,5, "Alejandro"]:
    #print(f"Elemento: {i}")
