# -*- coding: utf-8 -*-
from __future__ import division

def somadiagonal1(a):
    soma=0
    for i in range(0, a.shape[0],1):
        som=soma+a[i,i]
    return soma
    
def somadiagonal2(a):
    soma=0
    i=0
    j=a.shape[0]-1
    
    while i<a.shape[0]:
        soma=soma+a[i,j]
        i=i+1
        j=j-1
    return soma
    
    
def somadaslinhas(a):
    s=[]
    for i in range(0,a.shpe[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        s.append (soma)
    return s
    
def somaadascolunas(a):
    s=[]
    for i in range(0,a.shpe[0],1):
        soma=0
        for j in range(0,a.shape[1],1):
            soma=soma+a[i,j]
        s.append (soma)
    return s
    
def quadradomagico(a):
    sd1=somasiagonal1(a)
    sd2=somadiagonal2(a)
    somal=somalinhas(a)
    somac=somacolunas(a)
    cont=0
    for i in range(0,len(somal),1):
        if sd1==sd2==somal[i]==somac[i]:
            cont=cont+1
    if cont==len(somal):
        
        return True
    else:
        return False
        
        
n=input('digite  quantidade de ellementos da lista:')
a=[]
for i in range(0,n,1):
    a.append(input('coloque valores a lista'))
if quadromagico(a):
        
    print('S')
else:
    print('N')
            
    
   
            
    