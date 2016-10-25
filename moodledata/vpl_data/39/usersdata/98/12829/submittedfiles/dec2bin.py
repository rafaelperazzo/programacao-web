# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite o valor de n: ')
soma=0
i=0
while True:
    a=(n%2)*(10**i)
    soma=soma+a
    if n//2==0:
        break
    n=n//2
    i=i+1
print(soma)