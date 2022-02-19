#Calcular el promedio de un alumno que tiene 70 calificaciones de materia de calculo

"""n1 = int(input("Ingrese la nota: "))
n2 = int(input("Ingrese la nota: "))
n3 = int(input("Ingrese la nota: "))
n4 = int(input("Ingrese la nota: "))
n5 = int(input("Ingrese la nota: "))
n6 = int(input("Ingrese la nota: "))
n7 = int(input("Ingrese la nota: "))"""

n = 7
#print(range(n)) 
suma = 0
for i in range(n):
    nota = int(input("Ingrese una nota: " + str(i+1) + ": "))
    suma += nota
promedio = suma/n
print("Promedio: ", promedio)
#suma = n1 + n2 + n3 + n4 + n5 + n6 + n7
#promedio = suma / 7
#print("Su promedio es: ", promedio)