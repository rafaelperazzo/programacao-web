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
