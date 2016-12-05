# -*- coding: utf-8 -*-
from __future__ import division

#escreva suas funcoes aqui
def somacolunas(matriz):
    a=[]
    for j in range (0,matriz.shape[0],1):
        cont=0
        for i in range (0,matriz.shape[1],1):
            cont=cont+matriz[i,j]
        
        a.append(cont)
    
    return a



def somalinhas(matriz):
    a=[]
    for i in range (0,matriz.shape[1],1):
        cont=0
        for j in range (0,matriz.shape[0],1):
            cont=cont+matriz[i,j]
        
        a.append(cont)
    
    return a
    
def sum(T):
    cont=0
    for i in range (0,T.shape[0],1):
        for j in range(0,T.shape[1],1):
            cont=cont+T[i,j]
    
    return cont
    
    