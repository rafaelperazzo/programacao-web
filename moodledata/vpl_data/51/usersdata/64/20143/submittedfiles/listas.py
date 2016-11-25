# -*- coding: utf-8 -*-
from __future__ import division
import math

def maiorDegrau(lista):
    maior = 0
    for i in range (0, len(lista)-1, 1):
        degrau = math.fabs(a[i]-a[i+1])
        if degrau>maior:
            maior = degrau
    
    return maior
    
lista = []
lista.append(input("Digite a lista: ")



