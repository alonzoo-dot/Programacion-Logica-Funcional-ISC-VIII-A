## 01-print
#el modulo de print() es el  modulo que nos permite imprimir en consola
from os import system
 
if system("clear") !=0: system("cls")
 
print("¡Hola, crayola!")
 
print('Esto tambien funciona con una comilla')
 
 #puedes imprimir multiples elementos separados por un espacio
print("python","es","genial")
 
 #El parametro 'end' define lo que se imprime al final de la linea
print("python","es","brutal", sep = "-")
 
print("Esto se imprime", end ="\n")
print("en una linea")
 
print(42)
 
 
 #solucion 1: Usa comillas simples para encerrar la cadena
print('Esto es una "pulgada" dentro de un string con comillas simples')
 
 # solucion 2: usando comillas dobles
print("Esto es una \"pulgada\"dentro de un string con comillas dobles")
#solucion 3: usando comillas triples
print("""Esto es una "pulgada" dentro de un string con triple comiillas""")