# -*- coding: utf-8 -*-
from __future__ import division

#entrada
b=input('digite o valor de b:')

x=b
expoente=0
contador=0
d=0
#processamento 

while expoente<x:
    x=x//10
    contador=contador+1

while expoente<contador:
    y=b%10
    b=b//10
    d=d+(y*(2**expoente))
    expoente=expoente+1

#saida
print(d)