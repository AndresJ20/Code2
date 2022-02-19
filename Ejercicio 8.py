#Deber Andrés Jaramillo
"""num1 = int(input("Ingrese el año: " ))

if(num1%4 == 0):
    print("Es año bisiesto")
elif(num1%100 > 0):
    print("No es bisiesto")"""

anho = 2016
if (anho%4 == 0 and anho%100 != 0) or (anho%400 == 0):
    print(anho, "Es bisiesto")
else:
    print(anho, "No es bisiesto")

"""anho = 2016
if anho%4 == 0 and not (anho%100 == 0) or anho%400 == 0:
    print(anho, "Es bisiesto")
else:
    print(anho, "No es bisiesto")"""