#Deber Andrés Jaramillo
dia = int(input("Digite el dia: "))
mes = int(input("Digite el mes: "))
anho = int(input("Digite el año: "))
if mes <= 0 or mes > 12 or dia <= 0 or dia > 31 or anho <= 0:
    print("La fecha es incorrecta")
elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia > 31:
        print("Fecha correcta")
    else: 
        print("Fecha incorrecta")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia > 30:
        print("Fecha correcta")
    else:
        print("Fecha correcta")
elif mes == 2:
    if anho%4 == 0 and anho%100 != 0 or anho%400 == 0:
        if dia > 29:
            print("Fecha incorrecta")
        else:
            print("Fecha correcta")
    else:
        if dia > 28:
            print("Fecha incorrecta")
        else:
            print("Fecha correcta")  

"""dia = int(input("Introduce el dia: "))
mes = int(input("Introduce el mes: "))
anho = int(input("Introduce el año: "))

if mes <= 0 or mes > 12 or dia <= 0 or dia > 31 or anho <= 0:
    print("Fecha incorrecta")
elif mes in [4,6,9,11]:
    if dia > 30:
        print("Fecha correcta")
    else:
        print("Fecha correcta")
elif mes in [1,3,5,7,8,10,12]:
    if dia > 31:
        print("Fecha incorrecta")
    else: 
        print("Fecha correcta")
elif mes == 2:
    if anho%4 == 0 and anho%100 != 0 or anho%400 == 0:
        if dia > 29:
            print("Fecha incorrecta")
        else:
            print("Fecha correcta")
    else:
        if dia > 28:
            print("Fecha incorrecta")
        else:
            print("Fecha correcta")"""