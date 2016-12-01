# -*- coding: utf-8 -*-
from __future__ import division
import math

def maior(a):
    maior=a[0]
    for i in range(0,len(a),1):
        if a[i]>maior:
            maior=a[i]
    return maior

def menor(a):
    menor=a[0]
    for i in range(0,len(a),1):
        if a[i]<menor:
            menor=a[i]
    return menor

def somatotal(a,m):
    soma=(math.fabs(maior(a)-m))+(math.fabs(menor(a)-m))
    return soma
    
n=input('digite a quantidade de pinos:')
m=input('digite a altura em que os devem ficar:')
a=[]
for i in range(0,n,1):
    a.append(input('digite a altura dos pinos:')

print (somatotal(a,m))

