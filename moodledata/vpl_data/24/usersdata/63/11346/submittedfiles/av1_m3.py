# -*- coding: utf-8 -*-
from __future__ import division
import math

m=input('quantidade de termos:')
cont=3
j=2
k=3
l=4
while cont<m:
    if cont%2==0:
        cont=cont-4/(j*k*l)
    
    else:
        cont=cont+4/(j*k*l)
    cont=cont+1
    j=j+2
    k=k+2
    l=l+2
        print(cont)