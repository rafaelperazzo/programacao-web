# -*- coding: utf-8 -*-
import numpy as np

def somalinhas(a):
    cont=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        return soma

def somacolunas(a):
    soma=0
    for i in range(

