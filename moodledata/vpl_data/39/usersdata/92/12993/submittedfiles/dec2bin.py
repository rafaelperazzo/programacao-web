# -*- coding: utf-8 -*-
from __future__ import division

n= int(input('Digite um valor: '))

e=1
soma=0
while n>=1:
    soma= soma+(n%2)*(10**e)
    e=e+1
    n= n//2

print(soma)