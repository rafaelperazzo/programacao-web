# -*- coding: utf-8 -*-
from __future__ import division

#escreva suas funcoes aqui
def somaC(a):
    soma=0
    b=[]
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],):
            soma=soma+a[i,j]
            b.append(soma)
            return b
