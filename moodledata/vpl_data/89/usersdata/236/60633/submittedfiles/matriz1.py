# -*- coding: utf-8 -*-
import numpy as np

def recorte(A):
    for i in range (0,A.shape[0],1):
        somalinha=0
        for j in range (0,A.shape[1],1):
            somalinha=somalinha+ a[i,j]
            if somalinha !=0:
                guardalinha==i
                break
            
    for i in range (0,A.shape[0],1):
        somalinha=0
        for j in range (0,A.shape[1],1):
            somalinha=somalinha+ a[i,j]
            if somalinha !=0:
                guardalinha==i
                break
            






linhas= int(input('Número de linhas:'))
colunas= int(input('Número de colunas:'))
A= np.zeros ((linhas,colunas))

for i in range (0,A.shape[0],1):
    for j in range (0,A.shape[1],1):
        A[i,j]= input('Digite o valor:')
        
print(A)
        
    

