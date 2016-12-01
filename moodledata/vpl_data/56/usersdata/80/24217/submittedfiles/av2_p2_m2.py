# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite a quantidade de salas:')
v= [""]*n
i=0
while i<n:
    v[i]=(v.append(input('Digite a quantidade de vidas:')))
    i=i+1
x=input('Digite a porta de entrada:')
y=input('Digite a porta de saida:')
a=y+1
e=[]
e=v[x:a]
soma=v[x]
i=x
while i<a:
    i=i+1
    soma=soma+(v[i])
print(soma)    
    