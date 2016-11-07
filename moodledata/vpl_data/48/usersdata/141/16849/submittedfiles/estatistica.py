# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
def desviopadrao(lista):
    soma2=0
    for i in range (0,len(lista),1):
        soma2 = soma2 + ((lista[i] - media(lista))**2) 
    S=(soma2/(len(lista)-1))**0.5
    return S  
n=input('digite o valor de n:')
a=[]
b=[]
for i in range (0,n,1):
    a.append(input('digite o valor de a:')
for i in range (0,n,1):
    b.append(input('digite o valor de b:')
A=media(a)
B=media(b)
DA=desviopadrao(a)
DB=desviopadrao(b)
print(A)
print(DA)
print(B)
print(DB)

