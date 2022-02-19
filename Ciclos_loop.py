#Bucle While
"""import math
from re import M
numero = int(input("Digite un numero: "))

while numero<0:
    print("Error, digita un numero positivo")
    numero= int(input("Digite un numero: "))

print(f"\nSu raiz cuadrada es: {(math.sqrt(numero)):.2f}")

mensaje = 1
while mensaje<=10:
    print(mensaje) 
    mensaje+= 1"""

#Bucle for
coleccion = {"Alejandro":22}
for i in coleccion:
    print(f"{i}->{coleccion[i]}")
for clave,valor in coleccion.items():
    print(f"{clave}->{valor}")