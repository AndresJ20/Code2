#Deber Andrés Jaramillo
dinero = int(input("Digite el dinero: "))
anho = int(input("Digite cuantos años lleva el trabajador: "))
utilidad = 0
if anho < 1:
    utilidad = dinero * 0.05
if anho >= 1 or anho < 2:
    utilidad = dinero * 0.07
if anho >= 2 or anho < 5:
    utilidad = dinero * 0.10 
if anho >= 5 or anho < 10:
    utilidad = dinero * 0.15 
if anho >= 10:
    utilidad = dinero * 0.20 
print("Valor de utilidades: ", utilidad)