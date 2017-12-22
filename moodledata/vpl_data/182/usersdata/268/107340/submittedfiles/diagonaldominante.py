# -*- coding: utf-8 -*-
import numpy as np

n=int(input('Digite a ordem da matriz : '))
a=np.zeros((n,n))
cont= 0

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]= int(input('Digite o termo: '))

def soma_linha (b,l):
    soma=0
    for j in range (0,b.shape[1],1):
        soma= soma + b[l,j]
    return(soma)

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        if i==j:
            if a[i,j]> soma_linha(a,i) - a[i,j]:
                cont=cont+1
            else:
                cont=0
                break
if cont== n:
    print('SIM')
else:
    print('NAO')
            

