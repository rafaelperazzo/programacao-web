# -*- coding: utf-8 -*-
import numpy as np

def recorte(a):
    for i in range (0,a.shape[0],1):
        somalinha=0
        for j in range (0,a.shape[1],1):
            somalinha=somalinha+ a[i,j]
            if somalinha !=0:
                guardalinhai == i
                break
            
    for i in range (a.shape[0]-1,-1,1):
        somalinha=0
        for j in range (0,a.shape[1],1):
            somalinha=somalinha+ a[i,j]
            if somalinha !=0:
                guardalinhaf == i
                break
    
    for j in range (0,a.shape[1],1):
        somacoluna=0
        for i in range (0,a.shape[0],1):
            somacoluna=somacoluna+ a[i,j]
            if somacoluna !=0:
                guardacolunai == j
                break
    
    for j in range (a.shape[1]-1,-1,1):
        somacoluna=0
        for i in range (0,a.shape[0],1):
            somacoluna=somacoluna+ a[i,j]
            if somacoluna !=0:
                guardacolunaf == j
                break
            
    #printar a partir e até a linha guardada / coluna


linhas= int(input('Número de linhas:'))
colunas= int(input('Número de colunas:'))
a=np.zeros ((linhas,colunas))

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]= input('Digite o valor:')
        
recorte (a)

        
    

