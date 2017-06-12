# -*- coding: utf-8 -*-
import math

#comece abaixo
n=int(input('digite o número de elementos:'))
lista=[]
for i in range(0,n,1):
    elemento=float(input('digite o elemento:'))
    lista.append(elemento)

def media(a):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+a[i]
    media=soma/len(lista)    
    return(media)    
    
def    
    

