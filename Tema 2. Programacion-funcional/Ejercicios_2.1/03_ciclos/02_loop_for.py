##Bucles for
from os import system
if system("clear") != 0: system("cls")


#iteracion de una lista
frutas = ["manzana","pera","mandarina"]
for fruta in frutas:
    print(fruta)

#iterar sobre cualquier cosa que sea iterable
cadena = "estudiante"
for  caracter in cadena:
    print(caracter)
    
#enumerate()
frutas =["manzana","pera","mandarina"]
for idx, value in  enumerate(frutas):
    print(f"El indice es {idx} y la fruta es {value}")
    
#bucle anidados
letras = ["A","B","c"]
numeros = [1,2,3]

for letra in letras:
    for numero in numeros:
        print(f"{letra}{numero}")
        
#break 
print("\nbreak")
animales = ["perro","gato","raton", "loro","pez","canario"]
for idx, animal in enumerate(animales):
    print(animal)
    if animal == "loro":
        print(f"El loro esta escondido en el indice {idx}")
        break
    
#continue 
print("\ncontinue")
animales = ["perro","gato","raton", "loro","pez","canario"]
for idx, animal in  enumerate(animales):
    if animal == "loro":continue
    
    print(animal)
    

#compresion de lista (list comprehension)
animales = ["perro","gato","raton", "loro","pez","canario"]
animales_mayus = [animal.upper() for animal in animales]
print(animales_mayus)

# Muestra los números pares de una lista
pares = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]
print(pares)