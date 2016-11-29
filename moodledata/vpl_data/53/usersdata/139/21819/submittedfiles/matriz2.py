# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def somadiagonal1(lista):
    soma=0
    for i in range(0,lista.shape[0],1):
        soma=soma+lista[i,i]
    return soma
def somadiagonal2(lista):
    soma=0
    for i in range(0,lista.shape[0],1):
        soma=soma+lista[i,lista.shape[0]-i-1]
    return soma

