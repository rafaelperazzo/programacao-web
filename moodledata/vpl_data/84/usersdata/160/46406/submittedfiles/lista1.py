# -*- coding: utf-8 -*-
from __future__ import division


n=int(input('Digite n:'))

i=0
soma=0
cont=0

for i in range(1,n+1,1):
    nu=int(input('digite a entrada:'))
    if n>i:
        if n%2==0:
            soma=soma+i
    if n<i:
        if n%2==1:
            cont=cont+1
print(soma)
print(cont)
print(nu)

    
