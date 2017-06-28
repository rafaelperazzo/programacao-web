# -*- coding: utf-8 -*-
import numpy as np

def DIAGONALDOMINANTE (a):
    cont=0
    for i in range(0,a.shape[0],1):
        LINHA=0
        for j in range(0,a.shape[1],1):
            LINHA=LINHA+ a[i,j]
            k= LINHA-a[i,i]
            
            if a[i,i]>k:
                cont=cont+1
    if cont==n:
        print('S')
    else:
        print('N')
            
n= int(input('Digite a Dimensão da matriz:'))
a=np.zeros ((n,n))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite o valor:')

DIAGONALDOMINANTE(a)        

    