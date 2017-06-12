# -*- coding: utf-8 -*-
import math

#comece abaixo
n=int(input('digite o tamanho da lista:'))
lista=[]
for i in range(0,n,1):
    x=float(input('digite o valor:'))
    lista.append(x)
def media(lista):
    soma1=0
    for i in range(0,len(lista),1):
        soma=soma+lista[i]
    media=soma/len(lista)
    return(media)
def desvpad(lista):
    soma2=0
    for i in range(0,len(lista),1):
        soma2=soma2+((lista[i]-media)**2)
    desvpad=(soma2/(n-1)**(0.5))
    return(desvpad)
print('%.2f'%lista[0])
print('%.2f'%(lista[n-1]))
print('%.2f'%media(lista))
print('%.2f'%desvpad(lista))