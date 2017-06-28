# -*- coding: utf-8 -*-

def linha (n,m):
    soma=0
    for l in range(0,m.shape[1],1):
        soma=soma+m[n,l]
    return (soma)
    
def coluna (n,m):
    soma=0
    for l in range(0,m.shape[0],1):
        soma=soma+m[l,n]
    return (soma)
    
import numpy as wm
d=int(input('Dimensão da matriz:'))
f=int(input('f:'))
g=int(input('g:'))
e=wm.zeros((d,d))
print(e)

for i in range(0,e.shape[0],1):
    for j in range(0,e.shape[1],1):
        e[i,j]=int(input('termos:'))
numero=(linha(f,e)+coluna(g,e)-(2*e[f,g]))
print('%.d' %numero)


