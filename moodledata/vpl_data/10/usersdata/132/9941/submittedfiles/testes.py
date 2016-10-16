# -*- coding: utf-8 -*-
from __future__ import division
maior=0
dia=1
i=1
while(i<=10):
    n=input('digite a quantidade de discos vendidos:')
    if n>maior:
        maior=n
        dia=i
    i=i+1    
print(dia)
print(maior)