#!/usr/bin/env python 
#-*- coding: utf-8 -*-

def fun (x,y):
	mn=0
	ma=0
	
	if(x>y):
		mn=y
		ma=x
	elif(y<x):
		mn=x
		ma=y
	elif(x==y):
		mn=x
		ma=x
		
	while(mn<=ma):
		if(mn%2==0):
			print mn
		mn+=1
