# -*- coding: utf-8 -*-
from __future__ import division
import math

x=int(input('Digite o valor de x:'))
y-int(input('Digite o valor de y:'))


if x<y:
   i=x
if y<x:
    i=y
    contador=0
    
while contador==0 and i<=x and i<=y:
    if x%i==y%i==0:
        contador=contador+1
    else:
        i=i-1
print(i)
    