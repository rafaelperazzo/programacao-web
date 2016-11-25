# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

#Funções
def linha(a):
    soma = 0
    b = []
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            soma = soma +a[i,j]
            b[i] = b.append(soma)
    return b
    
def coluna(a):
    Soma = 0
    b = []
    for j in range (0,a.shape[1],1):
        for i in range (0,a.shape[0],1):
            Soma = Soma +a[i,j]
            b[j] = b.append(Soma)
    return b
    
def diagonal1(a):
    Soma = 0
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if i==j:
                Soma = Soma + a[i,j]
    return Soma
    
def diagonal2(a):
    Soma = 0
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if (i+j) == (a.shape[0]-1):
                Soma = Soma +a[i,j]
    return Soma
    
def magica(a):
    contador = 0
    if diagonal1(a) == diagonal2(a):
        Soma = diagonal1(a)
        b = linha(a)
        c = coluna(a)
        for i in range (0,a.shape[0],1):
            if b[i]!=Soma:
                contador = contador +1
        for i in range (0,a.shape[1],1):
            if c[i]!=Soma:
                contador = contador +1
        if contador ==0:
            return True
        elif contador!=0:
            return False
    else:
        return False
        
#CODIGO PRINCIPAL   
linhas = input ('Digite a quantidade de linhas:')
colunas = input ('Digite a quantidade de colunas:')
a= np.zeros ((linhas,colunas))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j] = input ('Digite um número:')
     
print (coluna(a))
print (linha(a))
print diagonal1(a)
print diagonal2(a)
if magica(a):
    print ('S')
else:
    print ('N')
