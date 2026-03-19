#Las variables sirven para guardar datos en memoria
#python es un lenguaje de tipado dinamico y de tipado fuerte

from os import system
if system("clear") !=0: system("cls")


my_name = "Michael"
print(my_name)

age = 21
print(age)

## Tipado dinamico: el tipo de dato se determine en tiempo de ejecución
# No es necesario declarar explicitamente el tipo de variable

name = "Michael"
print(type(name))

# Reasignar un valor nuevo a la variable
age = 22
print(age)


#concatenar
#f-string (literal de cadena de formato)
print(f"Hola {my_name}, tego {age + 5} años")

#No recomendada forma de asignar variables
name, age, city ="Michael",22,"FCP"

#snake_case
mi_nombre_de_variable = "ok"

miNombreDevariable = "no-recomendado"
MiNombreDeVariable = "no-recomendado"

mi_nombre_de_variable_123 = "0k"

MI_CONSTANTES = 3.14

# Anotaciones
is_user_logged_in: bool = True
print(is_user_logged_in)

name: str = "Michael"
print(name)
