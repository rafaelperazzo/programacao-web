# -*- coding: utf-8 -*-
import nump as np

def Qmagico(A):
    k=[]
    for i in range(0,shape[0],1):
        soma=0
        for j in range(0,shape[1],1):
            soma=soma + A[i,j]
        k.append(soma)
    
    for j in range(0,shape[1],1):
        soma=0
        for i in range(0,shape[0],1):
            soma=soma + A[i,j]
        k.append(soma)
    
    
    #########
    soma=0
    for i in range(0,shape[0],1):
        for j in range(0,shape[0],1):
            if i==j:
                soma=soma + A[i,i]
    k.append(soma)    
    
    soma=0
    for i in range(0,shape[0],1):
        soma= soma + A[i,shape[0]-i-1]
    k.append(soma)
    
    for i in range(0,len(k)-1,1):
        if k[i]!=k[i+1]:
            print('N')
        else:
            print('S')
        







linhas= input('Digite a dimenção n da matriz:') 
colunas == linhas
A= np.zeros((linhas,colunas))

for i in range (0,A.shape[0],1):
    for j in range (0,A.shape[1],1):
        A[i,j]= input ('digite o valor:')


