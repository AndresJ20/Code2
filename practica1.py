
num1 = 20
num2 = 50
num3 = 100
if num1 < num2:
    num1, num2 = num2, num1

if num1 < num3:
    num1, num3 = num3 , num1

if num2 < num3:
    num2, num3 = num3 , num2

print("Mayor:", num1)
print("Medio:", num2)
print("Menor:", num3)