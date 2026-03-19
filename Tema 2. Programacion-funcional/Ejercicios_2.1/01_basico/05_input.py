# input(), permite la entrada de datos
from os import system
if system("clear") !=0: system("cls")

# Para obtener datos del usuario se usa la funcion input()
nombre = input("Hola, ¿como te llamas?:\n")
print(f"Hola {nombre}, encantado de conocerte")

age = input("¿cuantos años tienes\n")
age = int(age)
print(f"Tienes {age} años")


# La funcion input() tambien puede devolver multiples valores
# Para hacerlo, el usario debe separar los valores con una coma
print("Obtener multiples valores a las vez")
country, city = input(f"¿En que pais vives y ciudad vives:\n").split()#.split() "separa"
print(f"Vives en {country},{city}")