# -*- coding: utf-8 -*-
from __future__ import division
import math

def maiorDegrau(a):
    maior = 0
    for i in range (0,len(a)-1,1):
        degrau = math.fabs(a[i] - a[i+1])
        if degrau > maior:
            maior = degrau
    return maior
    
n = input('Digite o valor de n:')
a = []

for i in range(0,len(a)-1,1):
    a.append(input('Digite os valores da lista:')
    