#Dada la fecha de hoy, calcular la fecha del dia siguiente, suponer que el año no es bisiesto
"""anho = int(input("Digite el año: "))
if anho%4 == 0 and not anho%100 == 0:
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")"""
"""dia = int(input("Registre el dia: "))
mes = int(input("Registre el mes: "))
anho = int(input("Registre el año: "))
#meses31 = 1 , 3 , 5 , 7 ,8 , 10, 12
#meses30 = 4, 6, 9, 11
if dia != 30 and dia != 31:
    dia = dia + 1
if dia == 31 and mes == 12:
    dia = 1
    mes = 1
    anho = anho+1
if dia == 31 and mes in [1,3,5,7,8,10]:
    dia = 1
    mes = mes + 1
    anho = anho
if dia == 30 and mes in [4,6,9,11]:
    dia = 1
    mes = mes + 1
    anho = anho
elif dia == 28 or mes == 2:
    dia = 1
    mes = mes + 1
    anho = anho
if dia > 31 and mes > 12 and anho < 0:
    print("Datos incorrectos")
print("La fecha dia el dia siguiente es {}/{}/{}".format(dia,mes,anho))

#Rust
mensaje = "Fundamentos de programación"
print(type(mensaje))"""

"""a = 1
b = 20
a, b = b, a
print(a* 2 + 1)"""

n = 2020
if n%2 == 1:
    print("Impar")

"""x = 36 / 4 * (3 + 2) * 4 + 2
print(x)"""
"""uno = 5 ** 2
dos = 5 ** 3
print(uno)
print(dos)
a = 4
b = 3
if a != b:
    print(b)"""