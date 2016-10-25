# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite o valor de n: ')
soma=0
cont=0
while True:
    if n==0:
        break
    a=n%10
    soma=soma+(a*(2**cont))
    cont=cont+1
    n=n//10
print(soma)