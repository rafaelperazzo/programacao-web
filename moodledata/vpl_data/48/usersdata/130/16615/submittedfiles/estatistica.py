# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
M=media(lista)
def desvio(lista): 
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+(lista[i]-M)**2
    resultado=(soma/(len(lista)-1))**0.5
    return resultado

a=[]
b=[]
n=input('Digite o valor de n:')
for i in range(0,n,1):
    a.append(input('Digite um elemento de a:'))
for i in range(0,n,1):
    b.append(input('Digite um elemento de b:'))
Ma=media(a)
Mb=media(b)
Da=desvio(a)
Db=desvio(b)
print('%.2f'%Ma)
print('%.2f'%Da)
print('%.2f'%Mb)
print('%.2f'%Db)




