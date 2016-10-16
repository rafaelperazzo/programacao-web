# -*- coding: utf-8 -*-
from __future__ import division
a=input('digite a:')
soma=0
i=1
while i<a:
    if a%i==0:
        soma=soma+i
    i=i+1
if soma==a:
    print ('perfeito')
else:
    print ('n perfeito')

        