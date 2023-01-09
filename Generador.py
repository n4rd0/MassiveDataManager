# -*- coding: utf-8 -*-

import random 
from  Asistente import Asistente
from Conector import establecerConexion
"""
Clase encargada de generar los datos de asistentes que compran y venden entradas para los estadios. 
"""

db = establecerConexion('localhost', 'root', '7821', 'tfg')
cursor = db.cursor()

nEstadios = cursor.execute("SELECT * FROM tfg.estadio")
cursor.execute("SELECT * FROM tfg.estadio")  
idEstadios = cursor.fetchall()
dicIdPlazasDisponibles = {}

for id in idEstadios:

    cursor.execute("SELECT Secciones, Grupos, Filas, Asientos FROM tfg.estadio WHERE IdEstadio = %s",id[0])
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

    cursor.execute("SELECT PlazaEstadio FROM tfg.asistente WHERE IdEstadio = %s",id[0])
    plazasOcupadas = cursor.fetchall()

    for plazaOcupada in plazasOcupadas:
        plazasDisponibles.remove(plazaOcupada[0])

    dicIdPlazasDisponibles[id[0]] = plazasDisponibles

l = open('metadata/Names.txt','r')
listaNombres = l.readlines()
l = open('metadata/Surnames.txt','r')
listaApellidos = l.readlines()
l = open('metadata/Alphabet.txt', 'r')
alphabet = l.readlines()
l.close()

#Eliminar asistentes del estadio por nombre
def eliminarAsistentes(nombreEstadio, numeroEliminaciones):
    
    db = establecerConexion('localhost', 'root', '7821', 'tfg')
    cursor = db.cursor()

    try:

        asistentesAEliminar = set()
        #Sacamos la id del estadio asociada al nombre
        cursor.execute("SELECT idEstadio FROM tfg.estadio WHERE NombreEstadio = %s", nombreEstadio)
        idEstadio = int(cursor.fetchone()[0])

        #Sacamos loas asistentes que se encuentran en ese estadio
        cursor.execute("SELECT * FROM tfg.asistente WHERE idEstadio = %s", idEstadio)
        asistentes = cursor.fetchall()

        #Si hay mas asistentes que los que queremos eliminar, los eliminamos, si no, vaciamos el estadio directamente
        if len(asistentes) > numeroEliminaciones:

            while(len(asistentesAEliminar) != numeroEliminaciones): asistentesAEliminar.add(random.randint(0, len(asistentes)-1)) 
            
            for numeroDeAsistente in asistentesAEliminar:
                idAsistente = asistentes[numeroDeAsistente][0]
                cursor.execute("DELETE FROM tfg.asistente WHERE idAsistente = %s", idAsistente)
                db.commit()

        else:
            cursor.execute("DELETE FROM tfg.asistente WHERE idEstadio = %s", idEstadio)
            db.commit()
            print("No puedes eliminar mas asistentes de los que hay, se han eliminado a todos.")
        
        modificarPorcentajeLleno(idEstadio)

    except:
        print("El nombre introducido para el estadio es incorrecto.")

    cursor.close()
    return

#Genera el numero indicado de asistentes
def generarAsistentes(numeroGeneraciones):


    #Accedemos a distitnas bases de datos de nombres y apellidos para posterior
    #mente generar aleatoriamente los datos
    
    listaAsistentesGenerada = []

    for i in range(numeroGeneraciones):

        #Generamos al azar en cual de todos los estadios nuestro asistente 
        #ficticio estara alojandose
        idEstadio = random.randint(0, nEstadios-1)

        if len(dicIdPlazasDisponibles[idEstadio])>0:
        
            #Cogemos un nombre y apellido al azar de las listas proporcionadas
            nombre = listaNombres[random.randint(0,len(listaNombres)-1)]
            apellido = listaApellidos[random.randint(0,len(listaApellidos)-1)]
            
            #La edad tambien se genera al azar entre 6 y 99
            edad = random.randint(6,99)
            
            #Para el DNI cogemos un numero al azar y calculamos el modulo para 
            #Asignarle una letra
            DNI = random.randint(0,99999999)
            DNI = str(DNI) + alphabet[DNI%len(alphabet)]
            
            #La plaza depende del estadio elegido obteniendola igual de forma
            #aleatoria

            plazaEstadio = dicIdPlazasDisponibles[idEstadio][random.randint(0,len(dicIdPlazasDisponibles[idEstadio])-1)]
            dicIdPlazasDisponibles[idEstadio].remove(plazaEstadio)

            #Obtenemos todos los estadios almacenados en la bbdd
            
            asist = Asistente(idEstadio, nombre.strip(), apellido.strip(), edad, DNI.strip(), plazaEstadio)
            listaAsistentesGenerada.append(asist)
    
    return listaAsistentesGenerada 

#Actualzia en la bbdd el porcentaje de llenado del estadio
def modificarPorcentajeLleno(idEstadio):

    db = establecerConexion('localhost', 'root', '7821', 'tfg')
    cursor = db.cursor()

    #Sacamos el total de asientos ocupados en el estadio
    asientosOcupados = cursor.execute("SELECT * FROM tfg.asistente WHERE idEstadio = %s", idEstadio)
    cursor.execute("SELECT Secciones, Grupos, Filas, Asientos FROM tfg.estadio WHERE idEstadio = %s", idEstadio)

    #Sacamos la capacidad del estadio
    datos = cursor.fetchall()
    capacidad = datos[0][0]*datos[0][1]*datos[0][2]*datos[0][3]

    #Calculamos el porcentaje
    porcentajeLLeno = round(asientosOcupados*100/capacidad,4)

    #Ejecutamos la actualizacion del porcentaje en la bbdd
    cursor.execute("UPDATE tfg.estadio SET PorcentajeLLeno = %s WHERE idEstadio = %s",(porcentajeLLeno, idEstadio))
    db.commit()

#Insertamos los datos de la lista en la BBDD
def insertarAsistenteBaseDatos(listaAsistentes):
    
    db = establecerConexion('localhost', 'root', '7821', 'tfg')
    cursor = db.cursor()
    
    for asistente in listaAsistentes:
        sql = """INSERT INTO `asistente` (idEstadio, Nombre, 
        Apellido, Edad, DNI, PlazaEstadio) values(%s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (asistente.idEstadio, asistente.nombre, asistente.apellido, asistente.edad, asistente.DNI, asistente.plazaEstadio))
        db.commit()
    cursor.execute("SELECT idEstadio FROM tfg.estadio")
    ids = cursor.fetchall()
    for id in ids: 
        modificarPorcentajeLleno(id[0])
    
    cursor.close()
    return 
