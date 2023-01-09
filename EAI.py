"""

La entidad actualizadora de la información será la encargada de periódicamente actualizar que asientos están ocupados de que estadios
e irá gestionando la información. 

"""

import time 
from ERI import generarAsistentesERI
from Generador import eliminarAsistentes
from Conector import establecerConexion


def correrSimulacion(asistentesAGenerar, asistentesAEliminar, hilosAUsar, generarSubida, imprimirPorPantalla, trabajoConHilos, numeroDeEjecuciones):
    while numeroDeEjecuciones > 0:
        db = establecerConexion('localhost', 'root', '7821', 'tfg')
        cursor = db.cursor()

        generarAsistentesERI(asistentesAGenerar, hilosAUsar,generarSubida, imprimirPorPantalla, trabajoConHilos)

        inicioEliminacion = time.time()

        nEstadios = cursor.execute("SELECT NombreEstadio from tfg.estadio")
        estadios = cursor.fetchall()

        for estadio in estadios:
            eliminarAsistentes(estadio[0], int(asistentesAEliminar/nEstadios))

        print("\n--- Ejecucion Completada en %.4f s. Asistentes Eliminados: %i. ---" % (time.time() - inicioEliminacion, nEstadios*int(asistentesAEliminar/nEstadios)))
        numeroDeEjecuciones-=1
        #time.sleep(3)

#correrSimulacion(100,0,10,True,False,True, 10)