hb# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
import funcoes

#ENTRADA
dimensao = input('Digite a dimensao das matrizes: ')
matrizA = input('Digite a Matriz A como uma única linha entre aspas: ')
matrizD = input('Digite a Matriz D como uma única linha entre aspas: ')
alfa = input('Digite o valor de alfa: ')

#PREPARANDO A ENTRADA
T = np.zeros((dimensao,dimensao))
A = np.fromstring(matrizA, sep=' ').reshape(dimensao, dimensao)
d = np.fromstring(matrizD, sep=' ').reshape(dimensao, dimensao)

#comece aqui...
#INÍCIO
def somaColunaA(m):
    b=[]
    for j in range (0,m.shape[1],1):
        soma=0
        for i in range(0,m.shape[0],1):
            soma=soma+m[i,j]
            b.append (soma)
            return b
def somaLinhaA(m):
    b=[]
    for i in range (0,m.shape[0],1):
        soma=0
        for i in range(0,m.shape[1],1):
            soma=soma+m[i,j]
            b.append (soma)
            return b

def matrizT(c,o,a):
    for i in range (0,c.shape[0],1):
        for j in range (0,c.shape[1],1):
            c[i,j]=o([i])*a([i])*i*((1/d[i,j]))*alfa
                return c
            
o=somaLinhaA(m)
a=somaColunaA(m)
T=[]
    


#SAÍDA

somatorio = sum(sum(T))
print('%.4f' % somatorio)
