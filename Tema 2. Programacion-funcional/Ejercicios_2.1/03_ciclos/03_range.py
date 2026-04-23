# 03_range()

from os import system
if system("clear") != 0: system("cls")

print("\n range():")

#Genera una secuencia de numeros del 0 al 9
for num in range(10):
    print(num)
    
#range(inicio, fin)
for num in range(5,10):
    print(num)
    
#range(inicio, fin, paso)
for num in range(0,1000, 5):
    print(num)
    
for num in range(-5,0):
    print(num)

for num in range(0, 10, -1):
    print(num)

for num in range(0, 444):
    print(num)
    
num = range(10)
list_of_nums = list(num)
print(list_of_nums)

#seria para hacerlo cinco veces
for _ in range(5):
    print("hacer cinco veces algo")
    


