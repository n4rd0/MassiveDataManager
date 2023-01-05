# -*- coding: utf-8 -*-

class Asistente: 
    
    def __init__ (self, idEstadio , nombre, apellido, edad, DNI, plazaEstadio):
        self.idEstadio = idEstadio
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.DNI = DNI
        self.plazaEstadio = plazaEstadio

    def __str__(self):
        return ("\nid del estadio: {0} \nnombre: {1} \napellido: {2} \nedad: {3} \nDNI: {4} \nplaza Estadio: {5}"
                .format(self.idEstadio, self.nombre, self.apellido, self.edad, self.DNI, self.plazaEstadio))
    
    #En vez de __str__ usamos funcion propia para imprimir
    """
    ("\nid del estadio:", self.idEstadio, "\nnombre:", self.nombre, 
                    "\napellido:", self.apellido,"\nedad:", self.edad, 
                    "\nDNI:", self.DNI, "\nseccion:",self.plazaEstadio[0] + 
                    self.plazaEstadio[1]
                    , "\ngrupo:",self.plazaEstadio[2]+self.plazaEstadio[3]
                    , "\nfila:",self.plazaEstadio[4] + self.plazaEstadio[5]
                    , "\nasiento:",self.plazaEstadio[6] + self.plazaEstadio[7], "\n")
    """
