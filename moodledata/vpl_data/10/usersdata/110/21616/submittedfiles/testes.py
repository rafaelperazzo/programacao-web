# -*- coding: utf-8 -*-
from __future__ import division


def arctan(x):
    soma=0
    i=0
    while (x**(2*i+1))/(2*i+1)>0.0001 :
        soma=soma+((-1)**i)*(x**(2*i+1))/(2*i+1)
        i=i+1
    return soma
x=input('Digite k: ')
print(arctan(x))