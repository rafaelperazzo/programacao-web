# -*- coding: utf-8 -*-
import numpy as np

linhas= int(input('Digite a quantidade de linhas:'))
colunas= int(input('Digite a quantidade de colunas:'))

a= np.zeros((linhas,colunas))

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]= int(input('Digite o elemento:'))
        
def soma_linha(b,l):
    soma=0
    for j in range(0,b.shape[1],1):
        soma=soma+b[l,j]
    return (soma)
    
def soma_coluna(b,c):
    soma=0
    for i in range(0,b.shape[0],1):
        soma=soma+b[i,c]
    return(soma)
    
for q in range (0,a.shape[0],1):
    if soma_linha(a,q)!=0:
        primeiro_1=q
        break 

for p in range (a.shape[0]-1,0,1):
    if soma_linha(a,p)!=0:
        ultimo_1=p
        break
    
for m in range (0,a.shape[1]-1,1):
    if soma_coluna(a,m)!=0:
        primeiro_c=m
        break
    
for n in range (a.shape[1]-1,0,1):
    if soma_coluna(a,n)!=0:
        ultimo_c=n
        break
    
b= np.zeros((p-primeiro_1+1,ultimo_c-primeiro_c+1))

for i in range (0,b.shape[0],1):
    for j in range (0,b.shape[1],1):
        b[i,j]=a[primeiro_1+i,primeiro_c+j]
        
print(b)
    

