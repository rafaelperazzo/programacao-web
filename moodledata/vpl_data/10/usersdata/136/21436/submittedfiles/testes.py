# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np


#RESOLUÇÃO LISTA 4 MATRIZES

#PRIMEIRO PASSO - DESCOBRIR A COLUNA CENTRAL
#"central = a.shape[0]//2"  ->> "//" é o resultado da divisão inteira

#SEGUNDO PASSO - Testar pares de elementos e CONTAR se forem IGUAIS

def simetricaC(a):
    c = a.shape[0]//2
    cont = 0
    for i in range(0,shape[0],1):
        f = a.shape[0]-1
        for j in range(0, c, 1):
            if a[i,j] == a[i,f]
            cont = cont + 1
        f = f - 1
    