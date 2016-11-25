# -*- coding: utf-8 -*-
from __future__ import division

def modulo(x):
    if x<0:
        x=x*(-1)
    else:
        x=x
    resultado=x    
    return resultado






a=[]
n=input('Digite o valor de n:')
for i in range(0,n,1):
    a.append(input('Digite um elemento:'))
for i in range(0,len(a)-2,1):
    if modulo(a[i]-a[i+1])>=modulo(a[i+1]-a[i+2]):
        maior= modulo(a[i]-a[i+1])
    else:
        maior=modulo(a[i+1]-a[i+2])
print(maior)        