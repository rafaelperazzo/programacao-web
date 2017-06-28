# -*- coding: utf-8 -*-
import numpy as np

def linhas(b):
    linhas=[]
    for i in range (0,b.shape[0],1):
        soma=0
        for j in range (0,b.shape[1],1):
            soma=soma+b[i,j]
        linhas.append(soma)
    return (linhas)
    
def colunas(b):
    colunas=[]
    for j in range (0,b.shape[1],1):
        soma=0
        for i in range (0,b.shape[0],1):
            soma=soma+b[i,j]
        colunas.append(soma)
    return (colunas)
    
def termo(t):
    for i in range (0,len(t),1):
        cont=0
        for j in range (0,len(t),1):
            if t[i]==t[j]:
                cont=cont+1
        if cont==1:
            return i
            
def numero(lista,termo):
    for i in range (0,len(lista),1):
        if i!=termo:
            numero=lista[termo]-lista[i]
            return numero
            
n=int(input('tamanho da matriz:'))
b=np.zeros((n,n))
for i in range(0,b.shape[0],1):
    for j in range(0,b.shape[1],1):
        b[i,j]=int(input('termo:'))
        
linhas=linhas(b)
colunas=colunas(b)

l=termo(linhas)
c=termo(colunas)

k=b[l,c]
m=k-(numero(linhas,1))
print('%.d'%m)
print('%.d'%k)