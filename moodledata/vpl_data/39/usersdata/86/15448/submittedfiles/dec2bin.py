# -*- coding: utf-8 -*-
from __future__ import division

d = int(input('d:'))
soma=0
cont=0
while d>0:
    soma=soma+(d%2)*(10**cont)
    d=d//2
    cont=cont+1
print(soma)