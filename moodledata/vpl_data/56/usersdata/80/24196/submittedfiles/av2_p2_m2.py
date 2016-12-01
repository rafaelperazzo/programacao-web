# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite a quantidade de salas:')
vidas= [""]*n
i=0
while i<n:
    vidas[i]=(vidas.append(input('Digite a quantidade de vidas:')))
    i=i+1
x=input('Digite a porta de entrada:')
y=input('Digite a porta de saida:')
a=y+1
entre=[]
entre=vidas[x:a]
print sum(entre)