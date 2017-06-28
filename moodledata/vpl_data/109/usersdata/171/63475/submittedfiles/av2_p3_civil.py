# -*- coding: utf-8 -*-
impo=rt numpy as np
def somatoriolinha(a,i):
    soma=0
    for j in range(0,a.shape[0],1):
        soma=soma+a[i,j]
    return(soma)
def somatoriocoluna(a,j):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,j]
    return(soma)
n=int(input('digite o numero de linhas e colunas:'))
p=int(input('digite a posicao da peca em relacao a linha:'))
pp=int(int(input('digite a posicao da peca em relacao a coluna:'))
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('escreva o peso:'))
c=somatoriolinha(a,p)+somatoriocoluna(a,pp)-(2*a[p,pp])

