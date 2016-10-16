# -*- coding: utf-8 -*-
from __future__ import division
maior=0
dia=1
i=1
while(i<=30):
    n=input('digite a quantidade de discos vendidos:')
    if n>maior:
        maior=n
        dia=i
print(dia)
print(maior)