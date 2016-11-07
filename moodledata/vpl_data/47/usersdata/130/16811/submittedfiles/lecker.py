# -*- coding: utf-8 -*-
from __future__ import division

def lecker(lista):
    cont=0
    for i in range(0,len(lista),1):
        if i==0:
            if lista[i]>lista[i+1]:
                cont=cont+1
        elif i==len(lista)-1:
            if lista[i]>lista[i-1]:
                cont=cont+1
        else:
            if lista[i]>lista[i+1] and lista[i]>lista[i-1]:
                cont=cont+1
    if cont==1:
        return S
    else:
        return N
        
a=[]
b=[]
n=input('Digite o valor de n:')
for i in range(0,n,1):
    a.append(input('Digite um elemento de a:'))
for i in range(0,n,1):
    b.append(input('Digite um elemento de b:'))
A=lecker(a)
B=lecker(b)
print(A)
print(B)
        