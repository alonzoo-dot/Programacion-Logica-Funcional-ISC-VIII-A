#python tiene varios tipos de datos
#int,float, complex, str, bool, NoneType,LIST, tuple, dict range, set.

from os import system
 
if system("clear") !=0: system("cls")

"""El comando 'type()' devuelve el tipo de un objeto en python"""

#enteros
print("init:")
print(type(10))#Numero entero positivo
print(type(0))#El numero cero tambien es un entero
print(type(-5))#numeos entero negativo
print(type(72238948239048230884923894823423490238490238))#python permite enteros de gran valor

#flotantes
print("float:")
print((type(3.14)))
print((type(1.0)))
print((type(1e3)))#notacion cientifica

#Numeros complejos
print("complex:")
print((type(1 + 2j)))


#cadena de texto: string
print("str:")
print(type("Hola"))
print(type(""))
print(type("123"))
print(type("""
           multilinea
           """))

# bool
print("bool:")
print(type(True))
print(type(False))
print(type(1 < 2))


#NoneType
print("NoneType:")
print(type(None))
