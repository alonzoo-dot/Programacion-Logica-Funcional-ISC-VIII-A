#Ejercicios (while)
from os import system
if system("clear") != 0: system("cls")

# Ejercicio 1: Cuenta atrás
#Imprime los numeros del 10 al 1.
print("--- Ejercicio 1: Cuenta atrás ---")
contador = 10
while contador >= 1:
    print(contador)
    contador -= 1

# Ejercicio 2: Suma de números pares 
# Calcula la suma de los numeros pares  entre 1 y 20.

print("\n--- Ejercicio 2: Suma de pares ---")
num = 1
suma = 0
while num <= 20:
    if num % 2 == 0:
        suma += num
    num += 1
print(f"La suma de los pares es: {suma}")

# Ejercicio 3: Factorial de un número
#pide al usuario que introduzca un  numero entero positivo y calcular su factorial usando bucle while
print("\n--- Ejercicio 3: Factorial ---")
n = int(input("Introduce un número entero positivo: "))
original = n 
factorial = 1
while n > 0:
    factorial *= n
    n -= 1 

print(f"El factorial de {original} es {factorial}")

# Ejercicio 4: Validación de contraseña
#pide al usuario que introduzca una contraseña,  la contraseña debe de ser de 8 caracteres
#usando bucle while para seguir pidiendo la contraseña hasta que cumpla los requisitos
print("\n--- Ejercicio 4: Validación de contraseña ---")
password = ""
while len(password) < 8:
    password = input("Introduce una contraseña (mínimo 8 caracteres): ")
    if len(password) < 8:
        print("Contraseña demasiado corta.")
print("Contraseña válida")

# Ejercicio 5: Tabla de multiplicar
print("\nEjercicio 5: Tabla de multiplicar")
numero = int(input("Escribe un número para ver su tabla de multiplicar: "))
contador = 1
while contador <= 10:
    print(f"{numero} x {contador} = {numero * contador}")
    contador += 1

# Ejercicio 6: Números primos hasta N
print("\nEjercicio 6: Números primos hasta N")
numero = -1
while numero < 0:  # while para validar que el número sea positivo
    numero = int(input("Escribe un número entero positivo N: "))
    if numero < 0:
        print("El número debe ser positivo. Intenta otra vez")

candidato = 2
while candidato <= numero:  # while exterior — recorre cada número
    divisor = 2
    es_primo = True
    while divisor < candidato:  # while interior — busca divisores
        if candidato % divisor == 0:
            es_primo = False
            break
        divisor += 1
    if es_primo:
        print(candidato)
    candidato += 1