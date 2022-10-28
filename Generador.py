# -*- coding: utf-8 -*-

import random 
from  Asistente import Asistente
from Conector import establecerConexion
"""

Clase encargada de generar los datos de asistentes que compran y venden entradas para los estadios. 

Asistente(self, idEstadio , nombre, apellido, edad, DNI, plazaEstadio)

"""

#conexion a la bbdd 
db = establecerConexion('localhost', 'root', '7821', 'tfg')
cursor = db.cursor()

def generarAsistentes(numeroGeneraciones):
    
    #Accedemos a distitnas bases de datos de nombres y apellidos para posterior
    #mente generar aleatoriamente los datos
    
    listaAsistentesGenerada = []
    l = open('Names.txt','r')
    listaNombres = l.readlines()
    l = open('Surnames.txt','r')
    listaApellidos = l.readlines()
    l = open('Alphabet.txt', 'r')
    alphabet = l.readlines()
    l.close()

    for i in range(numeroGeneraciones):
        
        #Obtenemos todos los estadios almacenados en la bbdd
        cursor.execute("SELECT * FROM estadio")
        #Generamos al azar en cual de todos los estadios nuestro asistente 
        #ficticio estara alojandose
        idEstadio = random.randint(0, cursor.execute("SELECT * FROM estadio")-1)
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
        cursor.execute("SELECT Secciones FROM tfg.estadio WHERE idEstadadio = '%s'",idEstadio)
        seccion = random.randint(0, cursor.fetchall()[0][0])
            
        if seccion < 10 :
            seccion = "0" + str(seccion)
        seccion = str(seccion)
                
        cursor.execute("SELECT Grupos FROM tfg.estadio WHERE idEstadadio = '%s'",idEstadio)
        grupo = random.randint(0, cursor.fetchall()[0][0])
        
        if grupo < 10 :
            grupo = "0" + str(grupo)
        grupo = str(grupo)
        
        cursor.execute("SELECT Filas FROM tfg.estadio WHERE idEstadadio = '%s'",idEstadio)
        fila = random.randint(0, cursor.fetchall()[0][0])
        
        if fila < 10 :
            fila = "0" + str(fila)
        fila = str(fila)
        
        cursor.execute("SELECT Asientos FROM tfg.estadio WHERE idEstadadio = '%s'",idEstadio)
        asiento = random.randint(0, cursor.fetchall()[0][0])
        
        if asiento < 10 :
            asiento = "0" + str(asiento)
        asiento = str(asiento)
        
        asist = Asistente(idEstadio, nombre.strip(), apellido.strip(), edad, DNI.strip(), seccion+grupo+fila+asiento)
        listaAsistentesGenerada.append(asist)
    
    return listaAsistentesGenerada 

#Insertamos los datos de la lista en la BBDD
def insertarAsistenteBaseDatos(listaAsistentes):
    
    for asistente in listaAsistentes:
        sql = """INSERT INTO `asistente` (idEstadio, Nombre, 
        Apellido, Edad, DNI, PlazaEstadio) values(%s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql, (asistente.idEstadio, asistente.nombre, asistente.apellido, asistente.edad, asistente.DNI, asistente.plazaEstadio))
        db.commit()
    return print("--- Todos los asistentes han sido actualizados correctamente ---")

#Por el momento vamos a trabajar solo con un estadio (El metropolitano) con 
#secciones, grupos, filas y asientos cuadrados, es decir, que todas las secciones
#son iguales con el mismo numero de grupos filas y asientos