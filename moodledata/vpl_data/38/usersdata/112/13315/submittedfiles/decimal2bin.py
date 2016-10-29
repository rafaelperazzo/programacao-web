# -*- coding: utf-8 -*-
from __future__ import division
soma=0
n=input('Digite a quantidade de números')
a=n
i=0

while n>i:
    i=i+1
    a=a-1
    p=input('Digite 0 ou 1:')
    p=p*2**a
    soma=soma+p
print(soma)