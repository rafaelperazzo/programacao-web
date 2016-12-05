# -*- coding: utf-8 -*-
from __future__ import division

#escreva suas funcoes aqui
def somal(b):
    soma=0
    i=0
    j=0
    v=[]
    n=b.shape[0]-1
    m=a.shape[1]-1
    while n>=i:
        while m>=j:
            soma=soma+b[i,j]
            j=j+1
        v.append(soma)
        i=i+1
        j=0
        soma=0
            
    return v

def somac(c):
    soma=0
    i=0
    j=0
    v=[]
    m=c.shape[0]-1
    n=c.shape[1]-1
    while n>=i:
        while m>=j:
            soma=soma+c[i,j]
            j=j+1
        v.append(soma)
        i=i+1
        j=0
        soma=0
    
    return v
    
x= input("Número de linhas da matriz quadrada:")
a=np.zeros((x,y))

for i in range(0,a.shape[0],1):
    for j in range(0,a.shape[1],1):
        a[i,j]=input("Digite um valor:")
    
print somal(a)
print somac(a)