# -*- coding: utf-8 -*-
import numpy as np

linhas= int(input('Digite linhas :' ))
colunas= int(input('Digite colunas: '))

a= np.zeros((linhas,colunas))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j] = int(input('Digite o elemento:'))

def soma_linha (b,l):
    soma=0
    for j in range (0,b.shape[1],1):
        soma= soma + a[l,j]
    return(soma)
    
def soma_coluna (b,c):
    soma=0
    for i in range (0,b.shape[0],1):
        soma= soma + a[i,c]
    return(soma)    

#limites das linhas
for q  in range (0,a.shape[0],1):
    if soma_linha(a,q) != 0:
        primeiro_l=q
        
for p in range (shape[0],0,-1):
    if soma_linha(a,p) != 0:
        ultimo_l=p
        
#limites das colunas 
for m  in range (0,a.shape[1],1):
    if soma_coluna(a,m) != 0:
        primeiro_c=m
        
for n in range (shape[1],0,-1):
    if soma_coluna(a,n) != 0:
        ultimo_c=n

b=np.zeros(ultimo_l-primeiro_l +1,ultimo_c-primeiro_c +1)
print(b)