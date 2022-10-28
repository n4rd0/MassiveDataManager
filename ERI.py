# -*- coding: utf-8 -*-

from  Generador import *
import time

inicioPrograma = time.time()

asistentes = generarAsistentes(2000)

for asistente in asistentes: 
    asistente.imprimirAsistente()

insertarAsistenteBaseDatos(asistentes)

print("--- Ejecucion Completada en %.4f s. Asistentes Generados: %i. ---" % (time.time() - inicioPrograma, len(asistentes)))

