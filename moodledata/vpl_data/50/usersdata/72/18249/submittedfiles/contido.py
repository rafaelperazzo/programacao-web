# -*- coding: utf-8 -*-
from __future__ import division

def contido(a,b):
    cont=0
    for i in range(0,len(b),1):
        if b[i] in a:
            cont=cont+1
    return cont
    
n=input('digite a quantidade de elementos de a:'))
m=input('digite a quantidade de elementos de b:'))

a=[]
b=[]

print contido(a,b)

