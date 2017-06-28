# -*- coding: utf-8 -*-
import numpy as np 
def magica(a):
    s1=0
    s2=0
    s3=0
    for i in range (0,a.shape[0],1):
        s3=s3+a[i,2]
        s2=s2+a[i,1]
        s1=s1+a[i,0]
    if s1==s2:
        f=s1
    else:
        f=s3
    return f
def le (a,f):
    lista=[]
    for i in range (0,a.shape[0],1):
        soma=0
        for j in range (0,a.shape[1],1):
            soma=soma+a[i,j]
        lista.append(soma)
    for i in range (0,len(lista),1):
        soma=0
        if lista[i]!=f:
            return i
def ce (a,f):
    lista=[]
    for i in range (0,a.shape[1],1):
        soma=soma+a[j,i]
    lista.append(soma)
for j in range (0,len(lista),1):
    if lista[i]!=f:
        j=i
    return j
def vc (a,x,y,f):
    s1=0s2=0
    for i in range 
    
    
    

N=int(input('digite a dimensão da matriz:'))
a=np.zeros( (N,N) )
for i in range (0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=int(input('digite o elemento da matriz:'))
               
    
