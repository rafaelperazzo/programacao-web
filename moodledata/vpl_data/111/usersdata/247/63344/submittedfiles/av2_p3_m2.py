# -*- coding: utf-8 -*-
def soma(a):
    b=[ ]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        b.append(soma)
    return (b)
def
