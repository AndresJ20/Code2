#Deber Andrés Jaramillo
"""num1 = int(input("Ingrese un valor: " ))

if num1 == 0:
    print("Grado celsius")

elif num1 <= 0: 
    print("Estado solido")

elif num1 >= 100:
    print("Estado gaseoso")

else: 
    print("Estado liquido")"""

temperatura = int(input("Ingrese la temperatura: "))
if temperatura <= 0:
    print("El estado es solido")
elif temperatura > 0 and temperatura <= 100:
    print("El estado es liquido")
else:
    print("El estado es gaseoso")