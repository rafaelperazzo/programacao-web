# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somaL(a,x):
    
    soma=0
    for j in range (0,a.shape[1],1):
        soma = soma+a[x,j]
        
    return soma

def somaC(a,y):
    for i in range (0,a.shape[0],1):
        soma = soma + a[i,y]
    return soma
        
def peso(a):
    somaL = somaL(a)
    somaC = somaC(a)
    
    peso = somaL + somaC
    for i in range(0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if a[x,y]
            
linhas = input('Digite a quantidade de linhas:')
colunas = input('Digite a quantiudade de colunas:')
a = np.zeros ((linhas,colunas))

        
        