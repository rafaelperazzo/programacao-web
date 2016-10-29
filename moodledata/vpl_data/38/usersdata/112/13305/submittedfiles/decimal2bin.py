# -*- coding: utf-8 -*-
from __future__ import division
a=0
soma=0
n=input('Digite a quantidade de números')
while a<n:
    r=n
    a=a+1
    p=input('Digite 0 ou 1')
    if p==1:
        p=(2**r-1)
    r=r-1
    soma=soma+p
print(soma)