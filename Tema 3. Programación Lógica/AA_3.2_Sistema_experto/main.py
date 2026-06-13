from pathlib import Path
from pyswip import Prolog

PREGUNTAS = (
    ("¿Te gusta programar?", "programacion"),
    ("¿Te gustan las redes y la infraestructura?", "redes"),
    ("¿Se te da bien la lógica y resolver problemas?", "logica"),
    ("¿Te gusta la estadística y el análisis de datos?", "estadistica"),
    ("¿Te interesa la inteligencia artificial?", "inteligencia_artificial"),
    ("¿Te gusta organizar y liderar equipos?", "liderazgo"),
    ("¿Te interesan las finanzas y los negocios?", "finanzas"),
    ("¿Te gusta optimizar procesos industriales?", "optimizacion"),
    ("¿Te interesa la química y la biología?", "quimica"),
    ("¿Te importa el bienestar social y comunitario?", "trabajo_social"),
    ("¿Te interesa el marketing y el emprendimiento?", "marketing"),
)

NOMBRES_CARRERAS = {
    "sistemas_computacionales": "Sistemas Computacionales",
    "ciencia_datos": "Ciencia de Datos",
    "administracion": "Administración",
    "industrial": "Industrial",
    "alimentarias": "Alimentarias",
    "desarrollo_comunitario": "Desarrollo Comunitario",
    "gestion_empresarial": "Gestión Empresarial",
}


def preguntar(pregunta_rasgo):
    pregunta, rasgo = pregunta_rasgo

    while True:
        respuesta = input(f"{pregunta} (si/no): ").strip().lower()

        if respuesta in ("si", "sí", "s"):
            return rasgo

        if respuesta in ("no", "n"):
            return None

        print("⚠ Responde solamente 'si' o 'no'.")


es_rasgo_valido = lambda rasgo: rasgo is not None


def capturar_perfil(preguntas, callback_pregunta, callback_filtro):
    respuestas = tuple(map(callback_pregunta, preguntas))
    rasgos_validos = tuple(filter(callback_filtro, respuestas))
    rasgos_normalizados = tuple(map(lambda r: r.lower(), rasgos_validos))

    return rasgos_normalizados


formatear_carrera = lambda carrera: NOMBRES_CARRERAS.get(carrera, carrera)


def consultar_prolog(rasgos):
    prolog = Prolog()

    ruta_base = Path(__file__).parent
    ruta_prolog = ruta_base / "carreras.pl"

    prolog.consult(str(ruta_prolog))

    lista_prolog = "[" + ", ".join(rasgos) + "]"

    resultado = list(prolog.query(f"mejor_carrera({lista_prolog}, Carrera, Puntaje)"))

    if not resultado:
        return None, 0

    carrera = str(resultado[0]["Carrera"])
    puntaje = resultado[0]["Puntaje"]

    return carrera, puntaje


def mostrar_resultado(carrera, puntaje):
    print("\n" + "=" * 55)
    print(" SISTEMA EXPERTO - RESULTADO")
    print("=" * 55)
    print(f" Carrera recomendada: {formatear_carrera(carrera)}")
    print(f" Coincidencias encontradas: {puntaje}")
    print("=" * 55)


def main():
    print("\n" + "=" * 55)
    print(" SISTEMA EXPERTO - ORIENTACIÓN VOCACIONAL")
    print(" Tecnológico Felipe Carrillo Puerto")
    print("=" * 55)
    print("\nResponde las siguientes preguntas con 'si' o 'no'.\n")

    rasgos = capturar_perfil(PREGUNTAS, preguntar, es_rasgo_valido)

    if not rasgos:
        print(
            "\nNo seleccionaste ningún interés. Se recomienda acudir a orientación escolar."
        )
        return

    carrera, puntaje = consultar_prolog(rasgos)

    if carrera and puntaje > 0:
        mostrar_resultado(carrera, puntaje)
    else:
        print("\nNo se encontró una carrera relacionada con el perfil seleccionado.")


if __name__ == "__main__":
    main()
