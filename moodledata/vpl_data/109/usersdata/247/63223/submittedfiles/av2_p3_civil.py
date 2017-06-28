# -*- coding: utf-8 -*-
def soma(a):
    soma=0 
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            if j==y:
                soma=soma+a[i,j]
            if i==x:
                soma=soma+a[i,j]
    soma=soma-a[x,y]
    return soma


