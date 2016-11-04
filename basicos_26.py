#!/usr/bin/env python 
#-*- coding: utf-8 -*-

a=int(raw_input("Introduce primer numero : "))
b=int(raw_input("Introduce segundo numero : "))
c=int(raw_input("Introduce tercer numero : "))

if a>b and b>c:
	print c," ",b," ",a
if b>c and c>a:
	print a," ",c," ",b
if c>a and a>b:
	print b," ",a," ",c
if b>a and a>c:
	print c," ",a," ",b
if a>c and c>b:
	print b," ",c," ",a
if c>b and b>a:
	print a," ",b," ",c
