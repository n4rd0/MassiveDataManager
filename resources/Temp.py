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

db = establecerConexion('localhost', 'root', '7821', 'tfg')
cursor = db.cursor()

idEstadio = 0
totalOcupadas = 0

cursor.execute("SELECT PlazaEstadio FROM tfg.asistente WHERE idEstadio = %s",idEstadio)
plazasOcupadas = cursor.fetchall()

cursor.execute("SELECT Secciones, Grupos, Filas, Asientos FROM tfg.estadio WHERE NombreEstadio = %s","Civitas Metropolitano")
infoAsientosEstadio = cursor.fetchall()

totalAsientosPorGrupo = infoAsientosEstadio[0][2]*infoAsientosEstadio[0][3]

seccion = str(infoAsientosEstadio[0][0])
grupo = str(infoAsientosEstadio[0][1])
#print(seccion,grupo)

for i in range(1,infoAsientosEstadio[0][0]+1):
    for j in range(1,infoAsientosEstadio[0][1]+1):

        seccion = str(i)
        grupo = str(j)
        if i < 10:
            seccion = "0"+str(i)
        if j < 10:
            grupo = "0"+str(j)

        for plaza in plazasOcupadas:
            if seccion+grupo in plaza[0][:4]:
                totalOcupadas+=1
        porcentajeLlenado = round(100*totalOcupadas/totalAsientosPorGrupo,1)
        totalOcupadas = 0
        print(seccion,grupo, porcentajeLlenado)



nombreEstadio = "Civitas Metropolitano"
cursor.execute("SELECT idEstadio FROM tfg.estadio WHERE nombreEstadio = %s",nombreEstadio)
idEstadio = cursor.fetchall()[0][0]
db = establecerConexion('localhost', 'root', '7821', 'tfg')
cursor = db.cursor()

cursor.execute("SELECT Secciones, Grupos, Filas, Asientos FROM tfg.estadio WHERE IdEstadio = 0")
dimensionesEstadio = cursor.fetchall()
plazasDisponibles = []

for i in range(1,dimensionesEstadio[0][0]+1):
    seccion = "0"+str(i)
    seccion = seccion[-2:]
    for j in range(1,dimensionesEstadio[0][1]+1):
        grupo = "0"+str(j)
        grupo = grupo[-2:]
        for k in range(1,dimensionesEstadio[0][2]+1):
            fila = "0"+str(k)
            fila = fila[-2:]
            for l in range(1,dimensionesEstadio[0][3]+1):
                asiento = "0"+str(l)
                asiento = asiento[-2:]
                plazasDisponibles.append(seccion+grupo+fila+asiento)

#print(plazasDisponibles)

cursor.execute("SELECT PlazaEstadio FROM tfg.asistente WHERE IdEstadio = 0")
plazasOcupadas = cursor.fetchall()

for plazaOcupada in plazasOcupadas:
    #print(plazaOcupada[0])
    plazasDisponibles.remove(plazaOcupada[0])
print(idEstadio)

porcentajeDeLlenado = 100
redTone = round(((porcentajeDeLlenado*510)/100)%256)
greenTone = 255
if porcentajeDeLlenado>=50:
    greenTone = 255 - round(((porcentajeDeLlenado*510)/100)%256)

print(redTone, greenTone)

modificarPorcentajeLleno(0)
modificarPorcentajeLleno(1)
modificarPorcentajeLleno(2)

db = establecerConexion('localhost', 'root', '7821', 'tfg')
cursor = db.cursor()

cursor.execute("SELECT NombreEstadio FROM tfg.estadio")
listaEstadios = cursor.fetchall()
print(listaEstadios)

def obtenerMetricas():
    with open("metadata\MetricasSimulacion", 'r') as f:
        for data in f.readlines():
            if data.rsplit("=")[0] == "asistentesAGenerar":
                asistentesAGenerar = int(data.rsplit("=")[1])
            elif data.rsplit("=")[0] == "asistentesAEliminar":
                asistentesAEliminar = int(data.rsplit("=")[1])
            elif data.rsplit("=")[0] == "hilosAUsar":
                hilosAUsar = int(data.rsplit("=")[1])
            elif data.rsplit("=")[0] == "trabajoConHilos":
                if data.rsplit("=")[1] == "True":
                    trabajoConHilos = True
                else:
                    trabajoConHilos = False
            elif data.rsplit("=")[0] == "numeroDeEjecuciones":
                numeroDeEjecuciones = int(data.rsplit("=")[1])
            
    return (asistentesAGenerar,asistentesAEliminar,hilosAUsar,trabajoConHilos,numeroDeEjecuciones)

def actualizarMetricas(asistentesAGenerar,asistentesAEliminar,hilosAUsar,trabajoConHilos,numeroDeEjecuciones):
    with open("metadata\MetricasSimulacion", 'w') as f:
        f.write("asistentesAGenerar="+str(asistentesAGenerar)+"\n")
        f.write("asistentesAEliminar="+str(asistentesAEliminar)+"\n")
        f.write("hilosAUsar="+str(hilosAUsar)+"\n")
        f.write("trabajoConHilos="+str(trabajoConHilos)+"\n")
        f.write("numeroDeEjecuciones="+str(numeroDeEjecuciones)+"\n")

tupla = obtenerMetricas()
actualizarMetricas(122,2,33,False,12)
tupla2 = obtenerMetricas()
print(tupla)
print(tupla2)

"""