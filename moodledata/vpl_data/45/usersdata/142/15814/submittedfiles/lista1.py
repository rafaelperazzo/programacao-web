# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite n:')
L=[]

for i in range (0,n,1):
    L.append(input('Digite um valor:'))

SI=0
SP=0
QI=0
QP=0

for i in range (0,n,1):
    if (L[i]%2==1):
        SI=SI+L[i]
        QI=QI+1
    if (L[i]%2==0):
        SP=SP+L[i]
        QP=QP+1

print('%d'%SI)
print('%d'%SP)
print('%d'%QI)
print('%d'%QP)
print L