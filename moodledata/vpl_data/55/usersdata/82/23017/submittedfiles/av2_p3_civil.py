# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

linhas = input('Digite a quantidade de linhas:')
colunas = input('Digite a quantiudade de colunas:')
a = np.zeros ((linhas,colunas))

def somaL(a):
    soma=0
    for i in range (0,a.shape[0],1):
        soma=soma+a[i]
        a.append
        