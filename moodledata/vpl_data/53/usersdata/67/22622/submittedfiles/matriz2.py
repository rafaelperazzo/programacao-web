# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np



def somadiagonal1 (a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,i]
    return soma
def somadiagonal2 (a):
    soma=0
    for i in range (0,a.shape[0],1):
        soma=soma+a[i,a.shape[0]-i-1]
    return soma
def somalinhas (a):
    s=[]
    for i in range (0,a.shape[0],1):
        soma=0
        for j in range (0,a.shape[1],1):
            soma=soma+a[i,j]
        s.append(soma)
    return s

    
    
    
    
    
    
    

linhas=input("Digite a quantidade de linhas:")
colunas=input("Digite a quantidade de colunas:")
a=np.zeros((linhas,colunas))
for i in range (0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input("Digite um elemento para a:")
        

  

         

