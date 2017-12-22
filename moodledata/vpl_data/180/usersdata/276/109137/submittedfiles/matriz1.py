# -*- coding: utf-8 -*-

import numpy as np

def primeiralinha (matriz):
for i in range (0,linhas, 1):
    for j in range (0,colunas,1):
        if a[i,j]==1:
            return i
    
def ultimalinha (matriz):
for i in range (0,linhas, 1):
    for j in range (0,colunas,1):
        if a[i,j]==1:
            l = i
    return (i)

def primeiracoluna (matriz):
for j in range (0,colunas, 1):
    for i in range (0,linhas,1):
        if a[i,j]==1:
            return j
    
def ultimacoluna (matriz):
for j in range (0,colunas, 1):
    for j in range (0,linhas,1):
        if a[i,j]==1:
            c = j
    return (j)

linhas = int (input('Digite a quantidade de linhas: '))
colunas = int (input('Digite a quantidade de colunas: '))

a = np.zeros ((linhas, colunas))

for i in range (0,linhas,1):
    for j in range (0,colunas,1):
        a[i,j] = int(input('Digite o elemento da matriz:'))

menorlinha = primeiralinha (a)
maiorlinha = ultimalinhas (a)
menorcoluna = primeiracoluna (a)
maiorcoluna = ultimacoluna (a)

a[maiorlinha - maiorlinhas:maiorcoluna - menorcoluna - 1]