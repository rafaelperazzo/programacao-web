# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

#escreva suas funcoes aqui
def somColunas(a):
    b=[]
    for j in range(0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma=soma +a[i,j]
        b.append(soma)
    return b    
        
def somLinhas(a):
    b=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma +a[i,j]
        b.append(soma)
    return b 

def somatorio(a,d):
    soma=0
    for i in range (0,d.shape[0],1):
        for k in range (0,d.shape[1],1):
            soma= soma + (a[k]/d[i,k])
    return soma

def matriz(o,a,d,alpha,t):
    for i in range(0,t.shape[0],1):
        for j in range(0,t.shape[1],1):
            soma = 0 #<------------------------------
            for k in range(0,a.shape[0],1): # <------------------------------
                soma = soma + (a[k]/d[i,k]) # <------------------------------
            t[i,j]= o[i]*((a[j] * (1/(d[i,j]**alpha)))/soma) # <------------------------------
    return t
