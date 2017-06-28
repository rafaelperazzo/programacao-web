# -*- coding: utf-8 -*-
import numpy as np
def M(matriza):
    M=0
    cont=0
    soma=0
    parametro=0
    for i in range(matriza.shape[0]):
        for j in range(matriza.shape[1]):
            soma=soma+matriza[i,j]
        if soma==parametro:
            M=soma
            cont=cont+1
            break
        parametro=soma
        soma=0
    if cont==0:
        soma=0
        cont=0
        for i in range(1,matriza.shape[0]):
            for j in range(matriza.shape[1]):
                soma=soma+matriza[i,j]
            if soma==parametro:
                M=soma
                cont=cont+1
                break
            parametro=soma
            soma=0
    return M

n=int(input('Digite n:'))
matriza=np.zeros((n,n))
for i in range(matriza.shape[0]):
    for j in range(matriza.shape[1]):
        matriza[i,j]=int(input('Digite um número da matriza:'))
        
somaLinha=M(matriza)        