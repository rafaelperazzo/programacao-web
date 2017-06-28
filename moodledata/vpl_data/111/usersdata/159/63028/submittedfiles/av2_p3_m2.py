# -*- coding: utf-8 -*-
import numpy as np

def soma(a):
    linhas=[]
    for i in range (0,a.shape[0],1):
        soma=0
        for j in range (0,,a.shape[1],1):
            soma=soma+a[i,j]
            linhas.append(soma)
    
    colunas=[]
    for j in range (0,a.shape[1],1):
        soma=0
        for i in range (0,a.shape[0],1):
            soma=soma+a[i,j]
            colunas.append(soma)
            