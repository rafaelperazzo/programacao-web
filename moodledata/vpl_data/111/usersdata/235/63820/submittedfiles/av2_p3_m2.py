# -*- coding: utf-8 -*-
import numpy as np
m=int(input('digite o numero de linhas e colunas sendo l=c:'))
a=np.zeros((m,m))
for i in range(0,a.shape(0),1):
    for j in range(0,shape(1),1):
        a[i,j]=int(input('digite os valores para a matriz:'))
def quasemagica1(a):
    lista1=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        lista1.append(soma)
    return(lista1)
def quasemagica2(a):
    lista2=[]
    for j in range(0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
        lista2.append(soma)
    return(lista2)
a=quasemagica1
b=quasemagica2
def diferentes(a,b):
    for i in range(0,len(a),1):
        for j in range(0,len(b),1):
            if
        
    
    
            


