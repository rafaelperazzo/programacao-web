# -*- coding: utf-8 -*-
from __future__ import division
import math
def mais_alto(a):
    maior=a[0]
    for i in range(0,len(a),1):
        if a[i]>maior:
            maior=a[i]
    return maior

def mais_baixo(a):
    menor=a[0]
    for i in range(0,len(a),1):
        if a[i]<menor:
            menor=a[i]
    return menor

def pino(a,m):
    b=mais_alto(a)
    c=mais_baixo(a)
    F=math.fabs(b-m)
    H=math.fabs(c-m)
    soma=F+H
    return soma
            
n=input('Quantidade de pinos:')
m=input('Digite a altura:')
a=[]
for i in range(0,n,1):
    a.append(input('Dig um elemento:'))

x=pino(a,m)
print ('%d'%x)
