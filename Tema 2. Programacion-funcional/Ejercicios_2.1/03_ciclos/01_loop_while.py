# buclw while

from os import system
if system("clear") != 0: system("cls")

print("\n Bucle while:")

#bucle con una simple condiccion 
contador = 0
while contador <= 5:
    print(contador)
    contador += 1  # es super importancia
 
#utiliza palabra break para romper el bucle    
print("\n Bucle while con break:")
contador = 0

while True:
    print(contador)
    contador += 1
    if contador == 5:
        break
    
#continue, que lo hace es saltar esta iteracion en concreto y continuar el bucle
print("\n Bucle con continue")
while contador < 10:
    contador += 1
    
    if contador % 2 == 0:
        continue
    print(contador)

#else, esta condiccion cuando se ejeccuta?
print("\n Bucle while con else:")
contador = 0
while contador <5:
    print(contador)
    contador += 1
else:
    print("El bucle ha terminado")

#pedirle al usuario un numero que tiene ser positivo si no, no le dejamos en paz
numero = -1
while numero <0:
    numero = int(input("Escribe un numero positivo: "))
    if numero <0:
        print("el numero debe ser  positivo. Intenta otra vez")
        
print(f"El numero que has introducido es {numero}")

numero = -1
while numero < 0:
    try:
        numero = int(input("Escribe un numero positivo: "))
    except:
        print("lo que intruduces debe de ser numero!")
print(f"El numero que has introduccion es {numero}")    
        
