# -*- coding: utf-8 -*-
import numpy as np

def DIAGONALDOMINANTE (a):
    for i in range(0,shape[0],1):
        LINHA=0
        for j in range(0,shape[1],1):
            LINHA=LINHA+ a[i,j]
            k= LINHA-A[i,i]
            cont=0
            if A[i,i]>k:
                cont=cont+1
    if cont==n:
        print('S')
    else:
        print('N')
            
            
    






linhas= int('Digite a Dimensão da matriz:')
colunas==linhas
a=np.zeros ((linhas,colunas))

for i in range(0,shape[0],1):
    for j in range(0,shape[1],1):
        a[i,j]=input('Digite o valor:')
        

    