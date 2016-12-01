# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def maior_altura(l):
    maior = l[0]
    for i in range (0, len(l), 1):
        if l[i] > maior:
            maior = l[i]
    return maior

def menor_altura(l):
    menor = l[0]
    for i in range (0, len(l), 1):
        if l[i] < menor:
            menor = l[i]
    return menor
    
def abs(x):
    if x < 0:
        x = x * (-1)
        return x
    else:
        return x
        
def maior_menor_soma(l,m):
    soma = abs(maior_altura(l)-m) + abs(menor_altura(l)-m)
    return soma
    
