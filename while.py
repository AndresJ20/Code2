#Bucle while ejecuta reptidamente instrucciones dentro del bucle
#Mientras una determinada condicion sigue siendo valida
#Estructura: 
"""while True:
    print("Ejecuto A")"""

#Ingresar numero del 1 al 10

"""numero = -1
while numero < 0:
    numero = int(input("Ingresar numeros positivos: "))
print("......")
if numero>=1 and numero <= 10:
    print("1-10")"""

"""numero = -1
while not(numero >= 1 and numero<= 10):
    numero = int(input("Ingresar numeros positivos: "))"""

#1-10
"""numero = -1
while numero < 1 or numero > 10:
    numero = int(input("Ingresar numero positivo: "))
print(".....")"""

#p = numero >= 1
#q = numero <= 10
#not(p and q) = not p or not q = numero < 1 or numero > 10

# 10-20
"""numero = -1
while numero < 10 or numero > 20:
    numero = int(input("Registre numeros dentro del rango: "))"""

#10-20 pares
"""if numero >= 10 and numero <= 20 and numero%2 == 0:
    pass"""

numero = 11
#while not(numero >= 10 and numero <= 20 and numero%2 == 0):
    #numero = int(input("Digite numeros positivos: "))

while numero < 10 or numero > 20 or numero%2 != 0:
    numero = int(input("Ingresar numeros positivos: "))
