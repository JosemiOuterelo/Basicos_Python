#!/usr/bin/env python 
#-*- coding: utf-8 -*-

def fun(li):
	lu=[]
	cont=0;
	for ele in li:
		if (cont%2!=0):
			lu.append(ele)
		cont+=1
	return lu
