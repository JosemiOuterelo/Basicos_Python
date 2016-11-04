#!/usr/bin/env python 
#-*- coding: utf-8 -*-

def primo(n):
	primo=False
	cont=2
	for ele in range(n+1):
		ele+=1
		if ele!=1 and ele!=n and n%ele==0:
			cont+=1

	if cont==2:
		primo=True
	return primo


cont=0
ultimo=0
suma=0
salir=False

while cont<10000 and salir==False:
	n=int(raw_input("Introduce numero : "))
	
	cont+=1
	ultimo+=1
	suma+=n
	
	if ultimo==3:
		print n
		salir=primo(suma)
		suma=0
		ultimo=0

print "Se han mostrado ",cont," numeros"


	
