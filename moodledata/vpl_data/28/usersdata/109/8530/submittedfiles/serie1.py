# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Digite o valor de n:')
cont=0

for i in range (0,n,1):
    if i%2==0:
        i=(i*(-1))
    a=(i/(i**2))
    cont=cont+a
    i=i+1
    print ('%.5f'%cont)