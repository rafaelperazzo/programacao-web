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

a = funcoes.somacolunas (A)
print (a)
o = funcoes.somalinhas (A)
print (o)
#matriz T
for i in range (0,dimensao,1):
    partedebaixo = 0
    for j in range (0,dimensao,1):
        if d[i,j] !=0 :
            partedecima = a[j] * (1/(d[i,j]**alfa))
            for k in range (0,dimensao,1):
                if d[i,k] !=0 :
                    partedebaixo = partedebaixo + (a[k]*(1/d[i,k]))
            T[i,j] = o[i] * (partedecima/partedebaixo)
            
                elif d[i,k] == 0:
                    T[i,j] = 0
        
        elif d[i,j] == 0:
            T[i,j] = 0

#SAÍDA

somatorio = sum(sum(T))
print('%.4f' % somatorio)
print (T)
