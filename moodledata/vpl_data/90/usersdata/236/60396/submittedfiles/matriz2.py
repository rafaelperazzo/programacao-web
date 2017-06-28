# -*- coding: utf-8 -*-
import numpy as np

def Qmagico(A):
    k=[]
    for i in range(0,A.shape[0],1):
        soma=0
        for j in range(0,A.shape[1],1):
            soma=soma + A[i,j]
        k.append(soma)
    
    for j in range(0,A.shape[1],1):
        soma=0
        for i in range(0,A.shape[0],1):
            soma=soma + A[i,j]
        k.append(soma)
    
    
    #########
    soma=0
    for i in range(0,A.shape[0],1):
        for j in range(0,A.shape[0],1):
            if i==j:
                soma=soma + A[i,i]
    k.append(soma)    
    
    soma=0
    for i in range(0,A.shape[0],1):
        soma= soma + A[i,A.shape[0]-i-1]
    k.append(soma)
    
    cont=0
    for i in range(0,len(k)-1,1):
        if k[i]!=k[i+1]:
            cont=cont+1
    if cont==0:
        print('S')
    else:
        print('N')
    
        
linha= input('Digite a dimenção n da matriz:') 
coluna==linha
a=np.zeros((linha,coluna))

for i in range (0,A.shape[0],1):
    for j in range (0,A.shape[1],1):
        A[i,j]= input ('digite o valor:')


