# -*- coding: utf-8 -*-
from __future__ import division
import math

def maior_degrau (x):
    maior = 0
    for i in range (0,len(x)-1,1):
        degrau = math.fabs (x[i] - x[i+1])
        if degrau > maior:
            maior = degrau
    return maior        

n = input('digite a quantidade de termos da lista: ')
a = []

for i in range (0,n,1):
    a.append (input('digite a quantidade de termos da lista: '))
    
print maior_degrau (a)    

