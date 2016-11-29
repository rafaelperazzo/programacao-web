# -*- coding: utf-8 -*-
from __future__ import division

#escreva suas funcoes aqui
def somaColunaA(m):
    b=[]
    for j in range (0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
            b.append (soma)
            return b
def somaLinhaA(m):
    b=[]
    for i in range (0,a.shape[0],1):
        soma=0
        for i in range(0,a.shape[1],1):
            soma=soma+a[i,j]
            b.append (soma)
            return b

def matrizT(m):
   
    for i in range (0,d.shape[0],1):
        for j in range (0,d.shape[1],1):
            c[i,j]=o([i])*a([i])*i*((1/d[i,j]))*alfa
        soma=0
        for k in range (0,d.shape[1],1):
            soma[i,k]=soma+(a[k]*(1/d[i,k]))
            T[i,j]=c[i,j]/soma[i,k]
        for i in range (0,T.shape[0],1):
            for j in range(0,T.shape[1],1):
               T[i,j]=matrizT(o,a) 
        return T
            
o=somaLinhaA
a=somaColunaA
T=[]
    