# -*- coding: utf-8 -*-
from __future__ import division

#entrada
b=input('digite o valor de b:')

x=b
i=0
contador=0
d=0
#processamento 

while i<x:
    x=x//10
    contador=contador+1

while i<contador:
    y=b%10
    b=b//10
    d=d+(y*(2**i))
    i=i+1

#saida
print(d)