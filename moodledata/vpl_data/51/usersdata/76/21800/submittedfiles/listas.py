# -*- coding: utf-8 -*-
from __future__ import division
import math

def maiorDegrau(a):
    maior = 0
    for i in range (0,len(a)-1,1):
        Degrau = math.fabs(a[i]-a[i+1])
        if degrau>maior:
            maior = Degrau
    return maior
    
n = input('Digite o valor de n:')
a = []

maior = 0
for i in range(0,len(a)-1,1):
    a.append(input('Digite os valores de a:')
    Degrau = math.fabs(a[i]-a[i+1])
    if Degrau>maior:
        maior = Degrau
print maior    
    