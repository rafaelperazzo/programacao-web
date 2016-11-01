# -*- coding: utf-8 -*-
from __future__ import division
a=input('valor de moeda disponivel')
b=input('Valor de moeda disponivel')
c=input('valor da cedula')
contmaior=contmaior+1
contmenor=contmenor+1

if a>b:
    maior=a
    menor=b
elif b>a:
    maior=b
    menor=a

while c>0:
    c=c-maior
    contmaior=contmaior+1

    
    
