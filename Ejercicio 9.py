#diaadiaa la fecha diae hoy calcular la fecha diael dia siguiente suponer que el año no es bisiesto
#diaeber Andiarés Jaramillo
"""dia=int(input("Introdiauce el dia: "))
mes=int(input("Introdiauce el mes: "))
anho=int(input("Introdiauce el año: "))
if dia andia mes andia anho:
    dia = dia + 1
    mes = mes
    anho = anho
if mes in [1, 3, 5, 7, 8, 10, 12]:
    if dia ==31 andia mes ==12:
        dia = 1
        mes = 1
        anho = anho + 1
if dia == 31 and dia not mes == 12:
        dia= 1
        mes= mes + 1
if mes in [4, 6, 9 ,11] andia dia <= 30:
    if dia == 30:
        dia = 1
        mes = mes + 1
    else:
        dia = dia + 1
if mes == 2 andia dia<= 28:
    if dia == 28:
        dia = 1
        mes = mes +1
print("La fecha diael dia siguiente es {}/{}/{}".format(dia,mes,anho))"""

"""dia = 29
mes = 2
anho = 2022
print(dia,mes,anho)

#1, 3, 5, 7, 8, 10, 12
#4, 6, 9, 11
#2 28-29

#if mes in (1, 3, 5, 7, 8, 10, 12):
    #pass

ultimo_dia = 28
if (anho%4 == 0 and anho%100 != 0) or (anho%400 == 0):
    ultimo_dia = 29
if mes == 1 or mes == 3 or mes == 5 or mes == 8 or mes == 10 or mes == 12:
    if dia == 31:
        dia = 1
        if mes != 12:
            mes += 1
        elif mes == 12:
            anho += 1
            mes = 1
    else:
        dia +=1
if  mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia == 30: 
        dia = 1
        mes += 1
    else:
        dia += 1
elif mes == 2:
    if dia == ultimo_dia:
        dia = 1
        mes += 1
    else:
        dia += 1

print(dia,mes,anho)"""

dia = 30
mes = 11
anho = 2022
print(dia,mes,anho)

ultimo_dia = 30
if mes == 2:
    if (anho%4 == 0 and anho%100 != 0) or (anho%400 == 0):
        ultimo_dia = 29
    else:
        ultimo_dia = 28
elif mes in (1,3,5,7,8,10,12):
    ultimo_dia = 31
if dia == ultimo_dia:
    dia = 1
    if mes == 12:
        dia = 1
        mes = 1
        anho += 1
    else:
        mes += 1
else:
    dia += 1

print(dia,mes,anho)