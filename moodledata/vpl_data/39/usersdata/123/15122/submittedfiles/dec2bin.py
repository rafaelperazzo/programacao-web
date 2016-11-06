# -*- coding: utf-8 -*-
from __future__ import division

d=input('Insira um número em d:')
n=0
c=d
while c>0:
    n=n+1
    c=c/2
soma=0
i=0
while i<n:
    soma=soma + ((d%2)*(10**i))
    d=d//2
    i=i+1
print(soma)