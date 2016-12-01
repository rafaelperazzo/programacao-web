# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

d=input("Insira a Dimensão da Matriz: ")
a=np.zeros((d,d))
x=input("Insira a Linha da Posição: ")
y=input("Insira a Coluna da Posição: ")

for i in range(0,a.shape[0],1): #Entrada da Matriz
    for j in range(0,a.shape[1],1):
        a[i,j]=input("Insira o Elemento: ")

def peso(matriz,i,j):
    linhas=sum(matriz[i,:])-matriz[i,j]
    colunas=sum(matriz[:,j])-matriz[i,j]
    peso=linhas+colunas
    return peso

print peso(a,x,y)