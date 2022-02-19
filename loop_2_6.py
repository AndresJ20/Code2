#DEBER ANDRES JARAMILLO
"""n= 3
suma=0
for i in range(n):
    nota=int(input("Ingrese un numero: "))
    suma= suma+nota

print("La suma total es: ", suma)
media_aritmetica =suma/n
print("La media aritmetica es: ", media_aritmetica)"""

n= 5
suma=0
for i in range(n):
    nota = int(input("Ingrese la nota: " + str(i+1) + ": "))
    suma= suma+nota

print("La suma total es: ", suma)
media_aritmetica =suma/n
print("La media aritmetica es: ", media_aritmetica)

if nota < 7:
    print ("la nota mas baja es:",nota)

"""n = 2
for i in range(n):
    numero = int(input('Ingrese numero: '))
    print(f"{numero}x2","=",numero*2)
    print(f"{numero}x3","=",numero*3)
    print(f"{numero}x4","=",numero*4)
    print(f"{numero}x5","=",numero*5)
    print(f"{numero}x6","=",numero*6)
    print(f"{numero}x7","=",numero*7)
    print(f"{numero}x8","=",numero*8)
    print(f"{numero}x9","=",numero*9)
    print(f"{numero}x10","=",numero*10)
    print(f"{numero}x11","=",numero*11)
    print(f"{numero}x12","=",numero*12)"""

"""n = int(input("Ingrese un numero: "))
for i in range (1,13):
    print(f"{i}x{n}= {i*n}")"""

"""import sys
n = 5
suma = 0
menor = sys.maxsize

for i in range(n):
    num = int(input("Ingrese un numero: "))
    suma += num
    if num < menor:
        menor = num
print("Promedio: ", suma/n)
print("Menor: ", menor)"""