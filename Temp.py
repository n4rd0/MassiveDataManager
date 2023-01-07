from Conector import establecerConexion
from GeneradorEstadios import generarEstadio
from Generador import eliminarAsistentes
import time 
from ERI import generarAsistentesERI
from Generador import eliminarAsistentes, modificarPorcentajeLleno
from Conector import establecerConexion
db = establecerConexion('localhost', 'root', '7821', 'tfg')
cursor = db.cursor()

"""
cursor.execute("SELECT Secciones FROM tfg.estadio WHERE idEstadadio = '0'")

print(cursor.fetchall()[0][0])



db = establecerConexion('localhost', 'root', '7821', 'tfg')
cursor = db.cursor()

cursor.execute("SELECT idEstadio FROM tfg.estadio")
idEstadios = cursor.fetchall()
maxId = -1
for x in idEstadios:
    if int(x[0]) > maxId: maxId = int(x[0])

generarEstadio("Camp Nou", 99354, "Barcelona", 5, 57, 20, 18)

eliminarAsistentes("Camp Nou", 200)

cursor.execute("SELECT idEstadio, PlazaEstadio FROM tfg.asistente")
asientos = cursor.fetchall()
print(asientos)
print((0, '04111811') in asientos)

nEstadios = cursor.execute("SELECT NombreEstadio from tfg.estadio")
estadios = cursor.fetchall()

print(nEstadios)
for estadio in estadios:
    print(estadio[0])
generarAsistentesERI(8000, 10, True, False, True)
modificarPorcentajeLleno(1)

cursor.execute("SELECT idEstadio FROM tfg.estadio")
ids = cursor.fetchall()
for id in ids: 
    print(id[0])


"""


modificarPorcentajeLleno(0)
modificarPorcentajeLleno(1)
modificarPorcentajeLleno(2)
