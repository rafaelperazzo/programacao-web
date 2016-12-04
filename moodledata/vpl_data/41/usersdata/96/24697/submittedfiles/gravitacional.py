# -*- coding: utf-8 -*-
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
def a(A):
    a = []
    for j in range(0,n,1):
        somacoluna = 0
        for i in range(0,n,1):
            somacoluna = somacoluna + A[i,j]
        a.append(somacoluna)
    return a

def o(A):
    o = []
    for i in range(0,n,1):
        somalinha = 0
        for j in range(0,n,1):
            somalinha = somalinha + A[i,j]
        o.append(somalinha)
    return o

def T(a,o,d):
    a = a(A)
    o = o(A)
    T = np.zeros((n,n))
    for i in range(0,n,1):
        for j in range(0,n,1):
            somatorio = 0
            for k in range(0,n,1):
                if i!=k:
                    somatorio = somatorio + (a[k]*(1/d[i,k]))
                if i!=j:
                    T[i,j]= (o[i]*a[j]*(1/(d[i,j]))**alfa)/somatorio
    return T

def somaT(T):
    T = T(a,o,d)
    soma = 0
    for i in range(0,n,1):
        for j in range(0,n,1):
            soma = soma + T[i,j]
    return soma
 
n = input('Digite a dimensão das matrizes:') 
A = np.zeros((n,n))
for i in range(0,n,1):
    for j in range(0,n,1):
        A[i,j] = input('Digite um valor de A:')
d = np.zeros((n,n))
for i in range(0,n,1):
    for j in range(0,n,1):
        d[i,j] = input('Digite um vaor de d:')
alfa = input('Digite um valor de alfa:')

somaT = somaT(T)
print('%.4f' %somaT)


#SAÍDA

somatorio = sum(sum(T))
print('%.4f' % somatorio)
