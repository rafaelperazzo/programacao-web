# -*- coding: utf-8 -*-
import numpy as np
def somal(l,i):
    soma=0
    for j in range(0,l.shape[1],1):
        soma=soma+l[i,j]
    return (soma)
def somac(l,j):
    soma=0
    for i in range(0,l.shape[0],1):
        soma=soma+l[i,j]
    return (soma)
n=int(input('Tamanho: '))
g=int(input('Pl: '))
h=int(input('Pc: '))
l=np.zeros((n,n))
for i in range(0,l.shape[0],1):
    for j in range(0,l.shape[1],1):
        l[i,j]= int(input(' peso: '))
fim=somal(l,g)+somac(l,h)-(2*a[g,h])
print(fim)

