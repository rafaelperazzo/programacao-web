# -*- coding: utf-8 -*-
from __future__ import division

#escreva suas funcoes aqui

def a(A):
    a=[]
    for i in range (0,A.shape[0],1):
        for j in range (0,A.shape[1],1):
            soma=soma+A[i,j]
        a.append(soma)
return (a)




