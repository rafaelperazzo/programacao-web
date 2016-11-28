# -*- coding: utf-8 -*-
from __future__ import division

def maior(a):
    maiorDegrau=0
    for i in range (0,len(a)-1,1):
        degrau= a[i]-a[i+1]
        if degrau<0:
            degrau=degrau*(-1)
        if degrau>maiorDegrau:
            maiorDegrau=degrau
    return maiorDegrau
    
a=[]    
n=input ('Digite a quantidade de elementos da lista a:')

for i in range (0,n,1):
    a.append (input('Digite um elemento da lista a:'))
    
print maior(a)    
    