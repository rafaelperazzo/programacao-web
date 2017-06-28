# -*- coding: utf-8 -*-
import numpy as np

def somaLinhas(a):
    b=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        b.append(soma)
    return(b)
    
def semRepeticao(b):
    c=[]
    for i in range(0,len(b),1):
        if b[i] not in c:
            c.append(b[i])
    return(c)
    
def vezes(x,b):
    cont=0
    for i in range(0,len(b),1):
        if b[i]==x:
            cont=cont+1
    return(cont)
    
def somaErrada(c,b):
    somaE=c[0]
    for i in range(1,len(c),1):
        if vezes(c[i],b)<vezes(c[i-1],b):
            somaE=c[i]
    return(somaE)
    
def somaCerta(c,b):
    somaC=c[0]
    for i in range(1,len(c),1):
        if vezes(c[i],b)>vezes(c[i-1],b):
            somaC=c[i]
    return(somaC)    

n=int(input('Digite a ordem da matriz: '))
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('Digite o valor do termo da matriz: '))

b=somaLinhas(a)
c=semRepeticao(b)
d=somaErrada(c,b)
e=somaCerta(c,b)
diferença=abs(d-e) 

    
    
    
