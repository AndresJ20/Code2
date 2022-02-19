#Calcular el mayor de cuatro numeros enteros introducidos por teclado

num1 = 15
num2 = 20
num3 = 2
num4 = 8

if num1 < num2:
    num1, num2 = num2, num1

if num1 < num3:
    num1, num3 = num3 , num1

if num1 < num4:
    num1 , num4 = num4 , num1

if num2 < num3:
    num2, num3 = num3 , num2

if num2 < num4:
    num2 , num4 = num4 , num2

if num3 < num4:
    num3, num4 = num4 , num3

print(num1)
print(num2)
print(num3)
print(num4)