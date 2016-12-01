# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np



def somadiagonal1 (a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,i]
    return soma


linhas=input("Digite a quantidade de linhas:")
colunas=input("Digite a quantidade de colunas:")
a=np.zeros((linhas,colunas))
for i in range (0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input("Digite um elemento para a:")
        

  

         

