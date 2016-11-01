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

while c>=0:
    c=c-maior
    contmaior=contmaior+1
    
    while c>=0:
        c=c-menor
        contmenor=contmenor+1

print ('%d' %contmaior)
print ('%d' %contmenor)
    

    
    
