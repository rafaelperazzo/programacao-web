# -*- coding: utf-8 -*-
from __future__ import division

def somalista(a):
    i=0
    b=[]
    soma=0
    while i<=len(a):
        soma=soma+a[i]
        b.append(soma)
        i=i+1
    return b

def maiorlista(b,ent,saida):
    for i in range(0,len(b),1):
        if b[i]>b[i+1]:
            maior = b[i]
        if b[i]>maior:
            maior=b[i]
    return maior
    
n=input('n:')
m=[]
for i in range(0,n,1):
    m.append(int(input('digite um valor:'))
    
c=maiorlista(b)
print c














