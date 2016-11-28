# -*- coding: utf-8 -*-
from __future__ import division

k=input('Digite k: ')
i=0
soma=0
while (x**(2*i+1))/(2*i+1)>0.0001 :
    soma=soma+(-1)**i*(x**(2*i+1))/(2*i+1)
    i=i+1
print(soma)