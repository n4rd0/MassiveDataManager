"""

Desde esta ventana manejaremos la interfaz grafica de la aplicacion

"""

from tkinter import *  
from PIL import ImageTk, Image
from Conector import establecerConexion

pantallaDeInicio = Tk()
pantallaDeInicio.title("Massive Data Manager")
pantallaDeInicio.geometry("900x450")
pantallaDeInicio.resizable(False, False)

#Funciones

#Devuelve los estadios en la bbdd
def obtenerListaDeEstadios():

    db = establecerConexion('localhost', 'root', '7821', 'tfg')
    cursor = db.cursor()

    cursor.execute("SELECT NombreEstadio FROM tfg.estadio")
    listaEstadios = cursor.fetchall()
    return listaEstadios

#Volver a la ventana principal

def abrirVentanaPrincipal(ventanaActual):

    ventanaActual.destroy()
    pantallaDeInicio = Tk()
    pantallaDeInicio.title("Massive Data Manager")
    pantallaDeInicio.geometry("900x450")
    pantallaDeInicio.resizable(False, False)
    #Visualizacion - Pantalla Principal 

    tituloPantallaPrincipal = Label(pantallaDeInicio, text="Bienvenido, selecciona una de las siguientes opciones.", font=("InputMonoCondensed","20"))

    marcoContenedorOpcionesPantallaPrincipal = LabelFrame(pantallaDeInicio)

    textoVisualizacionDeEstadiosEnTiempoReal = Label(marcoContenedorOpcionesPantallaPrincipal, text="- Visualizacion de Estadios en Tiempo Real.", font=("InputMonoCondensed  18"))
    botonVisualizacionDeEstadiosEnTiempoReal = Button(marcoContenedorOpcionesPantallaPrincipal, width=6, height=1, 
        text="Acceso", font="InputMonoCondensed 12", command= lambda: abrirVisualizacionDeEstadiosEnTiempoReal(pantallaDeInicio))

    textoMetricasDeEstadiosEnTiempoReal = Label(marcoContenedorOpcionesPantallaPrincipal, compound= LEFT, text="- Metricas de Estadios en Tiempo Real.", font=("InputMonoCondensed  18"))
    botonMetricasDeEstadiosEnTiempoReal = Button(marcoContenedorOpcionesPantallaPrincipal, compound= LEFT, width=6, height=1, 
        text="Acceso", font="InputMonoCondensed 12", command= lambda:print("test"))

    textoConsultarEstadios = Label(marcoContenedorOpcionesPantallaPrincipal, text="- Consultar Estadios.", font=("InputMonoCondensed  18"))
    botonConsultarEstadios = Button(marcoContenedorOpcionesPantallaPrincipal, width=6, height=1, 
        text="Acceso", font="InputMonoCondensed 12", command= lambda:print("test"))

    textoConsultarAsistentes = Label(marcoContenedorOpcionesPantallaPrincipal, text="- Consultar Asistentes.", font=("InputMonoCondensed  18"))
    botonConsultarAsistentes = Button(marcoContenedorOpcionesPantallaPrincipal, width=6, height=1, 
        text="Acceso", font="InputMonoCondensed 12", command= lambda:print("test"))


    textoCrearEstadio = Label(marcoContenedorOpcionesPantallaPrincipal, text="- Crear Nuevos Estadios.", font=("InputMonoCondensed  18"))
    botonCrearEstadio = Button(marcoContenedorOpcionesPantallaPrincipal, width=6, height=1, 
        text="Acceso", font="InputMonoCondensed 12", command= lambda:print("test"))

    textoAjustesMetricasSimulacion = Label(marcoContenedorOpcionesPantallaPrincipal, text="- Ajustes Metricas Simulacion.", font=("InputMonoCondensed  18"))
    botonAjustesMetricasSimulacion = Button(marcoContenedorOpcionesPantallaPrincipal, width=6, height=1, 
        text="Acceso", font="InputMonoCondensed 12", command= lambda:print("test"))

    #Grid - Pantalla Principal

    tituloPantallaPrincipal.grid(row=0, column=0,pady=10, padx=40)

    marcoContenedorOpcionesPantallaPrincipal.grid(row=1, column=0, pady=10, padx=40)

    textoVisualizacionDeEstadiosEnTiempoReal.grid(row=2, column=0, pady=10, padx = 18)
    botonVisualizacionDeEstadiosEnTiempoReal.grid(row=2,column=1, padx=48, pady=10)

    textoMetricasDeEstadiosEnTiempoReal.grid(row=3, column=0, sticky= "w", padx= 18, pady=10)
    botonMetricasDeEstadiosEnTiempoReal.grid(row=3,column=1, padx=48, pady=10)

    textoConsultarEstadios.grid(row=4, column=0, sticky= "w", padx= 18, pady=10)
    botonConsultarEstadios.grid(row=4,column=1, padx=48, pady=10)

    textoConsultarAsistentes.grid(row=5, column=0, sticky= "w", padx= 18, pady=10)
    botonConsultarAsistentes.grid(row=5,column=1, padx=48, pady=10)

    textoCrearEstadio.grid(row=6, column=0, sticky= "w", padx= 18, pady=10)
    botonCrearEstadio.grid(row=6,column=1, padx=48, pady=10)

    textoAjustesMetricasSimulacion.grid(row=7, column=0, sticky= "w", padx= 18, pady=10)
    botonAjustesMetricasSimulacion.grid(row=7,column=1, padx=48, pady=10)
    
    pantallaDeInicio.mainloop()

