# -*- coding: utf-8 -*-
def linha(a):
    listadassomas=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0.a.shape[1],1):
            soma=soma+a[i,j]
        listadassomas.append(soma)
    for j in range(0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
        listadassomas.append(soma)
    soma=0
    for i in range(0,a.shape[0],1):
        for j in range(0.a.shape[1],1):
            if i==j:
                soma=soma+a[i,j]
    listadassomas.append(soma)
    soma=0
    for i in range(a.shape[0]-1,-1,-1):
        for j in range(a.shape[1]-1,-1,-1):
            while a.shape[0]>-1:
                soma=soma+(a.shape[0]-1,a.shape[1]-1)
    listadassomas.append(soma)
    return(listadassomas)
a=l
        

