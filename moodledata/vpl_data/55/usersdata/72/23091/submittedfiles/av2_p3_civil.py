# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def soma_linha(a,l):
    soma=0
    for j in range(0,a.shape[1],1):
        soma=soma+a[l,j]
    return soma
    

def sona_coluna(a,c):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,c]
    return soma
    

def soma_total

