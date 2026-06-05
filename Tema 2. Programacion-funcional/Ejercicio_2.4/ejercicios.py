# Ejercicio 3: Inflar globos
# Objetivo: Crea un programa que simule la inflada de globos 🎈 para una fiesta, de acuerdo al número de invitados que asistirán.
"""
1.- Define una función llamada inflar_globo que no reciba parámetros
    y devuelva el emoji de globo "🎈".
2.- Crea esta misma función usando lambda y asigna el resultado a la variable inflar_globo_lambda.
3.- crea una lista de globos usando la función lambda y una comprensión de listas, para el número de invitados que se ingresen por el usuario.
2.- Define una función llamada preparar_globos que reciba un argumento
    numero_invitados (entero).
    Dentro de la función:
    -- Usa una comprensión de listas para llamar a inflar_globo()
       tantas veces como indique numero_invitados.
    -- Devuelve esa lista.
3.- Llama a preparar_globos solicitando al usuario ingresar el número
    de invitados a la fiesta y almacena el resultado en una variable globos_fiesta.
4.- Muestra en pantalla el contenido de globos_fiesta,
    que será una lista con varios emojis "🎈".
Ejemplo de salida:
    ¿Cuántos invitados van a la fiesta? 3
    ['🎈', '🎈', '🎈']
"""


# 1. Función que devuelve un globo
def inflar_globo():
    return "🎈"


# 2. Crear la misma función usando lambda y asigna el resultado a la variable inflar_globo_lambda.
inflar_globo_lambda = lambda: "🎈"  # función anónima

# 3. Lista de globos usando la lambda y comprensión de listas
num_invitados = int(input("¿Cuántos invitados van a la fiesta? "))
globos_lambda = [inflar_globo_lambda() for _ in range(num_invitados)]


# 4. Función para prepara globos con la función normal
def preparar_globos(numero_invitados):
    globos = [inflar_globo() for _ in range(numero_invitados)]
    return globos


globos_fiesta = preparar_globos(num_invitados)

# 5. Mostrar el resultado pedido
print(globos_fiesta)

print("\n")

# Ejercicio 4: Mostrar el menú de la cafetería
# Objetivo: Usar comprensión de listas para formatear y mostrar el menú de una cafetería con los precios de cada bebida.

"""
1.- Crea una función llamada ver_menu que reciba un diccionario llamado menu.
2.- Dentro de la función, usa comprensión de listas para recorrer menu.items().
    Cada elemento del diccionario tiene dos partes: la clave (nombre de la bebida) y el valor (precio).
    Estructura: for nombre, precio in menu.items()
3.- Para cada par clave-valor, genera una cadena con el formato: "Americano: $25.50"
Es decir: f"{nombre.capitalize()}: ${precio:.2f}"
4.- La función debe devolver la lista generada por la comprensión.
5.- Crea la variable menu con el diccionario de precios mostrado arriba.
6.- Llama a ver_menu con el diccionario menu y guarda el resultado en una variable llamada menu_formateado.
7.- Imprime cada elemento de menu_formateado en una línea separada usando un ciclo for.
Salida esperada (los precios pueden variar según el diccionario):
    Americano: $25.50
    Café de olla: $22.00
    Capuchino: $35.75
    Coca: $40.00
    Agua: $18.50
"""


def ver_menu(menu):
    """Devuelve una lista formateada con nombre y precio."""
    return [f"{nombre.capitalize()}: ${precio:.2f}" for nombre, precio in menu.items()]


menu = {
    "americano": 25.50,
    "café de olla": 22.00,
    "capuchino": 35.75,
    "coca": 40.00,
    "agua": 18.50,
}

menu_formateado = ver_menu(menu)

for linea in menu_formateado:
    print(linea)

print("\n")

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
