# -*- coding: utf-8 -*-
import numpy as np

def recorte(a):
    #eliminação das primeiras linhas zeradas e armazenamento do indice da linha não zerada
    guardalinhai=0
    for i in range (0,a.shape[0],1):
        somalinha=0
        for j in range (0,a.shape[1],1):
            somalinha=somalinha+ a[i,j]
        if somalinha !=0:
            guardalinhai = i
            #print(guardalinhai)
            break
    #eliminação das ultimas linhas zeradas e armazenamento do indice da linha não zerada       
    guardalinhaf=0
    for i in range (a.shape[0]-1,-1,-1):
        somalinha=0
        for j in range (0,a.shape[1],1):
            somalinha=somalinha+ a[i,j]
        if somalinha !=0:
            guardalinhaf = i
            #print(guardalinhaf)
            break    
    #eliminação das primeiras colunas zeradas e armazenamento do indice coluna não zerada
    guardacolunai=0
    for j in range (0,a.shape[1],1):
        somacoluna=0
        for i in range (0,a.shape[0],1):
            somacoluna=somacoluna+ a[i,j]
        if somacoluna !=0:
            guardacolunai = j
            #print(guardacolunai)
            break
    #eliminação das ultimas colunas zeradas e armazenamento do indice da coluna não zerada
    guardacolunaf=0
    for j in range (a.shape[1]-1,-1,-1):
        somacoluna=0
        for i in range (0,a.shape[0],1):
            somacoluna=somacoluna+ a[i,j]
        if somacoluna !=0:
            guardacolunaf = j
            #print(guardacolunaf)
            break
            
    printar a partir da e até a linha guardada / coluna
    for i in range (guardalinhai,guardalinhaf+1,1):
        for j in range (guardacolunai,guardacolunaf+1,1):
    #print(a[guardalinhai:guardalinhaf,guardacolunai:guardacolunaf])
            


linhas= int(input('Número de linhas:'))
colunas= int(input('Número de colunas:'))
a=np.zeros ((linhas,colunas))

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]= input('Digite o valor:')


        
recorte(a)

        
    

