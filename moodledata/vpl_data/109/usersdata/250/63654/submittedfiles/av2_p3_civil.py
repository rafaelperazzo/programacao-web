# -*- coding: utf-8 -*-
import numpy as np
def Slinha(a,li):
    soma=0
    for co in range (0,a.shape[1],1):
        soma=soma+a[li,co]
    return(soma)
def Scoluna(a,co):
    soma=0
    for li in range (0,a.shape[0],1):
        soma=soma+a[li,co]
    return(soma)
n=int(input('tamanho da matriz:'))
x=int(input('posição da linha:'))
y=int(input('posição da coluna:'))
a=np.zeros((n,n))
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=int(input('peso:'))
resul=Slinha(a,x)+Scoluna(a,y)-(2*a[x,y])
print(%dresul)
    
        
        

