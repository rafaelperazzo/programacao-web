# -*- coding: utf-8 -*-
import numpy as np
def m(a):
    doma1=o
    soma2=0
    soma3=0
    for i in range(0,a.shape[0],1):
        soma1=soma1+a[i,0]
        soma2=soma2+a[i,1]
        soma3=soma3+a[i,2]
    if soma1==soma2:
        m=soma1
    else:
        m=soma3
    return m
    
def lErrada(a,m):
    lista=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        lista.append(soma)
    for i in range(0,len(lista),1):
        if lista[i]!=m:
            return i
            
def cErrada(a,m):
    lista=[]
    for j in range(0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
        lista.append(soma)
    for i in range(0,len(lista,1):
        if lista [i]!=m:
            j=i
        return j
        
def vCerto(a,x,y,m):
    soma1=0
    soma2=0
    for i in range(0,a.shape[0],1):
        soma1=soma1+a[i,y]
    for j in range(0,a.shape[1],1):
        soma2=soma2+a[x,j]
    z=soma1+soma2-(2*a[x,y])
    valor=m-(z/2)
    return valor
    
            


