# -*- coding: utf-8 -*-
import numpy as np
m=int(input('digite a dimensao da matriz: '))
g=int(input('digite a linha: '))
h=int(input('digite a coluna: '))
a=np.zeros((m,m))
for i in range(0,m,1):
    for j in range(0,m,1):
        a[i,j]=int(input('digite o elemento: '))
def soma_linha(a,b):
    soma=0
    for j in range (0,a.shape[1],1):
        soma=soma+a[b,j]
    return(soma)
def soma_coluna(c,d):
    soma=0
    for i in range(0,c.shape[0],1):
        soma=soma+c[i,d]
    retrn(soma)
resultado=soma_linha(a,g)+soma_coluna(a,h)-(2*a[g,h])
print('%d' %resultado)
