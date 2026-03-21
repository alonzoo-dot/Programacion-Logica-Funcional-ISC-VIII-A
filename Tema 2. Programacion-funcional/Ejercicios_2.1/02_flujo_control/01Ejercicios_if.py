from os import system
if system("clear") != 0: system("cls")


# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

print("Ejercicio 1: Determinar el mayor de dos números\n")

num1 = int(input("Inserte el primer numero: "))
num2 = int(input("Inserte el segundo numero: "))

if num1 > num2:
    print(f"El primer numero es mayor :{num1} ")
elif num2 > num1:
    print(f"El segundo numero es mayor: {num2}")
else:
    print("Ambos numeros son iguales")
print("-----------------------------------------------\n")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)
print("Ejercicio 2: Calculadora simple\n")

nume1 = float(input("Inserte el primer numero: "))
nume2 = float(input("Inserte el segundo numero: "))
operación = input("Inserte la operacion que quiere realizar (+, -, *, /): ")

if operación == "+":
    print(f"El resultado de la suma es: {round(nume1 + nume2, 2)}")
    
elif operación == "-":
    print(f"El resultado de la resta es: {round(nume1 - nume2, 2)}")
    
elif operación == "*":
    print(f"El resultado de la operacion es: {round(nume1* nume2, 2)}")
    
elif operación == "/":
    if nume2 != 0:
        print(f"El resultado de la division es: {round(nume1 / nume2, 2)}")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Operacion  invalida")
print("-----------------------------------------------\n")   
      
# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero
print("Ejercicio 3: Año bisiesto\n")

año = int(input("Inserte un año: "))
if año %    400 == 0:
    print("Es bisiesto")
elif año % 100 == 0:
    print("No es bisiesto")
elif año % 4 == 0:
    print("Es bisiesto")
else:
    print("No es bisiesto")
    
print("-----------------------------------------------\n") 
    
# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

print("Ejercicio 4: Categorizar edades\n")

edad = int(input("Inserte su edad: "))

if edad < 0:
    print("Edad no válida")
elif edad <= 2:
    print("Eres un bebé")
elif edad <= 12:
    print("Eres un niño")
elif edad <= 17:
    print("Eres un adolescente")
elif edad <= 64:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")