###
# EJERCICIOS (for)
###

from os import system
if system("clear") != 0: system("cls")

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive)
print("\nEjercicio 1: Números pares del 2 al 20")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
pares = [num for num in numeros if num % 2 == 0]
print(pares)

# Ejercicio 2: Calcular la media de una lista
# Calcula la media de los números usando un bucle for
print("\nEjercicio 2: Media de una lista")
numeros = [10, 20, 30, 40, 50]
suma = 0
for numero in numeros:
    suma += numero
media = suma / len(numeros)
print(f"La media es: {media}")

# Ejercicio 3: Buscar el máximo de una lista
# Encuentra el número máximo usando un bucle for
print("\nEjercicio 3: Máximo de una lista")
numeros = [15, 5, 25, 10, 20]
maximo = numeros[0]
for numero in numeros:
    if numero > maximo:
        maximo = numero
print(f"El número máximo es: {maximo}")

# Ejercicio 4: Filtrar cadenas por longitud
# Crea una nueva lista con palabras de más de 5 letras usando for y list comprehension
print("\nEjercicio 4: Filtrar palabras por longitud")
palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]
palabras_largas = [palabra for palabra in palabras if len(palabra) > 5]
print(palabras_largas)

# Ejercicio 5: Contar palabras que empiezan con una letra
# Cuenta cuántas palabras empiezan con la letra que introduzca el usuario
print("\nEjercicio 5: Contar palabras por letra inicial")
palabras = ["cerro", "carros", "miel", "abejorro", "cantarito"]
letra = input("Introduce una letra: ")
contador = 0
for palabra in palabras:
    if palabra[0].lower() == letra.lower():
        contador += 1
print(f"Hay {contador} palabras que empiezan con '{letra}'")