# -*- coding: utf-8 -*-
import math

#comece abaixo
n=int(input('digite a quantidade de valores:'))
lista=[]
for i in range(0,n,1):
    t=float(input('digite o termo da lista:'))
    lista.append(t)
def media(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+lista[i]
    media=soma/len(lista)
    return(media)
def desvio(lista,media):
    soma1=0
    for i in range(0,n,1):
        soma1=soma1+((lista[i]-media)**2)
    r=soma1/(len(lista)-1)
    return(r)

desvio=(desvio(lista,media(lista)))**0.5
print('%.2f'%lista[0])
print('%.2f'%lista[n-1])
print('%.2f'%media(lista))
print('%.2f'%desvio)