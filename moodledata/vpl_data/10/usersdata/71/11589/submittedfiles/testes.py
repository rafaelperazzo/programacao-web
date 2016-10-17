# -*- coding: utf-8 -*-
from __future__ import division

b = input('INSIRA O NUMERO: ')
a = b
n=1
soma=0

while a//10!=0:
    n=n+1
    a=a//10
   
for i in range(0,n,1):
    d=(b%10)*(2**i)
    soma=soma+d
    b=b//10
    
print soma
