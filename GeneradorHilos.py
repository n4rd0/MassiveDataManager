# -*- coding: utf-8 -*-

from Generador import *

def generarAsistentesHilo(numeroDeAsistentes, generarSubida, imprimirPorPantalla):
    asistentes = generarAsistentes(numeroDeAsistentes)
    
    if imprimirPorPantalla:
        for asistente in asistentes:
            print(asistente)
       
    if generarSubida:
        insertarAsistenteBaseDatos(asistentes)