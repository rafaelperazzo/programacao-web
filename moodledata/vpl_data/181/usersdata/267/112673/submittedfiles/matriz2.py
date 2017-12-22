# -*- coding: utf-8 -*-

soma=0
for i in range(0,n,1):
    soma=soma+a[i,1]
    
def compara(a):
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
            
    for i in range(0,a.shape[0],1):
        somaD=somaD+a[i,i]
    if somaD!=soma:
        return (False)
    return (True)
    
    for i in range(0,a.shape[0],1):
        somaC=0
        for j in range(a.shape[1],0,-1):
            somaC=somaC+a[i,j]
        if somaC != soma:
            return (False)

n=int(input('Dimensão da matriz: '))

    