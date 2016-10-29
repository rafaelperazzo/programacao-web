# -*- coding: utf-8 -*-
from __future__ import division
a=0
soma=0
n=input('Digite a quantidade de números')
while a<n:
    a=a+1
    p=input('Digite 0 ou 1')
    if p==1:
        p=(p**n-1)
    n=n-1
    soma=soma+p
print(soma)