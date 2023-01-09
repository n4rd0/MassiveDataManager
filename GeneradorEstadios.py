from Conector import establecerConexion

#Con esta funcion podemos agregar los estadios que queramos modularmente a la BBDD

def generarEstadio(NombreEstadio, Ubicacion, Secciones, Grupos, Filas, Asientos):

    #Creamor el cursor con el que comunicaremos con la bbdd
    db = establecerConexion('localhost', 'root', '7821', 'tfg')
    cursor = db.cursor()

    #ejecutamos la secuencia sql para sacar los ids y encontrar el mayor
    cursor.execute("SELECT idEstadio FROM tfg.estadio")
    idEstadios = cursor.fetchall()
    maxId = -1
    for x in idEstadios:
        if int(x[0]) > maxId: maxId = int(x[0])
    maxId += 1
    Capacidad = Secciones*Grupos*Filas*Asientos
    #Insertamos el estadio en la bbdd
    sql = """INSERT INTO `estadio` (idEstadio, NombreEstadio, 
    Capacidad, Ubicacion, Secciones, Grupos, Filas, Asientos) values(%s, %s, %s, %s, %s, %s, %s, %s)"""
    cursor.execute(sql, (maxId, NombreEstadio, Capacidad, Ubicacion, Secciones, Grupos, Filas, Asientos))
    db.commit()
"""
generarEstadio("Teatro Real", "Madrid", 7,10,20,1)
generarEstadio("Cines Callao", "Madrid", 5,12,20,1)
generarEstadio("Gran Teatre del Liceu", "Barcenlona", 7,12,25,1)
generarEstadio("Teatro de Rojas", "Toledo", 4,10,18,1)
generarEstadio("Teatro Arriaga Antzokia", "Madrid", 10,12,10,1)
generarEstadio("Teatro Lope de Vega", "Sevilla", 5,15,25,1)
generarEstadio("Gran Teatro Falla", "Cadiz", 6,10,20,1)
generarEstadio("Teatro Calderon", "Valladolid", 4,10,18,1)"""
