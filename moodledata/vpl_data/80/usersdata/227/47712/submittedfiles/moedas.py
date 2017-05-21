# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('valor da moeda:'))
b=int(input('valor da moeda:'))
c=int(input('valor da cedula:'))

cont=0
for i in range (2,c+1,1):
    if c%a!=0:
        cont=c//a
    if c%a!=0:
        cont=c//b
print(cont)