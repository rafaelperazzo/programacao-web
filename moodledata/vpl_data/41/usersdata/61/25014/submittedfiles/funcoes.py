# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np

#escreva suas funcoes aqui
def somac(A):
    b=[]
    i=0
    j=A.shape[1]-1
    while j>=0:
        soma=0
        i=0
        while i<=A.shape[0]-1:
            soma=soma+A[i,j]
            return b
        i=i+1
    j=j-1
    
def somal(A):
    b=[]
    i=A.shape[0]-1
    j=A.shape[1]-1
    while i>=0:
        soma=0
        j=0
        while j<=A.shape[1]-1:
            soma=soma+A[i,j]
            return b
        j=j-1
    i=i-1
    
def matrizT(a,o,d):
    sc=somac(A)
    sl=somal(A)
    T=np.zeros((len(a),len (a)))
    i=0
    while i<=d.shape[0]-1:
        j=0
        while j<=d.shape[1]-1:
            k=0
            soma=0
            while k<=d.shape[0]-1:
                if i!=k:
                    soma=soma+a[k]*(1/d[i,k])
                k=k+1
            if i!=j:
                T[i,j]=(o[i]*a[j]*(1/(d[i,j])**alfa))/soma
    
            j=j+1
        i=i+1
    return T
            
        
        
    