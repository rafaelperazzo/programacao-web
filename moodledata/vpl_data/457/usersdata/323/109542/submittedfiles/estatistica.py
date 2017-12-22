# -*- coding: utf-8 -*-
import math

m=int(input('Digite a quantidade de listas: '))
n=int(input('Digite a quantidade de elementos das listas: '))

b=[]
c=[]

def media(lista):
    soma=0
    for i in range(0,len(Lista),1):
        soma=soma+a[i]
    media=soma/n
    return media
    
def desvio(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+(lista[i]-media(lista))**2
    desvio= (soma/(n-1))**(1/2)
    return desvio
    
for i in range(0,m,1):
    a=[]
    for i in range(0,n,1):
        valor=float(input('Digite o elemento da lista: '))
        a.append(valor)
    b.append(media(a))
    c.append(desvio(a))
for i in range(0,len(b),1):
    
    print('%.2f' %b[i])
    print('%.2f' %c[i])