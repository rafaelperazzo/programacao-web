# -*- coding: utf-8 -*-
from __future__ import division

b=input('Insira um número binário: ')
n=0
q=b

while q>=1:
    q=q/10
    n=n+1
    
soma=0

for i in range (0,n,1):
    ri=b%10
    d=ri*(2**i)
    soma=soma+d
    b=b//10

print soma