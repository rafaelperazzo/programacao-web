# -*- coding: utf-8 -*-
import numpy as np
n=int(input('Digite o tamanho da Matriz:'))
a=np.zeros((n,n))
if n>=3:
    for i in range(0,a.shape[0],1):
        for j in range(0,a.shape[1],1):
            a[i,j]=int(input('Digite um valor:'))
def m(a):
    soma=0
    soma1=0
    for i in range(0,a.shape[0],1):
        som=soma+a[i,0]
        soma1=soma1+som
    soma2=0
    soma3=0
    for j in range(0,a.shape[1],1):
        som=soma+a[0,j]
        soma3=soma3+som
    if soma1==soma3:
        print(soma3)