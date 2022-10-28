# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 11:40:35 2022

@author: berni
"""

from Conector import establecerConexion

db = establecerConexion('localhost', 'root', '7821', 'tfg')
cursor = db.cursor()

cursor.execute("SELECT Secciones FROM tfg.estadio WHERE idEstadadio = '0'")

print(cursor.fetchall()[0][0])