# -*- coding: utf-8 -*-
def somatórioDaLinha(A,i):
    soma=0
    for j in range(0,A.shape[1],1):
        soma=soma+A[i,j]
    return (soma)
def somatórioDaColuna(A,j):
    soma2=0
    for i in range(0,A.shape[0],1):
        soma2=soma2+1
    return(soma2)
n=int(input('Digite a dimensão da Matriz A:  '))

