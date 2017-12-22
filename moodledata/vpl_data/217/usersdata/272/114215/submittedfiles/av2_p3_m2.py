# -*- coding: utf-8 -*-
import numpy as np

n=int(input('Digite a ordem da matriz: '))
a=np.zeros( (n,n) )
for i in range (0,n,1):
    for j in range (0,n,1):
        a[i,j]=int(input('Digite um valor: '))

def soma_linha(matriz,l):
    soma=0
    for j in range (0,matriz.shape[1],1):
        soma=soma+matriz[l,j]
    return soma

def soma_coluna(matriz,c):
    soma=0
    for i in range (0,matriz.shape[0],1):
        soma=soma+matriz[i,c]
    return soma

soma=0
soma_linhas=[]
for i in range (0,a.shape[0],1):
    soma=soma_linha(a,i)
    soma_linhas.append(soma)

soma=0
soma_colunas=[]
for j in range (0,a.shape[1],1):
    soma=soma_coluna(a,j)
    soma_colunas.append(soma)

z=[]
e=[]

for i in range (0,1,1):
    for j in range (0,len(soma_linhas),1):
        if soma_linhas[i]==soma_linhas[j]:
            z.append(j)
        if soma_linhas[i]!=soma-linhas[j]:
            e.append(j)

if len(z)>len(e):
    linha_n=e[0]
else:
    linha_n=z[0]

s=[]
p=[]

for i in range (0,1,1):
    for j in range (0,len(soma_colunas),1):
        if soma_colunas[i]==soma_colunas[j]:
            s.append(j)
        if soma_colunas[i]!=soma_colunas[j]:
            p.append(j)

if len(s)>len(p):
    coluna_n=p[0]
else:
    coluna_n=s[0]

valor=a[linha_n,coluna_n]

if linha_n==0:
    soma_f=soma_linha(a,1)
else:
    soma_f=soma_linha(a,(linha_n)-1)

soma_n=soma_linha(a,linha_n)

desvio=soma_n-soma_f
resposta=a[linha_n,coluna_n]-desvio

print('%d' %resposta)
print('%d' %a[linha_n,coluna_n])
            

