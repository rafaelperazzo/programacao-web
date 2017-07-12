# -*- coding: utf-8 -*-
import numpy as np
def r(a):
    soma=0
    soma1=0
    soma2=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,0]
        soma1=soma1+a[i,1]
        soma2=soma2+a[i,2]
    if soma==soma1:
        r=soma
    else:
        r=soma2
    return r
    
def linhaErrada(a,p):
    b=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
            b.append(soma)
    for i in range(0,len(b),1):
        if b[i]!=p:
            return i
            
def colunaErrada(a,v):
    c=[]
    for j in range(0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
            c.append(soma)
    for i in range(0,len(c),1):
        if c[i]!=r:
            j=i
        return j
            
def valorCerto(a,x,y,r):
    soma=0
    soma1=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,y]
    for j in range(0,a.shape[1],1):
        soma1=soma1+a[x,j]
        w=soma+soma1-(2*a[x,y])
        valor=r-(w/2)
        return valor
        
n=int(input('Informe o valor da matriz:'))

matriz=np.zeros((n,n))
for i in range(0, matriz.shape[0],1):
    for j in range(0,matriz.shape[1],1):
        matriz[i,j]=int(input('Digite um valor:'))
r=r(matriz)
x=linhaErrada(matriz,r)
y=colunaErrada(matriz,r)
resultado=valorCerto(matriz,x,y,r)
print('%.f' %matriz[x,y])
print('%.f' %resultado)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    

