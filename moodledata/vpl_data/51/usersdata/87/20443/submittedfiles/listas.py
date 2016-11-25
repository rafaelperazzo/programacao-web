# -*- coding: utf-8 -*-
from __future__ import division
import math

def maiordegrau (lista):
    maior=0
    for i in range (0,len(lista)-1,1):
        degrau=math.fabs(lista[i]-lista[i+1])
        if degrau>maior:
            maior = degrau
    return maior

a=[]
n=int(input('digite quantidade de termos:'))
for i in range(0,n,1):
    a.append(int(input('digite termos:')))

print maiordegrau (a)
    
        