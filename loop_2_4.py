#Leer 5 numeros y obtener el cubo y su cuarta

"""n1 = int(input("Ingrese el numero 1: "))
print("Cubo y cuarta de",n1,"son",n1**3,"y",1**4)
n2 = int(input("Ingrese el numero 2: "))
print("Cubo y cuarta de",n2,"son",n2**3,"y",n2**4)
n3 = int(input("Ingrese el numero 3: "))
print("Cubo y cuarta de",n3,"son",n3**3,"y",n3**4)
n4 = int(input("Ingrese el numero 4: "))
print("Cubo y cuarta de",n4,"son",n4**3,"y",n4**4)
n5 = int(input("Ingrese el numero 1: "))
print("Cubo y cuarta de",n5,"son",n5**3,"y",n5**4)"""

n = 5
cubo_cuarta = 0
for i in range(n):
    numero = int(input("Ingrese un numero: " + str(i+1) + ": "))
    print("Cubo y cuarta de",numero,"son",numero**3,"y",numero**4)
