# -*- coding: utf-8 -*-
import numpy as np
import funcoes

#ENTRADA
dimensao = int(input('Digite a dimensao das matrizes: '))
matrizA = input('Digite a Matriz A como uma única linha: ')
matrizD = input('Digite a Matriz D como uma única linha: ')
alfa = int(input('Digite o valor de alfa: '))

#PREPARANDO A ENTRADA
T = np.zeros((dimensao,dimensao))
A = np.fromstring(matrizA, sep=' ').reshape(dimensao, dimensao)
d = np.fromstring(matrizD, sep=' ').reshape(dimensao, dimensao)

#comece aqui...
#INÍCIO

#FUNÇÃO SOMATÓRIO
def funcaoSoma(a,d,i):
    somatorio=0
    for k in range(0,d.shape[0],1):
        somatorio=somatorio+(a[k]*(1/(d[i,k])))
    return(somatorio)
    
'''    
i=1    
print(funcaoSoma(a,d,i))   
'''
    
#PROGRAMA PRINCIPAL
a=[]
o=[]
for i in range(0,A.shape[0],1):
    soma=0
    for j in range(0,A.shape[1],1):
        soma=soma+A[i,j]
    a.append(soma)
print(a)
for j in range(0,A.shape[1],1):
    soma=0
    for i in range(0,A.shape[0],1):
        soma=soma+A[i,j]
    o.append(soma)
print(o)
print()

for i in range(0,dimensao,1):
    for j in range(0,dimensao,1):
        T[i,j]=o[i]*(a[j]*(1/d[i,j]**alfa)/(funcaoSoma(a,d,i))
print('Matriz T: ')
print(T)
print('somatorio: ')
'''
print(funcaoSoma(a,d,i))

#SAÍDA

somatorio = sum(sum(T))
print('%.4f' % somatorio)
