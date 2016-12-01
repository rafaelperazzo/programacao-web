# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 16:54:28 2016

@author: Jonathan Moreira
"""

from __future__ import division
import numpy as np

#FUNÇÕES
#Soma_linha
def Somalinha(a,linha):
    somalinha=0
    for j in range(0,a.shape[1],1):
        somalinha=somalinha+a[linha,j]
    return somalinha

#Soma_coluna
def Somacoluna(a,coluna):
    somacoluna=0
    for i in range(0,a.shape[0],1):
        somacoluna=somacoluna+a[i,coluna]

    return somacoluna

#peso
def peso(a,linha,coluna):
    somatotal=Somacoluna(a,coluna)+Somalinha(a,linha)-(2*a[linha,coluna])
    return somatotal
   
#PRINCIPAL
n=input('Digite a dimensão: ')
x=input('Digite a posição x: ')
y=input('Digite a posição y: ')

matriz=np.zeros((n,n))

for i in range(0,matriz.shape[0],1):
    for j in range(0,matriz.shape[1],1):
        matriz[i,j]=input('Digite o elemento da matriz: ')

print ('%.1d'%(peso(matriz,x,y)))