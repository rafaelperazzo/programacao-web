# -*- coding: utf-8 -*-
import numpy as np

def linhas(a):
    linhas=[]
    for i in range (0,a.shape[0],1):
        soma=0
        for j in range (0,a.shape[1],1):
            soma=soma+a[i,j]
            linhas.append(soma)
    return (linhas)    
    

def colunas(a):
    colunas=[]
    for j in range (0,a.shape[1],1):
        soma=0
        for i in range (0,a.shape[0],1):
            soma=soma+a[i,j]
            colunas.append(soma)
    return (colunas)        

def termo(b):
    cont=0
    for i in range (0,len(b),1):
        for j in range (0,len(b),1):
            if b[i]==b[j]:
                cont=cont+1
        if cont==1:
            return i
            
def numero(lista,termo):
    for i in range (0,len(lista),1):
        if i!=termo:
            numero=a[termo]-a[i]
            return numero

n=int(input('Tamanho da matriz'))            
a=np.zeros((n,n))    
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=int(input('Termo:'))

linhas=linhas(a)
colunas=colunas(a)

l=termo(linhas)
c=termo(colunas)

k=a[l,c]
m=k-(numero(linhas,l))
print(k)
print(m)