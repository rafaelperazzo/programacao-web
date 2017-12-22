# -*- coding: utf-8 -*-

def dominante(a):
    somaL=0
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[0],1):
            somaL=somaL+a[i,j]
        somaL=somaL-a[i,i]
        if somaL>a[i,i]:
            return False
    return True