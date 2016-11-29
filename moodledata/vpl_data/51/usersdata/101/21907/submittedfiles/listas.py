# -*- coding: utf-8 -*-
from __future__ import division
import math

def maior_degrau(a):
    maior = 0
    for i in range (0, len(a)-1, 1):
        degrau = math.fabs(a[i] - a[i+1])
        if degrau > maior:
            maior = degrau
            cont = cont + 1
    return maior
            

n = input('Digite o número de termos da lista: ')
a = []

for i in range (0,n,1):
    a.append(input('Digite um termo: '))

print ('%d' %maior_degrau(a))