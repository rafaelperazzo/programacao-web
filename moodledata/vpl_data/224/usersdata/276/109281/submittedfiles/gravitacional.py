# -*- coding: utf-8 -*-
import numpy as np
import funcoes

#ENTRADA
dimensao = int (input('Digite a dimensao das matrizes: '))
matrizA = input('Digite a Matriz A como uma única linha entre aspas: ')
matrizD = input('Digite a Matriz D como uma única linha entre aspas: ')
alfa = int(input('Digite o valor de alfa: '))

#PREPARANDO A ENTRADA
T = np.zeros((dimensao,dimensao))
A = np.fromstring(matrizA, sep=' ').reshape(dimensao, dimensao)
d = np.fromstring(matrizD, sep=' ').reshape(dimensao, dimensao)

#comece aqui...
#INÍCIO

#somas colunas

somacolunas = 0
a = []

for j in range (0, dimensao,1):
    for i in range (0,dimensao,1):
        somacolunas = somacolunas + A[i,j]
    a.append (somacolunas)
    somacolunas = 0
        
print (somacolunas)

#somas linhas

somalinhas = 0
o = []

for i in range (0,dimensao,1):
    for j in range (0,dimensao,1):
        somalinhas = somalinhas + A[i,j]
    o.append (somalinhas)
    somalinhas = 0
    
partedebaixo = 0    
partedecima = 0

#matriz T
for i in range (0,dimensao,1):
    for j in range (0,dimensao,1):
        partedecima = a[j] * (1/(d[i,j]**alfa))
        for k in range (0,dimensao,1):
            partedebaixo = partedebaixo + (a[k]*(1/d[i,k])) 
        T[i,j] = o[i] * (partedecima/partedebaixo)
        
#SAÍDA

somatorio = sum(sum(T))
print('%.4f' % somatorio)
