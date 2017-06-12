# -*- coding: utf-8 -*-
import math

#comece abaixo
def media(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+lista[i]
    resultado=soma/len(lista)
    return resultado
def dp(lista):
    v=0
    d=0
    for i in range(0,len(lista),1):
        v=v+((lista[i]-media(lista))**2)
    d=(v/(len(lista)-1))**0.5
    return d
a=[]
n=int(input('n:'))
for i in range(0,n,1):
    valor=int(input('valor:'))
    a.append(valor)
print('%.2f'%a[0])
print('%.2f'%a[len(a)-1])
print('%.2f'%media(a))
print('%.2f'%dp(a))






