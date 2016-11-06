# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite um número na base decimal:')

n1=0

q=n

while q>0:
    q=q//2
    n1=n1+1
    
soma=0

for i in range (0,n1,1):
    a=n%2
    c=a*(10**i)
    soma=soma+c
    n=n//2
    
print (soma)