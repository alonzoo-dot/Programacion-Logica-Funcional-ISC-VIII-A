% Base de conocimientos: carreras disponibles

carrera(sistemas_computacionales).
carrera(ciencia_datos).
carrera(administracion).
carrera(industrial).
carrera(alimentarias).
carrera(desarrollo_comunitario).
carrera(gestion_empresarial).

% Perfiles de cada carrera

perfil(sistemas_computacionales,
    [logica, programacion, matematicas, resolucion_problemas, tecnologia, redes]).

perfil(ciencia_datos,
    [estadistica, matematicas, programacion, analisis, investigacion, inteligencia_artificial]).

perfil(administracion,
    [organizacion, liderazgo, comunicacion, finanzas, toma_decisiones, negocios]).

perfil(industrial,
    [procesos, optimizacion, fisica, matematicas, gestion_produccion, logistica, calidad]).

perfil(alimentarias,
    [quimica, biologia, investigacion, procesos, salud, inocuidad, laboratorio]).

perfil(desarrollo_comunitario,
    [trabajo_social, comunicacion, liderazgo, empatia, gestion_proyectos, responsabilidad_social]).

perfil(gestion_empresarial,
    [negocios, finanzas, liderazgo, comunicacion, emprendimiento, marketing]).

% Regla para calcular coincidencias entre el perfil del usuario y una carrera

puntaje(Carrera, RasgosUsuario, Puntos) :-
    perfil(Carrera, RasgosCarrera),
    intersection(RasgosUsuario, RasgosCarrera, Coincidencias),
    length(Coincidencias, Puntos).

% Regla principal: obtiene la carrera con mayor puntaje

mejor_carrera(RasgosUsuario, MejorCarrera, MejorPuntaje) :-
    findall(Puntos-Carrera,
        (
            carrera(Carrera),
            puntaje(Carrera, RasgosUsuario, Puntos)
        ),
        Resultados),
    keysort(Resultados, Ordenados),
    reverse(Ordenados, [MejorPuntaje-MejorCarrera | _]),
    MejorPuntaje > 0.