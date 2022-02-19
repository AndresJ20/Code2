#Deber if-elif-else Andrés Jaramillo
#Entrada
num1 = int(input("Ingrese un valor: " ))
num2 = int(input("Ingrese un valor: " ))
num3 = int(input("Ingrese un valor: " ))
#Proceso
if num2 < num1 > num3:
#Salida    
    print("El numero mayor es el numero:", num1)
elif num1 < num2 > num3:
#Salida
    print("El numero mayor es el numero:", num2)
elif num1 < num3 > num2:
#Salida
    print("El numero mayor es el numero:", num3)
#Proceso
elif num1 == num2 or num2 == num1:
    print("Los números son iguales", num1)
#Proceso
elif num2 == num3 or num3 == num2:
    print("Los números son iguales", num2)
elif num1 == num3 or num3 == num1:
    print("Los números son iguales", num3)