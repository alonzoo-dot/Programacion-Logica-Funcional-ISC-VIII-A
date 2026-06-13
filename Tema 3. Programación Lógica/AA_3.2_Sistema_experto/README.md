AA 3.2 Sistema Experto - Recomendación de Carrera

Sistema experto desarrollado para recomendar una carrera ideal a estudiantes de nuevo ingreso del Tecnológico, utilizando el paradigma lógico como motor de inferencia y el paradigma funcional como controlador.
Objetivo

Desarrollar un sistema experto que integre Prolog y Python para recomendar una carrera con base en los intereses, habilidades y perfil del usuario.
Carreras incluidas

El sistema considera las siguientes carreras:

    Sistemas Computacionales
    Ciencia de Datos
    Administración
    Industrial
    Alimentarias
    Desarrollo Comunitario
    Gestión Empresarial

    Nota: La actividad menciona “6 opciones”, pero en las instrucciones se listan 7 carreras. Por ello, el sistema incluye las 7 carreras solicitadas.

Tecnologías utilizadas

    Python 3
    SWI-Prolog
    PySwip

Estructura del proyecto

AA_3.2_Sistema_experto/
├── carreras.pl
├── main.py
├── README.md
└── requirements.txt

Descripción de archivos
carreras.pl

Contiene la base de conocimientos del sistema experto. En este archivo se definen:

    Las carreras disponibles.
    Los perfiles, habilidades e intereses asociados a cada carrera.
    Las reglas de inferencia para calcular coincidencias.
    La regla principal para determinar la carrera más adecuada.

main.py

Funciona como controlador del sistema. Este archivo:

    Muestra un cuestionario interactivo.
    Captura las respuestas del usuario.
    Usa características funcionales como map, filter, lambda e inmutabilidad mediante tuplas.
    Envía el perfil del usuario a Prolog mediante PySwip.
    Recibe la carrera recomendada y muestra el resultado.

requirements.txt

Contiene la dependencia necesaria para conectar Python con SWI-Prolog.
Requisitos previos

Antes de ejecutar el sistema se debe tener instalado:

    Python 3.
    SWI-Prolog.
    PySwip.

Instalación

Clonar o descargar el repositorio y entrar a la carpeta del proyecto:

cd AA_3.2_Sistema_experto

Instalar las dependencias:

pip install -r requirements.txt

También se puede instalar PySwip directamente con:

pip install pyswip

Verificar instalación de PySwip

PySwip no se ejecuta como comando en la terminal. Para verificar que está instalado correctamente, usar:

python -c "import pyswip; print('PySwip instalado correctamente')"

Ejecución

Desde la carpeta del proyecto, ejecutar:

python main.py

El sistema mostrará un cuestionario con preguntas de respuesta si o no.
Ejemplo

¿Te gusta programar? (si/no): si
¿Te gustan las redes y la infraestructura? (si/no): si
¿Se te da bien la lógica y resolver problemas? (si/no): si

Al finalizar, el sistema mostrará la carrera recomendada:

=======================================================
 SISTEMA EXPERTO - RESULTADO
=======================================================
 Carrera recomendada: Sistemas Computacionales
 Coincidencias encontradas: 3
=======================================================

Funcionamiento general

El sistema trabaja en dos partes:
Motor lógico en Prolog

Prolog almacena la base de conocimientos y aplica reglas de inferencia para calcular qué carrera coincide mejor con los rasgos del usuario.
Controlador funcional en Python

Python realiza el cuestionario, procesa las respuestas usando funciones funcionales y consulta a Prolog para obtener la recomendación.
Características funcionales aplicadas

En el archivo main.py se aplican elementos del paradigma funcional:

    map: para procesar las preguntas del cuestionario.
    filter: para eliminar respuestas vacías o negativas.
    lambda: para definir funciones anónimas simples.
    Tuplas: para mantener estructuras de datos inmutables.

Autores

    Michael Alonzo Gonzalez
    Julian Alberto Morales Mena

Para crear ambos rápido desde PowerShell

notepad README.md
notepad requirements.txt

