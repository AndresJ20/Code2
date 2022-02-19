#El ciclo for ejecuta un bloque de codigo repetidamente hasta 
# que la condicion en el ciclo for no sea valida

mascotas = ["gatos" , "perros" , "gatos" , "peces" , "perros" , "perros"] #Son ciclos que dan vuelta e imprimen los elementos 
# de manera vertical de la lista
for i in mascotas:
    print(i)

contador_gatos= 0
contador_perros= 0 
contador_peces= 0

"""for i in mascotas:
    if i == "gatos":
        contador_gatos = contador_gatos + 1
    elif i == "perros":
        contador_perros = contador_perros + 1
    else:
        contador_peces = contador_peces + 1"""

for i in mascotas:
    if i == "gatos":
        contador_gatos = contador_gatos + 1

for i in mascotas:
    if i == "perros":
        contador_perros = contador_perros + 1

for i in mascotas:
    if i == "peces":
        contador_peces = contador_peces + 1

print("El numero de gatos es: ", contador_gatos)
print("El numero de perros es: ", contador_perros)
print("El numero de peces es: ", contador_peces)