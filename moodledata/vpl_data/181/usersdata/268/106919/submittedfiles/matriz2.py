# -*- coding: utf-8 -*-
import numpy as np

n=int(input('Digite n : '))
a= np.zeros((n,n))
cont=0

for i in range ( 0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('Digite o termo : '))

def soma_linha (a,l):
    soma=0
    for j in range(0,a.shape[1],1):
        soma= soma + a[l,j]
    return(soma)
    
def soma_coluna  (a,c):
    for i in range(0,a.shape[0],1):
        soma= soma + a[i,c]
    return(soma)
    
def soma_diagonal_p (a):
    soma=0
    for i in range ( 0,a.shaoe[0],1):
         for j in range(0,a.shape[1],1):
                 if i==j:
                     soma= soma + a[i,j]
    return(soma)

def soma_diagonal_s (a):
    for i in range ( 0,a.shaoe[0],1):
        for j in range(0,a.shape[1],1):
            if (i+j) == n-1:
                soma = soma + a[i,j]
    return(soma)

soma=soma_linha(a,1)

for i in range (0,a.shape[0],1):
    if soma_linha(a,i)==soma:
        cont=cont+1
for i in range (0,a.shape[1],1):
    if soma_coluna(a,i)==soma:
        cont=cont+1
if soma_diagonal_p==soma:
    cont=cont+1
if soma_diagonal_s==soma:
    cont=cont+1
if cont ==n*2 + 2:
    print('S')
else:
    print('N')
    