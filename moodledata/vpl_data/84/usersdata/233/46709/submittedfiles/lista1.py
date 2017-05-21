# -*- coding: utf-8 -*-
from __future__ import division
n=int(input('Digite o número de valores: '))
list=[]
impares=[]
pares=[]
somaímpares=0
somapares=0
for i in range(1,n+1,1):
    a=int(input('Digite um  número: '))
    list=list+[a]
for i in range(0,n+1,1):
    a=list[i]
    if a%2==1:
        impares=impares+[a]
        somaimpares=somaimpares+a
    elif a%2==0:
        pares=pares+[a]
        somapares=somapares+a
qimpares=len(impares)
qpares=len(pares)
print(somaimpares)
print(somapares)
print(qimpares)
print(qpares)
print(list)