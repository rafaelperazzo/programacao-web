# -*- coding: utf-8 -*-
import numpy as np

n=int(input('Digite a ordem da matriz: '))
x=int(input('Digite a linha: '))
y=int(input('Digite a coluna: '))
a=np.zeros( (n,n) )

for i in range (0,n,1):
    for j in range (0,n,1):
        a[i,j]=int(input('Digite um valor: '))

def soma_l (matriz,i_linha):
    soma=0
    for j in range (0,matriz.shape[1],1):
        soma=soma+matriz[i_linha,j]
    return soma

def soma_c (matriz,j_coluna):
    soma=0
    for i in range (0,matriz.shape[0],1):
        soma=soma+matriz[i,j_coluna]
    return soma

resposta=soma_l(a,x)+soma_c(a,y)-(2*a[x,y])

print('%d' %resposta)

    