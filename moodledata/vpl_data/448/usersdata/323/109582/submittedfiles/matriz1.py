# -*- coding: utf-8 -*-

import numpy as np

m=int(input('Digite a quantidade de linhas da matriz: '))
n=int(input('Digite a quantidade de colunas da matriz: '))

a=np.zeros((m,n))

for i in range(0,m,1):
    for j in range(0,n,1):
        a[i,j]= float(input('Digite os elementos: '))

def rodar_90(matriz):
    nova_matriz=[[0 for j in range (len(matriz))] for i in range(len(matriz[0]))]
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[0])):
            nova_matriz[coluna][len(matriz)-1-linha] = matriz[linha][coluna]
    return nova_matriz
def rodar_180(matriz):
    return rodar_90(rodar_90(matriz))
def rodar(matriz,grau):
    if grau==180:
        return rodar_180(matriz)
        
print(rodar(a,180))