# -*- coding: utf-8 -*-
import math

#comece abaixo
n=int(input('Digite n:'))
lista=[]
for i in range(0,n,1):
    a=float(input('termos:'))
    lista.append(a)
def media(lista):
    soma1=0
    for i in range(0,len(lista),1):
        soma1=soma1+lista[i]
    media=soma1/len(lista)
    return(media)
def desvio(lista,media):
    soma2=0
    for i in range(0,len(lista),1):
        soma2=soma2+((lista[i]-media)**2)
    desvpad=(soma2/(n-1))**(0.5)
    return(desvpad)
    
print('%.2f'%lista[0])
print('%.2f'%lista[n-1])
print('%.2f'%media(lista))
print('%.2f'%desvio(lista,media))
    