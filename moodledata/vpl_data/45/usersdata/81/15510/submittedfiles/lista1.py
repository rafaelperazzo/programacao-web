# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite a quantidade de números da lista:')
t=[]
pares=impares=0
qpares=qimpares=0

for i in range (0,n,1):
    t.append('Digite o valor do elemento da lista:')
    
for j in range (0,n,1):
    if t[j]%2==0:
        pares=pares+j
        qpares=qpares+1
    else:
        impares=impares+j
        qimpares=qimpares+1
print impares
print pares
print qimpares
print qpares
print (t)