# -*- coding: utf-8 -*-
import numpy as np
matriz=[]
n=int(input('digite a ordem da matriz: '))
while not n>=3:
    n=int(input('digite a ordem da matriz: '))
for i in range (0,n):
    linhas=[]
    for j in range (0,n):
        linhas.append(int(input('qual o valor da linha coluna?:' )))
    matriz.append(linhas)

print(matriz)
#for j in range (0,n):
    #for i in range (0,n):
        


