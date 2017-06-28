# -*- coding: utf-8 -*-
import numpy as np

def Qmagico(a):
    k=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma + a[i,j]
        k.append(soma)
    
    for j in range(0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma=soma + a[i,j]
        k.append(soma)
    
    
    #########
    soma=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[0],1):
            if i==j:
                soma=soma + a[i,i]
    k.append(soma)    
    
    soma=0
    for i in range(0,A.shape[0],1):
        soma= soma + a[i,a.shape[0]-i-1]
    k.append(soma)
    
    cont=0
    for i in range(0,len(k)-1,1):
        if k[i]!=k[i+1]:
            cont=cont+1
    if cont==0:
        print('S')
    else:
        print('N')
    
        
n= int(input('Digite a dimenção n da matriz:')) 
a=np.zeros((n,n))

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]= input ('digite o valor:')


