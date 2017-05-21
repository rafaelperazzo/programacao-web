# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('valor da moeda:'))
b=int(input('valor da moeda:'))
c=int(input('valor da cedula:'))

i=0
cont=0
while i<c:
    if c//a!=0:
        cont=cont+i
    i=i+1
print(cont)