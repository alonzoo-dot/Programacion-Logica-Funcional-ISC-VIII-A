#Transformar un tipo de un valor a otro
from os import system
if system("clear") !=0: system("cls")

#convertir una cadena de texto a numero
print(int("100")+2)

#convertir un entero a coadena para concatenar con otra cadena
print("100" + str(2))

#convertir un numero decimal a entero
print(type(float("3.1416")))

print(int(3.1416))# Convierte 3.1416 a 3 eliminado la parte de decimal. Resultado es un entero

#Evaluar valores numericos como booleanos
print(bool(3))#Culaquier numero distinto de 0 es True. Resultado. True
print(bool(0))
print(bool(-1))#Números negativos tambien son True. Resultado: True

#Evaluar cadenas como booleanos
print(bool(""))#Una cadena vacia es False
print(bool(" "))#Una cadena con un espacio es True
print(bool("False"))#una cadena con texto, aunque sea "false", es true

#Redondear un numero decimal
print(round(2.51))#Redondear 2.51 al entero mas cercabi



