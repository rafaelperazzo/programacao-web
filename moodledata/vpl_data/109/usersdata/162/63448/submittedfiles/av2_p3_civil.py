# -*- coding: utf-8 -*-
import numpy as np
def SomaLinha(a,i):
    soma1=0
    for j in range(0,a.shape[1],1):
        soma1=soma1+a[i,j]
    return(soma1)    

def SomaColuna(a,j):
    soma2=0
    for i in range(0,a.shape[0],1):
        soma2=soma2+a[i,j]
    return(soma2)

n=int(input('Digite n:'))
x=int(input('Digite x:'))
y=int(input('Digite y:'))

a=np.zeros((n,n))
for i in range(0,a.shape[1],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('Digite peso:'))
        
resultado=SomaLinha(a,x)+SomaColuna(a,y)-(2*a[x,y])

print(resultado)
