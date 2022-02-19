#Calcular el mayor de dos numeros enteros introducidos por teclado

#Entrada
num1 = int(input("Ingrese num 1: "))
num2 = int(input("Ingrese num 2: "))

#Proceso
if num1 > num2:
    print("El numero mayor es:", num1)
elif num2 > num1:
    #Salida
    print("El numero mayor es:", num2)
else:
    print("Los numeros son iguales")

#===========================================================================
if num1 > num2:
    print("El numero mayor es:", num1)
print(".....")

if num2 > num1:
    #Salida
    print("El numero mayor es:", num2)
print("******")

if num1 == num2:
    print("Los numeros son iguales")