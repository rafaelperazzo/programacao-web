# -*- coding: utf-8 -*-
from __future__ import division

b = input('INSIRA O NUMERO: ')
a = b
n=1
soma=0

while a//2!=0:
    n=n+1
    a=a//2
print n

for i in range(0,n,1):
    d=(b%2)*(10**i)
    soma=soma+d
    b=b//2
    
print soma
