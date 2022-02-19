#Deber Andrés Jaramillo
dia = int(input("Digite el dia: "))
mes = int(input("Digite el mes: "))
if dia >= 22 and mes == 12 or dia <= 20 and mes == 1:
    print("Capricornio")
elif dia >= 21 and mes == 1 or dia <= 19 and mes == 2:
    print("Acuario")
elif dia >= 20 and mes == 2 or dia <= 20 and mes == 3:
    print("Piscis")
elif dia >= 21 and mes == 3 or dia <= 19 and mes == 4:
    print("Aries")
elif dia >= 20 and mes == 4 or dia <= 20 and mes == 5:
    print("Tauro")
elif dia >= 21 and mes == 5 or dia <= 21 and mes == 6:
    print("Geminis")
elif dia >= 22 and mes == 6 or dia <= 21 and mes == 7:
    print("Cancer")
elif dia >= 22 and mes == 7 or dia <= 21 and mes == 8:
    print("Leo")
elif dia >= 22 and mes == 8 or dia <= 22 and mes == 9:
    print("Virgo")
elif dia >= 23 and mes == 9 or dia <= 22 and mes == 10:
    print("Libra")
elif dia >= 23 and mes == 10 or dia <= 21 and mes == 11:
    print("Escorpio")
elif dia >= 22 and mes == 11 or dia <= 21 and mes == 12:
    print("Sagitario")

"""dia = int(input("Escribe el día:"))
mes = int(input("Escribe el mes:"))
if ((mes==3) and (dia>=21)) or ((mes==4) and (dia<=20)): signo = 'aries'
signo = ("capricornio", "acuario", "piscis", "aries", "tauro", "géminis", "cáncer", "leo", "virgo", "libra", "escorpio", "sagitario") 
fechas = (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21) 
mes=mes-1 
if dia>fechas[mes]: mes=mes+1 
if mes==12: mes=0 
print ("Tu signo es: " + signo[mes])"""