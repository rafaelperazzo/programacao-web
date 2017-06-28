# -*- coding: utf-8 -*-
import numpy as np
def Slinhas(a):
    soma=0
    lista1=[]
    for l in range (0,a.shape[0],1):
        for c in range (0,a.shape[1],1):
            soma=soma+a[l,c]
            lista1.append(soma)  
        return(lista1)
def Scolunas(a):
    soma=0
    lista2=[]
    for c in range (0,a.shape[1],1):
        for l in range (0,a.shape[0],1):
            soma=soma+a[l,c]
            lista2.append(soma)
        return(lista2)
n=int(input('tamanho da matriz:'))


    
    
        

