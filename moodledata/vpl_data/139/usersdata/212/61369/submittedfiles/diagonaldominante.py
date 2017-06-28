# -*- coding: utf-8 -*-

def somade (matriz):
    a=[]
    for i in range(0,matriz.shape[0],1):
        soma=0
        for j in range(0,matriz.shape[1],1):
            if i==j:
                soma=soma
            else:
                soma = soma + matriz[i,j]
        a.append(soma)
    return(a)
def somadp(matriz,lista):
    i=0
    j=0
    cont=0
    while i<matriz.shape[0]:
        if i==j:
            if lista[i]<matriz[i,j]:
                cont=cont+1
        i=i+1
        j=j+1
    return(cont)
n=int(input('digite o número de elementos de para as linhas e as colunas da matriz'))
import numpy as np
m=np.zeros((n,n))
for i in range(0,m.shape[0],1):
        soma=0
        for j in range(0,m.shape[1],1):
            m[i,j]=int(input('digite um elementos'))
se=somade(m)
teste=somadp(m,se)
if teste!=0:
    print('NÃO')
else:
    print('SIM')
            