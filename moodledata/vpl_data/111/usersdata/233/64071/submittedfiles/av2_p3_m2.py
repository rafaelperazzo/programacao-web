# -*- coding: utf-8 -*-
import numpy as np
def soma_linha(a,i):
    soma=0
    for j in range(a.shape[1]):
        soma=soma+a[i,j]
    return soma
def soma_coluna(a,j):
    soma=0
    for i in range(a.shape[0]):
        soma=soma+a[i,j]
    return soma
def laura(a):
    if soma_linha(a,0)==soma_linha(a,1) or soma_linha(a,0)==soma_linha(a,2):
        soma_base=soma_linha(a,0)
    else:
        soma_base=soma_linha(a,1)
    indice_errado_x=0
    for i in range(a.shape[0]):
        if soma_linha(a,i)!=soma_base:
            indice_errado_x=i
    indice_errado_y=0
    for j in range(a.shape[1]):
        if soma_coluna(a,j)!=soma_base:
            indice_errado_y==j
    errado=a[indice_errado_x,indice_errado_y]
    return errado
def diferença(a):
    if soma_linha(a,0)==soma_linha(a,1) or soma_linha(a,0)==soma_linha(a,2):
        soma_base=soma_linha(a,0)
    else:
        soma_base=soma_linha(a,1)
    for i in range(a.shape[0]):
        if soma(a,i)!=soma_base:
            soma_errada=soma_linha(a,i)
    valor=soma_errada-soma_base
    return valor
n=int(input('n '))
a=np.zeros((n,n))
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        a[i,j]=int(input('Digite o elemento: '))
print(int(laura(a)-diferença(a)))
print(int(laura(a)))

