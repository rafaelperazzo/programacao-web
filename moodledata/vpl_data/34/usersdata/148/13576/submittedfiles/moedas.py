# -*- coding: utf-8 -*-
from __future__ import division
a=input('valor de moeda disponivel: ')
b=input('Valor de moeda disponivel: ')
c=input('valor da cedula')
contmaior=0
contmenor=0

if a>b:
    maior=a
    menor=b
elif b>a:
    maior=b
    menor=a

while c>=maior:
    contmaior=contmaior+1
    c=c-maior
    
while c>=menor:
    contmenor=contmenor+1
    c=c-menor


    print ('%d' %contmaior)
    print ('%d' %contmenor)
    

    
    
