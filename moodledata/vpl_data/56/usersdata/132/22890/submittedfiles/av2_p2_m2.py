# -*- coding: utf-8 -*-
from __future__ import division
def pontos(a,pe,ps):
    s=0
    for i in range(pe,ps,1):
        s=s+a[i]
    return s    
n=input('digite a qauntidade de salas:')
a=[]
for i in range(0,n,1):
    a.append(input('digite a quantidade de vidas da sala:'))
pe=input('digite o indice da porta de entreda:')
ps=input('digite o indice da porta de saida:')
print(pontos(a,pe,ps))