# -*- coding: utf-8 -*-
from __future__ import division

def degrau(lista):
    maior = 0
    for i in range(0,len(lista),1):
        s = lista[i] - lista[i+1]
    if s >= 0 and s > maior:
        return s
    if s<0 and (-1)*s>maior:
        return (-1)*s
n = input('Digite n:')
a = []

for i in range(0,n,1):
    a.append(input('jgd:'))
print ('%.d' %degrau(a))
