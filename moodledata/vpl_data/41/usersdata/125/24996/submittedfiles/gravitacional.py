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


a=[]
for j in range(0,a.shape[1],1):
    soma=0
    for i in range(0,a.shape[0],1):
        soma = soma + a[i,j]
    
    a.append(soma)

o=[]
for i in range(0,a.shape[0],1):
    soma=0
    for j in range(0,a.shape[1],1):
        soma = soma + a[i,j]
    
    o.append(soma)

        
b=[]
for i in range(0,shape[0],1):
    soma=0
    for k in range(0,a.shape[1]-1,1):
        soma = soma + a[k]*(1/d[i,k])
        
    b.append(soma)
    
c=[]
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        valor= a[j]*(i/(d[i,j]**alfa))
        
    c.append(valor)
        
        
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        T[i.j]=o[i]*(c[j]/b[i])
        


#SAÍDA

somatorio = sum(sum(T))
print('%.4f' % somatorio)
