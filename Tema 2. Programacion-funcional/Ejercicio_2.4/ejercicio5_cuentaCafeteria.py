# Ejercicio 4: La cuenta de la cafetería
# Objetivo: Dada una lista de precios de las ordenes de la cafetería y deberás aplicar varias funciones de orden superior (map, filter, reduce) para calcular el total a pagar.
from functools import reduce

# Lista de precios de ejemplo
orden = [28.0, 18.5, 45.25, 23.0, 30.0]

# aplicar 10 % de descuento
precios_con_descuento = list(map(lambda precio: precio * 0.90, orden))
print("Precios con descuento:", precios_con_descuento)

# Nos quedamos solo con los precios superiores a 25
bebidas_caras = list(filter(lambda precio: precio > 25, precios_con_descuento))
print("Bebidas caras (> $25):", bebidas_caras)

# umamos los precios filtrados para obtener el total
total = reduce(lambda acumulado, precio: acumulado + precio, bebidas_caras)
print(f"Total a pagar: ${total:.2f}")
