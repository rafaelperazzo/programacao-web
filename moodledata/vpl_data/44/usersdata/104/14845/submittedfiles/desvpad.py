# -*- coding: utf-8 -*-
from __future__ import division
import math
#Entrada
n=input('Digite o valor de n:')
l=[]
soma=0
#Processamento
for i in range(0,n,1):
    l.append(input('Digite o valor:'))
for i in range(0,n,1):
    soma=soma+l[i]
media=(soma/len(l))
somat=0
for i in range(0,n,1):
    somat=somat+((l[i]-media)**2)
variancia=((1/n-1)*(somat))**0.5
#Saída
print('%.2f'%(l[0]))
print('%.2f'%(l[i]))
print('%.2f'%(media))
print('%.2f'%(variancia))
