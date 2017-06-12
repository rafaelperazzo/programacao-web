# -*- coding: utf-8 -*-
import math

#comece abaixo
def media (lista):
    soma=0
    for i in range (0,len(lista),1):
        soma=soma+a[i]
    soma=soma/n
    return soma
def desvio (lista):
    soma=0
    for i in range (0,len(lista),1):
        soma=soma+((lista[i]-media(a))**2)
    soma=((soma/(n-1))**0.5)
    return soma

n=int(input('digite o numero de elementos da lista:'))
a=[]
for i in range(0,n,1):
    numero=int(input('digite o valor da lista:'))
    a.append(numero)
print('%.2f'%a[0])
print('%.2f'%a[n-1])
mediaa=media (a)
print('%.2f'%mediaa)
desvioa=desvio (a)
print('%.2f'%desvioa)
    
