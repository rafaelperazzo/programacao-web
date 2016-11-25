# -*- coding: utf-8 -*-
from __future__ import division
def degrau(lista):
    degrau=0
    for i in range(0,len(lista),1):
        if i<=n and n>=2:
            b=0
            degrau=degrau+(a[i]-a[i+1])
            if degrau<0:
                degrau=degrau*(-1)
            a[i]=a[i+1]
            a[i+1]=a[i+2]
            if b<degrau:
                b=degrau
    return b        

a=[]
n=input('insira o numero de termos da lista:')
for i in range(0,n,1):
    a.append(input('digite um elemento de a:')
print b    
    
