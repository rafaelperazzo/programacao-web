# -*- coding: utf-8 -*-
import numpy as np
def soma (a):
    b=[]
    for i in range (0,a.shape[0],1)
        soma=0
        for j in range (0,a.shape[1],1):
            if i!=j:
                soma=soma+a[i,j]
        b.append(soma)
    return(b)
def diagonal (a,b):
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if i==j:
                if a[i,j]<b[i]:
                    return False
    return True
n=int(input('tamanho da matriz:'))
a=np.zeros((n,n))
for i in range (0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('valor:'))
b=soma(a)
if diagonal (a,b):
    print ('SIM')
else:
    print ('NAO')
        

