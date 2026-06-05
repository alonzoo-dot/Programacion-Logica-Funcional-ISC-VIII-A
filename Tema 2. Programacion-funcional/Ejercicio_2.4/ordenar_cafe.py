# Ejercicio 1: ordenar cafe para el grupo ISC.
"""
1. crear una funcion que no tome ningun argumento y devuelve la cadena de texto cafe.
para simular la preparacion de una taza de cafe.

2. crear funcion para tomar la orden del cafe que toma un argumento  numero_tazas que indica cuantas tazas de cafe se desean.
    dentro de la funcion
    --Almacena los resultados
    --Utiliza una lista por compresion para llamar a la funcion preparar_cafe segun el numero_tazas
    proporcionado. Ir archivo compresionLista.py.
    --Finalmente devuelve la lista tazas_cafe
3. Crear una nueva variable cafe_para_grupo que recibe el resultado de llamar a la funcion ordenar_cafe con el numero de tazas deseado.
4. Imprime el resultado de cafe_para_grupo.
"""


def preparar_cafe_():
    return "cafe"


def ordenar_cafe(numero_tazas):
    tazas_cafe = [preparar_cafe_() for _ in range(numero_tazas)]
    return tazas_cafe


cafe_para_grupo = ordenar_cafe(10)

print(cafe_para_grupo)
