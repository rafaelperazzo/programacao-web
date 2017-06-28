# -*- coding: utf-8 -*-
import numpy as np
def m(a):
    somaa=0
    somb=0
    somac=0
    for i in range(0,a.shape[0],1):
        somaa=somaa+a[i,0]
        somab=somab+a[i,1]
        somac=somac+a[i,2]
    if somaa==somab:
        m=somaa
    else:
        m=somac
    return m
def linhaincorreta(a,m):
    lista=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        lista.append(soma)
    for i in range(0,len(lista),1):
        if lista[i]!=m:
            return(i)
def colunaincorreta(a,m):
    lista=[]
    for j in range(0,a.shaoe[1],1):
        soma=0
        for i in range(a.shape[0],1):
            soma=soma+a[i,j
