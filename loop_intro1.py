mascotas = ["gatos" , "perros" , "peces" , "loros"]
result = len(mascotas)
m1 = mascotas[0]
m2 = mascotas[2]
print("El numero de elementos es: ", result)
print(m1)

for index, mascota in enumerate(mascotas): #index numero y posicion de la mascota
    print(index, mascota)

posicion_peces = 0
for index, mascota in enumerate(mascotas):
    if mascota == "peces":
        posicion_peces = index
print("Se encontro un pez en la posicion: ", posicion_peces)