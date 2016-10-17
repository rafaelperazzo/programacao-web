# -*- coding: utf-8 -*-
from __future__ import division
import math

m=input('quantidade de termos:')
cont=3
a=4
i=1
j=2
k=3
while i<=m:
    pi=cont+(a/(i*j*k))-(a/(k*i*j))
    print('cont')
     
    cont=cont+1
    i=i+1
    j=j+1
    k=k+1