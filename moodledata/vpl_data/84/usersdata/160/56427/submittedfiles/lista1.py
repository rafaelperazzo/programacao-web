# -*- coding: utf-8 -*-
from __future__ import division
def simpar(a):
    soma=0
    for i in range(0,len(a),1):
        if a[i]%2==1:
            soma=soma+a[i]
    return(soma)
    
def spar(a):
    soma=0
    for i in range(0,len(a),1):
        if a[i]%2==0:
            soma=soma+1
    return(soma)

def cimpar(a):
    cont=0
    for i in range(0,len(a),1):
        if a[i]%2==1:
            cont=cont+1
    return(cont)
    
def cpar(a):
    cont=0
    for i in range(0,len(a),1):
        if a[i]%2==0:
            cont=cont+1
    return(cont)
    

        
n=int(input('Digite a quantidade de elementos da lista:'))
a=[]
for i in range(1,n+1,1):
    valor=float(input('Digite a lista:'))
    a.append(valor)
    
print(simpar(a))
print(spar(a))
print(cimpar(a))
print(cpar(a))
print(a)

