# -*- coding: utf-8 -*-
import numpy as np

dimensao=int(input('Digite a dimensão : '))
a= np.zeros((dimensao,dimensao))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('Digite o elemento: '))



#Funções
def soma_linha(matriz,linha):
    soma=0
    for j in range(0,matriz.shape[1],1):
        soma= soma + matriz[linha,j]
    return(soma)
    


def soma_coluna(matriz,coluna):
    soma=0
    for i in range(0,matriz.shape[0],1):
        soma= soma + matriz[i,coluna]
    return(soma)



 #Criação das listas-apoio  
soma=0
soma_linhas=[]
for i in range(0,a.shape[0],1):
    soma= soma_linha(a,i)
    soma_linhas.append(soma)
 
soma=0
soma_colunas=[]
for j in range(0,a.shape[1],1):
    soma= soma_coluna(a,j)
    soma_colunas.append(soma)
  
#Encontrar o valor critico 
#LINHAS
x=[]
y=[]
for i in range(0,1,1):
    for j in range(0,len(soma_linhas),1):
        if soma_linhas[i]==soma_linhas[j]:
            x.append(j)
        if soma_linhas[i] != soma_linhas[j]:
            y.append(j)
    
if len(x)>len(y):
    linha_QM=y[0]
else:
    linha_QM=x[0]
print(linha_QM)
#COLUNAS

m=[]
n=[]
for i in range(0,1,1):
    for j in range(0,len(soma_colunas),1):
        if soma_colunas[i]==soma_colunas[j]:
            m.append(j)
        if soma_colunas[i] != soma_colunas[j]:
            n.append(j)
    
if len(m)>len(n):
    coluna_QM=n[0]
else:
    coluna_QM=m[0]
print(coluna_QM)
#Valor critico

QM=a[linha_QM,coluna_QM]
if linha_QM==0:
    soma_base=soma_linha(a,1)
else:
    soma_base=soma_linha(a,linha_QM -1)

soma_QM= soma_linha(a,linha_QM)

#Determinaoção do novo valor

subtracao= soma_QM - soma_base
resultado= a[linha_QM,coluna_QM] - subtracao


print(resultado)
print(a[linha_QM,coluna_QM])
    
    

