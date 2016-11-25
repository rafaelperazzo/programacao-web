# -*- coding: utf-8 -*-
from __future__ import division

def menorLinha(a):
    ml=0
    for i in range(0,a.shape[0],1):
        if 1 in a[i,:]:
            ml=i
            break
    return ml
      
def maiorLinha(a):
    mal=0
    for i in range(0,a.shape[0],1):
        if 1 in a[i,:]:
            mal=i
    return mal
def colunaesquerda(a):
    ce=0
    for j in range(0,a.shape[1],1):
        if 1 in a[:,j]:
            ce=j
            break
    return ce
def colunadireita(a):
    cd=0
    for j in range(0,a.shape[1],1):
        if 1 in a[:,j]:
            cd=j
    return cd
linhas