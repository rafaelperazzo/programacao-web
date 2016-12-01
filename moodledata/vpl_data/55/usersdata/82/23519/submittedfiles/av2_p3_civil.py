# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

linhas = input('Digite a quantidade de linhas:')
colunas = input('Digite a quantiudade de colunas:')
a = np.zeros ((linhas,colunas))

def somaL(a):
    soma=0
    for i in range (0,a.shape[0],1):
        a.append(input('Digite um elemento:'))
        soma=soma+a[i]

def somaC(a):
    for j in range (0,a.shape[1],1):
        a.append(input('Digite um elemento:'))
        soma = soma+a[i]
        
def peso(a):
    for i in ranfge
        