#Pedir al usurio un valor. Si el valor es positivo
#Pedir un segundo valor y calcular la suma, resta y producto de
#ambos.

num1 = int(input("Ingrese el valor:" ))
num2 = int(input("Ingrese el valor:" ))

if num1 > 0:
    print("El numero:", num1, "es positivo")
else:
    print("El numero negativo")

num3 = int(input("Ingrese el valor:" ))
num4 = int(input("Ingrese el valor:" ))
suma = num3 + num4
resta = num3 - num4
multi = num3 * num4

print("La suma es:" , suma)
print("La resta es:" , resta)
print("La multiplicacion es:" , multi)
