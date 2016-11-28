# -*- coding: utf-8 -*-
from __future__ import division

k=input('Digite k: ')
i=0
soma=0
while i<=k :
    if i==0 or i%2==0:
        soma=soma+ 4*(2*k+1)
    else:
        soma=soma-4*(2*k+1)
    i=i+1
print(soma)