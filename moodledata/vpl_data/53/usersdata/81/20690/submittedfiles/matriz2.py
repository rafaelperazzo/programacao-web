# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somad(a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,i]
    return soma
    
def somad2(a):
    soma=0
    i=0
    j=a.shape[0]-1
    while i<a.shape[0]:
        soma=soma+a[i,j]
        i=i+1
        j=j-1
    return soma
    
def somal(a):
    t=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        t.append(soma)
    return t
    
def somac(a):
    t=[]
    for j in range(0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
        t.append(soma)
    return t
        
def quadradom(a):
    sd=somad(a)
    sds=somad2(a)
    
    sl=somal(a)
    sc=somac(a)
    
    cont=0
    for i in range(0,len(sl),1):
        if sd==sds==sl[i]==sc[i]:
            cont=cont+1
            
    if cont==len(sl):
        return True
    else:
        return False
        
n=input('Digite a dimensão da matriz:')
a=np.zeros((n,n))
for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input('Digite um valor para ser armazenado:')

if quadradom(a):
    print('S')
else:
    print('N')
        
