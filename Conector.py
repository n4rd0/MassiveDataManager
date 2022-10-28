# -*- coding: utf-8 -*-

import pymysql

"""
Created on Thu Oct 27 13:19:52 2022

@author: berni
"""

def establecerConexion(host, usuario, contrasenia, bbdd):
    #conexion a la bbdd 
    db = pymysql.connect(host = 'localhost', 
                         user = 'root', 
                         passwd = '7821', 
                         database = 'tfg')
    return db
