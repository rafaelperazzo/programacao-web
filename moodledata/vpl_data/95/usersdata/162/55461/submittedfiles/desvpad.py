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
def desvio(lista):
    soma2=0
    for i in range(0,len(lista),1):
        soma2=soma2+((lista[i]-media)**2)
    desvio=(soma2/(n-1))**(0.5)
    return(desvio)
    
print    
    