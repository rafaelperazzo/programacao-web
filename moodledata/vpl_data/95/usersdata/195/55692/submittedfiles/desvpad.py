# -*- coding: utf-8 -*-
import math

#comece abaixo
n=int(input('digite o tamanho da lista:'))
lista=[]
for i in range(0,n,1):
    x=float(input('digite os termos'))
    lista.append(x)
def media(lista):
    soma1=0
    for i in range(0,len(lista),1):
        soma1=soma1+lista[i]
    media=soma1/len(lista)
    return(media)
def desvpad(lista,media):
    soma2=0
    for i in range(0,len(lista),1):
        soma2=soma2+((lista[i]-media)**2)
    desvio=(soma2/(n-1))**(0.5)
    return(desvio)
print('%.2f' %lista[0])
print('%.2f' %(lista[n-1]))
print('%.2f' %media(lista))
print('%.2f' %desvpad(lista,media(lista)))