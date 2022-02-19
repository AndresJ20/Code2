#num = 19
#result = num%2
#if(num%2 == 0):
    #print("El numero es par")
#else:
    #print("El numero es impar")
#=======================================
#if result == 0:
    #print("result:",result)
    #print(num, "Es par")

#else:
    #print("result:",result)
    #print(num, "Es impar")
# =======================================

#num = -10
#if num == 0:
    #print("El numero es cero")
#elif num > 0:
    #print("Es positivo")
#else:
    #print("Es negativo")

#num1 = int(input("Ingrese un valor: "))
#if num1 > 0:
    #num2 = int(input("Ingrese un numero:" ))
#suma = num1 + num2
#resta = num1 - num2
#producto = num1 * num2
#print("Suma:", suma)
#print("Resta: ", resta)
#print("Producto: ", producto) 

#num1 = 10
#num2 = 1
#if  num1 > num2:
    #print("El mayor es: ", num1)
    #if num1%2 == 0:
        #print("El numero es par")
    #else:
        #print("El numero es impar")    
#else:
    #print("El mayor es: ", num1)
    #print("El menor es: ", num2)

num1 = 10
num2 = 2
num3 = 30
#result1 = num1 > num2 and num1 > num3
#result2 = num2 > num1 and num2 > num3
#result3 = num3 > num1 and num3 > num2
#print(result1)
#print(result2)
#print(result3)

if num1 > num2 and num1 > num3:
    print("El mayor es: ", num1)
elif num2 > num1 and num2 > num3:
    print("El mayor es: ", num2)
else:
    print("El mayor es: ", num3)