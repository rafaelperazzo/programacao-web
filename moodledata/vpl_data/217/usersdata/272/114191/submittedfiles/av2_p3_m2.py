# -*- coding: utf-8 -*-
import numpy as np

n=int(input('Digite a ordem da matriz: '))
a=np.zeros( (n,n) )
for r in range (0,n,1):
    for s in range (0,n,1):
        a[r,s]=int(input('Digite um valor: '))

def soma_linha (matriz,n):
    soma=0
    for j in range (0,matriz.shape[1],1):
        soma=soma+matriz[n,j]
    return soma

def soma_coluna (matriz,n):
    soma=0
    for i in range (0,matriz.shape[0],1):
        soma=soma+matriz[i,n]
    return soma

linhas=[]
for k in range (0,n,1):
    soma_linhas=soma_linha(a,k)
    linhas.append(soma_linhas)

colunas=[]
for l in range (0,n,1):
    soma_colunas=soma_coluna(a,l)
    colunas.append(soma_colunas)

erro=0
i=0
j=0

for h in range(0,len(linhas),1):
    if h==(len(linhas)-1):
        if linhas[h]!=linhas[h-1] and linhas[h]!=linhas[h-2]:
            i=linhas.index(linhas[h])
            erro=linhas[h]
        if linhas[h]!=linhas[h-2] and linhas[h]==linhas[h-1]:
            i=linhas.index(linhas[h-2])
            erro=linhas[h-2]
        if colunas[h]!=colunas[h-1] and colunas[h]!=colunas[h-2]:
            j=colunas.index(colunas[h])
        if colunas[h]!=colunas[h-2] and colunas[h]==colunas[h-1]:
            j=colunas.index(colunas[h-2])
    
    if h==(len(linhas)-2):
        if linhas[h]!=linhas[h-1] and linhas[h]!=linhas[h+1]:
            i=linhas.index(linhas[h])
            erro=linhas[h]
        if linhas[h]!=linhas[h+1] and linhas[h]==linhas[h-1]:
            i=linhas.index(linhas[h+1])
            erro=linhas[h+1]
        if colunas[h]!=colunas[h-1] and colunas[h]!=colunas[h+1]:
            j=colunas.index(colunas[h])
        if colunas[h]!=colunas[h+1] and colunas[h]==colunas[h-1]:
            j=colunas.index(colunas[h+1])
        
    if h<(len(linhas)-2):
        if linhas[h]!=linhas[h+1] and linhas[h]!=linhas[h+2]:
            i=linhas.index(linhas[h])
            erro=linhas[h]
        if linhas[h]!=linhas[h+1] and linhas[h]==linhas[h+2]:
            i=linhas.index(linhas[h+1])
            erro=linhas[h+1]
        if colunas[h]!=colunas[h+1] and colunas[h]!=colunas[h+2]:
            j=colunas.index(colunas[h])
        if colunas[h]!=colunas[h+1] and colunas[h]==colunas[h+2]:
            j=colunas.index(colunas[h+1])
            
    if erro!=0 and i!=0 and j!=0:
        break


desvio=erro-linhas[h-1]
resposta=a[i,j]-desvio

print(resposta)
print(a[i,j])