#Cambia la ventana a la visualiacion de estadios en tiempo real
def abrirVisualizacionDeEstadiosEnTiempoReal(ventanaActual):

    #Eliminamos la ventana principal
    ventanaActual.destroy()

    #Configuracion de la ventana de visualizacion de estadios en tiempo real
    visualizacionDeEstadiosEnTiempoReal = Tk()
    visualizacionDeEstadiosEnTiempoReal.title("Visualizacion de Estadios en Tiempo Real")
    visualizacionDeEstadiosEnTiempoReal.geometry("1080x720")
    visualizacionDeEstadiosEnTiempoReal.resizable(False, False)

    estadios = obtenerListaDeEstadios()

    #Visualizacion - Pantalla Visualizacion de Estadios en Tiempo Real
    
    tituloPantallaDeVisualizacionDeEstadiosEnTiempoReal = Label(visualizacionDeEstadiosEnTiempoReal, 
    text="Bienvenido, selecciona un Estadio:", font=("InputMonoCondensed","10"))
    botonRegresoPantallaPrincipal = Button(visualizacionDeEstadiosEnTiempoReal, width=6, height=1,text="Home", 
    font="InputMonoCondensed 12", command= lambda: abrirVentanaPrincipal(visualizacionDeEstadiosEnTiempoReal))

    frameCajaEstadio = LabelFrame(visualizacionDeEstadiosEnTiempoReal)
    textoEstadio = Text(frameCajaEstadio, width=90, height=35)
    
    def dibujarEstadio():
        
        for i in range(6):
            for j in range(40):
                textTemp = Text(bg="green", width= 6,height=3, font="InputMonoCondensed 10")
                textTemp.insert(END,"s:"+str(i)+"\ng:"+str(j)+"\np:"+"11.1")
                textoEstadio.window_create(END,window=textTemp)
            textoEstadio.insert(END,"\n")
            textoEstadio.insert(END,"\n")
        return
    


    frameCajaScrollConEstadios = LabelFrame(visualizacionDeEstadiosEnTiempoReal)
    texto = Text(frameCajaScrollConEstadios, width=28, height=35)
    cajaScrolleableConEstadios = Scrollbar(frameCajaScrollConEstadios, command=texto.yview)
    texto.configure(yscrollcommand=cajaScrolleableConEstadios.set)

    for estadio in estadios:
        botonTemp = Button(text=estadio[0], width=30, height=1, font="InputMonoCondensed 10", command= lambda:print("hello"))
        texto.window_create(END, window=botonTemp)
        texto.insert(END,"\n")

    texto.configure(state=DISABLED)

    #Grid - Pantalla Visualizacion de Estadios en Tiempo Real

    tituloPantallaDeVisualizacionDeEstadiosEnTiempoReal.grid(row=0,column=0, pady=10, sticky="w", padx=15)
    botonRegresoPantallaPrincipal.grid(row=0,column=1, pady=10, padx=10, sticky="e")

    frameCajaScrollConEstadios.grid(row = 1, column=0, pady=10, padx=15)
    texto.pack(side=LEFT, pady=10, padx = 10)
    cajaScrolleableConEstadios.pack(side=RIGHT, fill=Y, pady=10,padx=10)

    frameCajaEstadio.grid(row = 1, column=1, pady=10,padx=10, sticky="w")
    textoEstadio.grid(row=0, column=0)

    visualizacionDeEstadiosEnTiempoReal.mainloop()

