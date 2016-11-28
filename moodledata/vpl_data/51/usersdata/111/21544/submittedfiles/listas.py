# -*- coding: utf-8 -*-
from __future__ import division

def deg(a):
    c=0
    maior=0
    for i in range(1,len(a),1):
        c=a[i]-a[i-1]
        if c<0:
            c=(c*-1)
        if c>maior:
            maior=c
    return maior
    
n=input('tamanho da lista: ')
a=[]
for i in range(0,n,1):
    a.append(input('elementos da lista: '))
    
print deg(a)
