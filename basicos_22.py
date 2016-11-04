#!/usr/bin/env python 
#-*- coding: utf-8 -*-

filas=int(raw_input("Introduce numero de filas : "))
columnas=int(raw_input("Introduce numero de columnas : "))

for ele1 in range(filas+1):
	for ele2 in range(columnas+1):
		prod=ele1*ele2
		print prod,
	print " "
		

