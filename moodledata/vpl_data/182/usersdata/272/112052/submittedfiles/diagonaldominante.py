# -*- coding: utf-8 -*-
import numpy as np

def soma_linhas(a,n):
    soma=0
    for j in range (0,a.shape[1],1):
        soma=soma+a[n,j]
    return (soma)



n=int(input('Digite a ordem da matriz: '))
a=np.zeros( (n,n) )
for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=float(input('Digite um valor: '))

cont=0
for k in range (0,a.shape[0],1):
    for l in range (0,a.shape[1],1):
        if k==l:
            if (a[k,l]>(soma_linhas(a,k)-a[k,l])):
                cont=cont+1

if cont==a.shape[0]:
    print('SIM')
else:
    print('NAO')

