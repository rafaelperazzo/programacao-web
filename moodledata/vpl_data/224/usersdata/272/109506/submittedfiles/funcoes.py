# -*- coding: utf-8 -*-


#escreva suas funcoes aqui

def o(A,n):
    soma=0
    for j in range (0,A.shape[1],1):
        soma=soma+A[n,j]
    return (soma)

def a(A,n):
    soma=0
    for i in range (0,A.shape[0],1):
        soma=soma+A[i,n]
    return (soma)


