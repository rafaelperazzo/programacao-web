# -*- coding: utf-8 -*-
from __future__ import division

d=input('Insira um número de base decimal: ')
n=0
q=d

while q>0:
    q=q//2
    n=n+1

soma=0

for i in range (0,n,1):
    ri=d%2
    b=ri*(10**i)
    soma=soma+b
    d=d//2

print soma