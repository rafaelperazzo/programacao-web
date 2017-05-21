# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('valor da moeda:'))
b=int(input('valor da moeda:'))
c=int(input('valor da cedula:'))

resto=0
resto1=0
cont=0
cont1=0
cont2=0
cont3=0

for c in range(1,c+1,1):
    if c//a==0:
        cont=c//a
    if c%a!=0:
            cont=c//b
        if c//b==0:
        cont=c//b
        if c%b!=0:
            cont=cont//a
    
        
print(cont)
print(cont1)

