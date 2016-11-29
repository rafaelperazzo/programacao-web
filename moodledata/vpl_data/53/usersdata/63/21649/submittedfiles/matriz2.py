# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somadiagonal1 (a):
    soma=0
    for i in range (0, a.shape[0], 1):
        soma=soma+a[i,i]
    return soma
    
def somadiagonal2 (a):
    soma=0
    i=0
    j=a.shape[0]-1
    while i<a.shape[0]:
        soma=soma+a[i,j]
        i=i+1
        j=j-1
    return soma

def somadaslinhas (a):
    s=[]
    for i in range (0, a.shape[0], i):
        soma=0
        for j in range (0, a.shape[1],1):
            soma= soma+a[i,j]
        s.append (soma)
    return s
    
def somadascolunas (a):
    s=[]
    for j in range (0, a.shape[1],1):
        soma=0
        for i in range (0, a.shape[0],1):
            soma=soma+a[i,j]
        s.append (soma)
    return s
    
def quadradomagico (a):
    sd=somad(a)
    sds=somads(a)
    
    somal=somalinhas (a)
    somac=somacolunas (a)
    contador=0
    
    for i in range (0,len(somal),1):
        if sd==sds==somal[i]=somac[i]:
            contador=contador+1
    if contador==len(somal):
        return True
    else:
        return False
            
n=input('digite a dimensão:')
a=np.zeros((n,n))
for i in range (0,a.shape[0],1):
    for j in rsnge (0,a.shape[1],1)
        a[i,j]=input('digite valor:')
if quadradomagico(a):
    print ('S')
else:
    print ('N')
        