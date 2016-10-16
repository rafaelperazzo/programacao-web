# -*- coding: utf-8 -*-
from __future__ import division
maior=0
dia=1
for i in range(1,31,1):
    n=input('numero de discos vendidos')
    if n>maior:
        maior=n
        dia=i
print(dia)
print(maior)
        