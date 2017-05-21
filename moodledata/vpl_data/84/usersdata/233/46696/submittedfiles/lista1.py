# -*- coding: utf-8 -*-
from __future__ import division
n=int(input('Digite o número de valores: '))
list=[]
ímpares=[]
pares=[]
somaímpares=0
for i in range(1,n+1,1):
    a=int(input('Digite um  número: '))
    list=list+[a]
for i in range(0,n+1,1):
    a=list[i]
    if a%2==1:
        ímpares=ímpares+[a]
        somaímpares=somaímpares+a
        