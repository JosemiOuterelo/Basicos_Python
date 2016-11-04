#!/usr/bin/env python 
#-*- coding: utf-8 -*-

n=int(raw_input("Introduce numero : "))
cont=2
for ele in range(n+1):
	ele+=1
	if ele!=1 and ele!=n and n%ele==0:
		cont+=1

if cont==2:
	print n," es primo"
elif cont>2:
	print n," no es primo"
