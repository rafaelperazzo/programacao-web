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
    
    
    
def linhaErro(d,a):    
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        if soma==d:
            return(i)
            
def colunaErro(d,a):    
    for j in range(0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
        if soma==d:
            return(j)            

def numeroTrocado(diferenca,errado,d,e):
    trocado=0
    if d>e:
        trocado=errado-diferenca
    else:
        trocado=errado+diferenca
    return(trocado)
    
n=int(input('Digite a ordem da matriz: '))
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('Digite o valor do termo da matriz: '))

b=somaLinhas(a)
c=semRepeticao(b)
d=somaErrada(c,b)
e=somaCerta(c,b)
diferenca=abs(d-e)
x=linhaErro(d,a)
y=colunaErro(d,a)
errado=a[x,y]
trocado=numeroTrocado(diferenca,errado,d,e)
print(trocado)
print(errado)




    
    
    
