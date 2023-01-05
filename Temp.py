from Conector import establecerConexion
from GeneradorEstadios import generarEstadio

"""
db = establecerConexion('localhost', 'root', '7821', 'tfg')
cursor = db.cursor()

cursor.execute("SELECT Secciones FROM tfg.estadio WHERE idEstadadio = '0'")

print(cursor.fetchall()[0][0])



db = establecerConexion('localhost', 'root', '7821', 'tfg')
cursor = db.cursor()

cursor.execute("SELECT idEstadio FROM tfg.estadio")
idEstadios = cursor.fetchall()
maxId = -1
for x in idEstadios:
    if int(x[0]) > maxId: maxId = int(x[0])
"""

#generarEstadio("Camp Nou", 99354, "Barcelona", 5, 57, 20, 18)

