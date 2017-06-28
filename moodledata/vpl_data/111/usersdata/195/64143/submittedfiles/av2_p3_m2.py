# -*- coding: utf-8 -*-
import numpy as np
def somaL(x,i):
    soma=0
    for j in range(0,x.shape[1],1):
        soma=soma+x[i,j]
    return (soma)
def somaC (x,j):
    soma=0
    for i in range(0,x.shape[0],1):
        soma=soma+x[i,j]
    return (soma)
def L(x):
    if somaL(x,0)==somaL(x,1) or somaL(x,0)==somaL(x,2):
        somaY=somaL(x,0)
    else:
        somaY=somaL(x,1)
    for i in range(0,x.shape[0],1):
        if somaL(x,i)!=somaY:
            termoerradoz=i
    for j in range(0,x.shape[1],1):
        if somaC(x,j)!=somaY:
            termoerradok=j
    E=x[termoerradoz,termoerradok]
    return (E)
def diferente(x):
    if somaL(x,0)==somaL(x,1) or somaL(x,0)==somaL(x,2):
        somaY=somaL(x,0)
    else:
        somaY=SomaL(x,1)
    for i in range(0,x.shape[0],1):
        if somaL(x,i)!=somaY:
            somaerrada=somaL(x,i)
    v=somaerrada-somaY
    return(v)
f=int(input('f:'))
x=np.zeros((f,f))
for i in range(0,x.shape[0],1):
    for j in range(0,x.shape[1],1):
        x[i,j]=int(input('valor:'))
print(int(L(x)-diferente(x)))
print(int(L(x)))


