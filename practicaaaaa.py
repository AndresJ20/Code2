"""n = 4
suma = 0
for a in range (n):
    numero = int(input("Ingrese la nota: " + str(a+1) + ": "))
    suma = suma + numero
    media = suma/n    
print("La suma es: ", suma)
print("La media es: ", media)"""

"""n = 4
suma = 0
for a in range (n):
    numero = int(input("Ingrese la nota: " + str(a+1) + ": "))
    suma = suma + numero
    media = suma/n    
print("La suma es: ", suma)
print("La media es: ", media)
if numero <= 7:
    print("La calificacion mas baja es: ", numero)"""

"""n = int(input("Digite un numero: "))
for i in range(1,13):
    print(f"{i}x{n}:",i*n)"""

"""n = int(input("Digite un numero: "))
for i in range(1,13):
    print(f"La multiplicacion es: {i}*{n}=",i*n)"""

"""for i in range(101,201):
    if i%2 == 0:
        print(i)

suma = 0
for a in range (101,201):
    suma = suma + a
print("La suma es: ", suma)"""

"""for i in range(1,6):
    print(f"Hola el numero de {i}i es: ", i)"""

"""n = int(input("Digite un numero: "))
for i in range(1,13):
    print(f"La multiplicacion {i} x {n} :", i*n)"""

#n = int(input("Digite un numero: "))
for n in range(1,10):
    print("---Tabla del "+str(n)+"---")
    for i in range(10):
        resultado = i * n
        print(i,"x",n,"=",resultado)