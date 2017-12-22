# -*- coding: utf-8 -*-
#FUNÇÕES
def somalinha (A) :
    soma = 0
    for i in range (0,A.shape[0],1) :
        for j in range (0,A.shape[1],1) :
            soma = soma + A[i,j]
        return(soma)
def somacoluna (A) :
    soma = 0
    for j in range (0,A.shape[1],1) :
        for i in range (0,A.shape[0],1) :
            soma = soma + A[i,j]
        return(soma)

            
            


