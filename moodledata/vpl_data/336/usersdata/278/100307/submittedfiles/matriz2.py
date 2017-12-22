# -*- coding: utf-8 -*-
import numpy as np
n = int(input("Digite a dimensão da matriz: "))
matriz = np.empty([n,n])
for i in range (0,n,1):
    for j in range (0,n,1):
        matriz[i][j] = float(input("Digite o elemento da linha%.d e coluna%.d: " %(i,j)))
somaL=0
somaC=0
somaDP=0
somaDS=0
for i in range (0,n,1):
    somaL+=matriz[i]
    somaL*=-1
for j in range (0,n,1):
    somaC+=matriz[j]
    somaC*=-1
for i in range (0,n,1):
    somaDP+=matriz[i][i]
    somaDP*=-1
for i in range (0,n,1):
    for j in range (n-1,-1,-1):
        somaDS+=matriz[i][j]
        somaDS*=-1
if somaL.all (==somaC and ==somaDP and ==somaDS):
    print("S")
else:
    print("N")

