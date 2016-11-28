# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somadiagonal1 (lista):
    soma=0
    for i in range(0,lista.shape[0],1):
        soma=soma+lista[i,i]
    return soma

def somadiagonal2 (lista):
    soma=0
    for i in range(0,lista.shape[0],1):
        soma=soma+lista[i,lista.shape[0]-i-1]
    return soma


def somalinhas (lista):
    s=[]
    for i in range(0,lista.shape[0],1):
        soma=0
        for j in range(0,lista.shape[1],1):
            soma=soma+lista[i,j]
        s.append(soma)
    return s

def somacolunas (lista):
    s=[]
    for i in range(0,lista.shape[0],1):
        s.append(sum(lista[i,:]))
    return s
    
def quadrado (lista):
    sd1 = somadiagonal1 (lista)
    sd2 = somadiagonal2 (lista)
    sl = somalinhas (lista)
    sc = somacolunas (lista)
    
    cont=0
    for i in range(0,len(sl),1):
        if sd1==sd2==sl[i]==sc[i]:
            cont=cont+1
    if cont == len(sl):
        return True
    else:
        return False

n=input('digite n:')
a=np.zeros((n,n))

for i in range (0,a.shape[0],1):
    for j in range (0,a.shape[1],1):
        a[i,j]=input('digite elementos:')
        
if quadrado(a):
    print('S')
else:
    print('N')
    
    

