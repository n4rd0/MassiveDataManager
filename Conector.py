# -*- coding: utf-8 -*-

import pymysql

"""
Created on Thu Oct 27 13:19:52 2022

@author: berni
"""

def establecerConexion(host, usuario, contrasenia, bbdd):
    #conexion a la bbdd 
    db = pymysql.connect(host = host, 
                         user = usuario, 
                         passwd = contrasenia, 
                         database = bbdd)
    return db
