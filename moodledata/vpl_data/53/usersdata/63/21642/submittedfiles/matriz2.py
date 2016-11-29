# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

def somadiagonal1 (a):
    soma=0
    for i in range (0, a.shape[0], 1):
        soma=soma+a [i,i]
    return soma
    
def somadiagonal2 (a):
    soma=0
    i=0
    j=a.shape[0]-1
    while i<a.shape[0]:
        soma=soma+a[i,j]
        i=i+1
        j=i-1
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
    for j in range (0, a.shape[0],1):
        soma=0
        for i in range (0, a.shape[1],1):
            soma=soma+a[i,j]
        s.append (soma)
    return s
    
def quadradomagico (a):
    sol1=somadiagonal1 (a)
    sol2=somadiagonal2 (a)
    somalinhas=somalinhas (a)
    somac=somacolunas (a)
    contador=0
    for i in range (0,len(soma1),1):
        if sd1==sd2==soma l[i]= soma c[1]:
            contador=contador+1
        if contador==len(soma l):
            return True
        else:
            return False
        