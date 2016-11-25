# -*- coding: utf-8 -*-
from __future__ import division

def maior(lista):
    cont=0
    for i in range(0,len(lista),1):
        if len(lista[i])>len(lista[i+1]):
            x=lista[i]-lista[i+1]
            cont=cont+1
        if x>len(lista):
            return x
            
a=[]
n=input('digite valor de termos:')
for i in range(0,n,1):
    a.append(input('digite termos:'))

print(maior(a))
    

