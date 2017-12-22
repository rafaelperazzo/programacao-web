# -*- coding: utf-8 -*-

import numpy as np
def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desvio(lista):
    dn=0
    for i in range (0,len(lista),1):
        dn=dn+((lista[i] - (media(lista)))**2/(len(lista)-1))
        dn=dn**(0.5)
    return dn
    

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n=int(input('Digite o numero de elementos(coluna): '))
m=int(input('Digite o numero de listas (linhas): '))
mat=[]
for i in range(m):
    a=[]
    for j in range (n):
        a.append(float(input('Digite o numero abaixo: ')))
    mat.append(a)
for i in range (m):
    print ('%.2F' %media(mat[i]))
    print ('%.2F' %desvio(mat[i]))
    


