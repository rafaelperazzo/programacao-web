# -*- coding: utf-8 -*-
from __future__ import division
import numpy as np
def somal(a):
    l=[]
    for i in range(0,a.shape[0],1):
        soma=0
        for j in range (0,a.shape[1],1):
            soma=soma+a[i,j]
        l.append(soma)
    return l
def somac(a):
    l=[]
    for j in range(0,a.shape[1],1):
        soma=0
        for i in range(0,a.shape[0],1):
            soma=soma+a[i,j]
        l.append(soma)
    return l
def soma_diagonalp (a):
    soma=0
    for i in range(0,a.shape[0],1):
        soma=soma+a[i,i]
    return soma 
def diagonalsec(a):
    soma=0
    for i in range (0,a.shape[0],1):
        for j in range (0,a.shape[1],1):
            if (i+j)==a.shape[0]-1:
                soma=soma+a[i,j]
    return soma 
def quadradomagico(a):
    sc=somac(a)
    sl=somal(a)
    dp=soma_diagonalp(a)
    ds=diagonalsec(a)
    cont=0
    for i in range(0,len(sl),1):
        if dp==ds==sc[i]==sl[i]:
            cont=cont+1
    if cont==len(sl):
        return True
    else:
        return False
            
            
n=input("Digite um número: ")
a=np.zeros((n,n))
for i in range (0,n,1):
    for j in range(0,n,1): #VOCE TINHA ESQUECIDO A SEGUNDA REPETIÇÃO!!
        a[i,j]=input("Digite um valor: ")
if quadradomagico(a):
    print ("S")
else:
    print ("N")
    

