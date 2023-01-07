"""

La entidad actualizadora de la información será la encargada de periódicamente actualizar que asientos están ocupados de que estadios
e irá gestionando la información. 

"""

import time 
from ERI import generarAsistentesERI
from Generador import eliminarAsistentes
from Conector import establecerConexion


db = establecerConexion('localhost', 'root', '7821', 'tfg')
cursor = db.cursor()

asistentesAEliminar = 0
asistentesAGenerar = 0
hilosAUsar = 0

generarAsistentesERI(asistentesAGenerar, hilosAUsar,True, False, True)

inicioEliminacion = time.time()

nEstadios = cursor.execute("SELECT NombreEstadio from tfg.estadio")
estadios = cursor.fetchall()

for estadio in estadios:
    eliminarAsistentes(estadio[0], int(asistentesAEliminar/nEstadios))

print("\n--- Ejecucion Completada en %.4f s. Asistentes Eliminados: %i. ---" % (time.time() - inicioEliminacion, nEstadios*int(asistentesAEliminar/nEstadios)))
