# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('valor da moeda:'))
b=int(input('valor da moeda:'))
c=int(input('valor da cedula:'))

resto=0
cont=0
cont1=0
for c in range(1,c+1,1):
    if c//a!=0:
        cont=c//a
        cont1=c//b
        resto=c//a
    if resto//b!=0:
         cont=c//a
         cont=c//b
         resto=c//a
        
    if  c//a==0 or c//b==0:
        cont1=c//b
        cont=c//a
print(cont)
print(cont1)