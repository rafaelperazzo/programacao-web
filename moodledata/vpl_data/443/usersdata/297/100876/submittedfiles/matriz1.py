# -*- coding: utf-8 -*-
import numpy as np
m=int(input('digite o número de linhas que sua matriz terá: '))
n=int(input('digite o número de linhas que sua matriz terá: '))
matriz=[]
for i in range(0,m,1):
    linhas=0
    for j in range(0,n,1):
        linhas.append(int(input('digite o elemento da linha e da coluna: '((i+1),(j+1)))))
    matriz.append(linhas)
print(matriz)