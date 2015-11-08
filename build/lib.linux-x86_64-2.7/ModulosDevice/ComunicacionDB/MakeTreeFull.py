#!/usr/bin/env python

# Comunication.py, script que permite gestionar la comunicacion con la base de datos
# 
# Copyright (C) 14/10/2015 David Alfredo Medina Ortiz  dmedina11@alumnos.utalca.cl
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA

#Modulos a utilizar
import sys
import psycopg2

from ModulosDevice.ComunicacionDB import Comunication

def MakeTree ():

	#establecemos la comunicacion
	database = Comunication.BeginComunication()

	#creamos una consulta...
	query = "SELECT * FROM campus"

	info_campus = Comunication.MakeQueryDB (query, database[1])#gestionamos la consulta

	for element in info_campus:
		print element

	return 0
