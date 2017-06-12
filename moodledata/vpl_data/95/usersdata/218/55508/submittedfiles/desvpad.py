# -*- coding: utf-8 -*-
import math

#comece abaixo
def media (lista):
    soma=0
    for i in range (0,len(lista),1):
        soma=soma+a[i]
    return soma
def desvio (lista):
    soma=0
    for i in range (0,len(lista),1):
        soma=soma+((lista[i]-media(a))**2)
        soma=(soma/n-1)**0.5
    return soma
n=int(input('digite o numero de elementos da lista:'))
a=[]
for i in range(0,n,1):
    numero=float(input('digite o valor da lista:'))
    a.append(numero)
print(a[0])
print(a[n-1])
mediaa=media (a)
print(mediaa)
desvioa=desvio (a)
print(desvioa)
    
