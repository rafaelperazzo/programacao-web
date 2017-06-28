# -*- coding: utf-8 -*-
def somatorio(a):
    somatorio=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            if i!=j:
                soma=soma+a[i,j]
        somatorio.append(soma)
    return somatorio
def domdiag(a,b):
    soma=0
    for i in range(0,a.shape[0],1):
        for i in range(0,a.shape[1],1):
            if a[i,i]>=b[i]:
                soma=soma+1
            if soma==0:
                return True
            else:
                return False

n=int(input('Digite o tamanho da matriz:'))
import numpy as np
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('Digite um valor para a matriz:'))

if domdiag(a,somatorio(a)):
    print('SIM')
else:
    print('NAO')