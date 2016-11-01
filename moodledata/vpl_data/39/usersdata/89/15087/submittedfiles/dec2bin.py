# -*- coding: utf-8 -*-
from __future__ import division

#entrada

n=input('digite o valor de n:')

x=n
expoente=0
contador=0
d=0

#processamento
while expoente<x:
    x=x//2
    contador=contador+1

while expoente<contador:
    y=n%2
    n=n//2
    d=d+(y*(10**expoente))
    expoente=expoente+1

#saida
print(d)