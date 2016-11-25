# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
#COMECE AQUI ABAIXO

def colunaEsquerda(a):
    for i in range (0,a.shape[1],1):
        if 1 in a[:,i]:
            c1=i
            break
    return c1
        
def colunaDireita(a):
    for i in range (0,a.shape[1],1):
        if 1 in a[:,i]:
            c2=i
    return c2
    
def linhaCima(a):
    for i in range (0,shape[0],1):
        if 1 in a[i,:]:
            l1=i
            break
    return l1
          
def linhaCima(a):
    for i in range (0,shape[0],1):
        if 1 in a[i,:]:
            l2=i
    return l2