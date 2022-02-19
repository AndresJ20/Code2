#Solicitar al usuario la inicial del dia de la semana y mostrar el nombre del dia completo. 
#La letra inicial puede ser mayuscula o minuscula. Usa x para el miercoles 
dia = input("Digite la inicial de la semana: ")
#print(dia.lower())Mayuscula a minuscula
#print(dia.upper())Minuscula a mayuscula
if dia == "L" or dia == "l":
    print("El dia es lunes")
elif dia == "M" or dia == "m":
    print("El dia es martes")
elif dia == "X" or dia == "x":
    print("El dia es miercoles")
elif dia == "J" or dia == "j":
    print("El dia es jueves")
elif dia == "V" or dia == "v":
    print("El dia es viernes")
elif dia == "S" or dia == "s":
    print("El dia es sabado")
elif dia == "D" or dia == "d":
    print("El dia es domingo")
else:
    print("Inicial incorrecta")
