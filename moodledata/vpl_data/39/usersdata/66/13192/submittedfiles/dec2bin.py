# -*- coding: utf-8 -*-
from __future__ import division
a=input ("digite a:")
soma=0
i=0
while a>0:
    r=a%2
    soma=soma + r*(10**i)
    i=i+1
    a=a//2
print soma