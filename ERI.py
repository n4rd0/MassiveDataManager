# -*- coding: utf-8 -*-

from  Generador import *
import time
import threading
from GeneradorHilos import * 

inicioPrograma = time.time()

def generarAsistentesERI(numeroDeAsistentes, numeroDeHilos, generarSubida, imprimirPorPantalla, trabajoConHilos):
    if trabajoConHilos:
        t = []
        
        for _ in range(numeroDeHilos):
            th = threading.Thread(target = generarAsistentesHilo, args = (numeroDeAsistentes, generarSubida, imprimirPorPantalla, ))
            th.start()
            t.append(th)
            
        for thread in t:
            thread.join()
        
        print("\n--- Ejecucion Completada en %.4f s. Asistentes Generados: %i. ---" % (time.time() - inicioPrograma, numeroDeHilos*numeroDeAsistentes))

    else:
        asistentes = generarAsistentes(numeroDeAsistentes)
        if imprimirPorPantalla:
            for asistente in asistentes: 
                print(asistente)
        if generarSubida:
            insertarAsistenteBaseDatos(asistentes)
        print("\n--- Ejecucion Completada en %.4f s. Asistentes Generados: %i. ---" % (time.time() - inicioPrograma, numeroDeAsistentes))
