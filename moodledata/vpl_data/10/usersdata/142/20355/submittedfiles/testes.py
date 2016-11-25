# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
#FUNÇÃO DE TESTE
def L1(a):
    linhadecima=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                linhadecima=i
        break
    return linhadecima

def L2(a):
    linhadebaixo=0
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[0],1):
            if a[i,j]==1:
                linhadebaixo=i
    return linhadebaixo

def C1(a):
    colunaesquerda=0
    for j in range(0,a.shape[1],1):
        for i in range(0,a.shape[1],1):
            if a[i,j]==1:
                colunaesquerda=j
                break
    return colunaesquerda

def C2(a):
    colunadireita=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if a[i,j]==1:
                colunadireita=j
                break
    return colunadireita
#PROGRAMA PRINCIPAL
linhas=input('Digite uma quantidade de linhas:')
colunas=input('Digite uma quantidade de colunas:')

a=np.zeros((linhas,colunas))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite um valor:')

print a[:,:]

print 'Linha de cima:%.d'%L1(a)

#print 'Linha de baixo:%.d'%L2(a)

#print 'Coluna esquerda:%.d'%C1(a)

#print 'Coluna direita:%.d'%C2(a)