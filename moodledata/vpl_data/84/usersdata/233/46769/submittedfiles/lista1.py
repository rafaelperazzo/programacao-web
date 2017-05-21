# -*- coding: utf-8 -*-
from __future__ import division
n=int(input('Digite o número de valores: '))
list=[]
impares=[]
pares=[]
somaimpares=0
somapares=0
for i in range(1,n+1,1):
    a=int(input('Digite um  número: '))
    list=list+[a]
for number in list:
    if number%2==1:
        impares=impares+[number]
        somaimpares=somaimpares+number
    elif number%2==0:
        pares=pares+[number]
        somapares=somapares+number
qimpares=len(impares)
qpares=len(pares)
print(somaimpares)
print(somapares)
print(qimpares)
print(qpares)
list.sort()
print(list)