# -*- coding: utf-8
import numpy as np

def compara(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,1]
    for i in range(0,a.shape[0],1):
        somaL=0
        for j in range(0,a.shape[1],1):
            somaL=somaL+a[i,j]
        if somaL!=soma:
            return (False)
    for j in range(0,a.shape[1],1):
        somaC=0
        for i in range(0,a.shape[0],1):
            somaC=somaC+a[i,j]
        if somaC != soma:
            return (False)
    somaD=0
    for i in range(0,a.shape[0],1):
        somaD=somaD+a[i,i]
    if somaD != soma:
        return (False)
    for i in range(0,a.shape[0],1):
        somaC=0
        for j in range(a.shape[1],0,-1):
            somaC=somaC+a[i,j]
        if somaC != soma:
            return (False)
    return (True)
n=0
while n<2:
    n=int(input('Dimensão da matriz: '))

matriz=np.zeros((n,n))
for i in range(0,n,1):
    for j in range(0,n,1):
        matriz[i,j]=input('Digite o elemento a%d%d: ' %(i+1,j+1))

for i in range(0,matriz.shape[0],1):
    somaD=0
    somaD=somaD+matriz[i,i]
    print(somaD)
print(matriz)
if compara(matriz)==False:
    print('N')
else:
    print('S')

    