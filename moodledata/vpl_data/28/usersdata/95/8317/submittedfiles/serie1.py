# -*- coding: utf-8 -*-
from __future__ import division
import math

n=input('Quant de termos:')
i=1
soma=o
j=1

while i<=n:
    if i%2==0:
        soma = soma - 1/j
    else:
        soma=soma+1/j
    i=i+1
    j=j+1
print(soma)