#Visualizacion - Pantalla Principal 

tituloPantallaPrincipal = Label(pantallaDeInicio, text="Bienvenido, selecciona una de las siguientes opciones.", font=("InputMonoCondensed","20"))

marcoContenedorOpcionesPantallaPrincipal = LabelFrame(pantallaDeInicio)

textoVisualizacionDeEstadiosEnTiempoReal = Label(marcoContenedorOpcionesPantallaPrincipal, text="- Visualizacion de Estadios en Tiempo Real.", font=("InputMonoCondensed  18"))
botonVisualizacionDeEstadiosEnTiempoReal = Button(marcoContenedorOpcionesPantallaPrincipal, width=6, height=1, 
    text="Acceso", font="InputMonoCondensed 12", command= lambda: abrirVisualizacionDeEstadiosEnTiempoReal(pantallaDeInicio))

textoMetricasDeEstadiosEnTiempoReal = Label(marcoContenedorOpcionesPantallaPrincipal, compound= LEFT, text="- Metricas de Estadios en Tiempo Real.", font=("InputMonoCondensed  18"))
botonMetricasDeEstadiosEnTiempoReal = Button(marcoContenedorOpcionesPantallaPrincipal, compound= LEFT, width=6, height=1, 
    text="Acceso", font="InputMonoCondensed 12", command= lambda:print("test"))

textoConsultarEstadios = Label(marcoContenedorOpcionesPantallaPrincipal, text="- Consultar Estadios.", font=("InputMonoCondensed  18"))
botonConsultarEstadios = Button(marcoContenedorOpcionesPantallaPrincipal, width=6, height=1, 
    text="Acceso", font="InputMonoCondensed 12", command= lambda:print("test"))

textoConsultarAsistentes = Label(marcoContenedorOpcionesPantallaPrincipal, text="- Consultar Asistentes.", font=("InputMonoCondensed  18"))
botonConsultarAsistentes = Button(marcoContenedorOpcionesPantallaPrincipal, width=6, height=1, 
    text="Acceso", font="InputMonoCondensed 12", command= lambda:print("test"))


textoCrearEstadio = Label(marcoContenedorOpcionesPantallaPrincipal, text="- Crear Nuevos Estadios.", font=("InputMonoCondensed  18"))
botonCrearEstadio = Button(marcoContenedorOpcionesPantallaPrincipal, width=6, height=1, 
    text="Acceso", font="InputMonoCondensed 12", command= lambda:print("test"))

textoAjustesMetricasSimulacion = Label(marcoContenedorOpcionesPantallaPrincipal, text="- Ajustes Metricas Simulacion.", font=("InputMonoCondensed  18"))
botonAjustesMetricasSimulacion = Button(marcoContenedorOpcionesPantallaPrincipal, width=6, height=1, 
    text="Acceso", font="InputMonoCondensed 12", command= lambda:print("test"))

#Grid - Pantalla Principal

tituloPantallaPrincipal.grid(row=0, column=0,pady=10, padx=40)

marcoContenedorOpcionesPantallaPrincipal.grid(row=1, column=0, pady=10, padx=40)

textoVisualizacionDeEstadiosEnTiempoReal.grid(row=2, column=0, pady=10, padx = 18)
botonVisualizacionDeEstadiosEnTiempoReal.grid(row=2,column=1, padx=48, pady=10)

textoMetricasDeEstadiosEnTiempoReal.grid(row=3, column=0, sticky= "w", padx= 18, pady=10)
botonMetricasDeEstadiosEnTiempoReal.grid(row=3,column=1, padx=48, pady=10)

textoConsultarEstadios.grid(row=4, column=0, sticky= "w", padx= 18, pady=10)
botonConsultarEstadios.grid(row=4,column=1, padx=48, pady=10)

textoConsultarAsistentes.grid(row=5, column=0, sticky= "w", padx= 18, pady=10)
botonConsultarAsistentes.grid(row=5,column=1, padx=48, pady=10)

textoCrearEstadio.grid(row=6, column=0, sticky= "w", padx= 18, pady=10)
botonCrearEstadio.grid(row=6,column=1, padx=48, pady=10)

textoAjustesMetricasSimulacion.grid(row=7, column=0, sticky= "w", padx= 18, pady=10)
botonAjustesMetricasSimulacion.grid(row=7,column=1, padx=48, pady=10)

pantallaDeInicio.mainloop()



