# -*- coding: utf-8 -*-
import numpy as np

l=int(input('digite o numero de linhas da matriz: '))
c=int(input('digite o numero de colunas da matriz: '))
m[i] [j]=int(input('digite o numero na linha%.d e coluna%.d: '  %((i+1),(j+1))))


def cria_matriz(l,c,m):
    m=np.empty([l,c])
    for i in range(0,l,1):
        for j in range(0,c,1):
            m[i] [j]=int(input('digite o numero na linha%.d e coluna%.d: '  %((i+1),(j+1))))
    return(m)

