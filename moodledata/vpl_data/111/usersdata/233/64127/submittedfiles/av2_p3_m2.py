# -*- coding: utf-8 -*-
import numpy as np
def somalinha(a,i):
    soma=0
    for j in range(a.shape[1]):
        soma=soma+a[i,j]
    return soma
def somacoluna(a,j):
    soma=0
    for i in range(a.shape[0]):
        soma=soma+a[i,j]
    return soma
def parametro(a):
    if somalinha(a,0)==somalinha(a,1) or somalinha(a,0)==somalinha(a,2):
        somabase=somalinha(a,0)
    else:
        somabase=somalinha(a,1)
    for i in range(a.shape[0]):
        if somalinha(a,i)!=somabase:
            indiceerrado_x=i
    for j in range(a.shape[1]):
        if somacoluna(a,j)!=somabase:
            indiceerradoy==j
    errado=a[indiceerradox,indiceerradoy]
    return errado
def diferença(a):
    if somalinha(a,0)==somalinha(a,1) or somlinha(a,0)==somalinha(a,2):
        somabase=somalinha(a,0)
    else:
        somabase=somalinha(a,1)
    for i in range(a.shape[0]):
        if somalinha(a,i)!=soma_base:
            somaerrada=somalinha(a,i)
    valor=somaerrada-somabase
    return valor
n=int(input('n '))
a=np.zeros((n,n))
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        a[i,j]=int(input('Digite o elemento: '))
print(int(parametro(a)-diferença(a)))
print(int(parametro(a)))

