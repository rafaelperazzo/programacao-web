# -*- coding: utf-8 -*-
import numpy as np

def recorte(A):
    for i in range (0,A.shape[0],1):
        somalinha=0
        for j in range (0,A.shape[1],1):
            somalinha=somalinha+ a[i,j]
            if somalinha !=0:
                guardalinhai == i
                break
            
    for i in range (A.shape[0]-1,-1,1):
        somalinha=0
        for j in range (0,A.shape[1],1):
            somalinha=somalinha+ a[i,j]
            if somalinha !=0:
                guardalinhaf == i
                break
    
    for j in range (0,A.shape[1],1):
        somacoluna=0
        for i in range (0,A.shape[0],1):
            somacoluna=somacoluna+ a[i,j]
            if somacoluna !=0:
                guardacolunai == j
                break
    
    for j in range (A.shape[1]-1,-1,1):
        somacoluna=0
        for i in range (0,A.shape[0],1):
            somacoluna=somacoluna+ a[i,j]
            if somacoluna !=0:
                guardacolunaf == j
                break


linhas= int(input('Número de linhas:'))
colunas= int(input('Número de colunas:'))
A= np.zeros ((linhas,colunas))

for i in range (0,A.shape[0],1):
    for j in range (0,A.shape[1],1):
        A[i,j]= input('Digite o valor:')
        
print(A)
        
    

