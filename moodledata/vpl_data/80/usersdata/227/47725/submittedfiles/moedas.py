# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('valor da moeda:'))
b=int(input('valor da moeda:'))
c=int(input('valor da cedula:'))

resto=0
cont=0
cont2=0
for i in range (2,c+1,1):
    if c%a!=0:
        resto=c%a
        cont=c//a
    if c%a!=0:
        cont1=resto//b
    if c%b!=0:
      cont2=c//b  
print(cont)
print(cont1)
print(cont2)