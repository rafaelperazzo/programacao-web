# -*- coding: utf-8 -*-
from __future__ import division
a=int(input('valor da moeda:'))
b=int(input('valor da moeda:'))
c=int(input('valor da cedula:'))

resto=0
cont=0
cont1=0

for c in range(1,c+1,1):
    if c//a!=0 or  resto//b!=0:
        cont=c//a      
        resto=c-(cont*a)
        cont1=resto//b
        
print(cont)
print(cont1)

