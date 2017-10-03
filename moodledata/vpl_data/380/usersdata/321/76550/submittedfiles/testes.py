# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
#ENTRADA
a = input('Digite a: ')
b = input('Digite b: ')
c = input('Digite c: ')
delta = b**2-4*a*c
x1= (-b+delta**1/2)/2
x2= (-b-delta**1/2)/2
if delta >=0 :
    print (x1 and x2)