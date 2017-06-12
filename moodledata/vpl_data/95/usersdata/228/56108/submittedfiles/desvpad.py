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
    
def despd(a,media):   
    md=media(a)
    soma=0
    for i in range(0,len(a),1):
        soma=soma+((a[i]-md)**2)
    variância=soma/(len(a)-1)
    desvio=(variância**0,5)
    return(desvio)

print('%.2f'%lista[0])
print('%.2f'%lista[len(lista)-1])
print('%.2f'%media(lista))
print('%.2f'%despd(lista))