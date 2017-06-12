# -*- coding: utf-8 -*-
import math
def media(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+lista[i]
    
    media=soma/len(lista)
    return(media)
    
def desvio(lista):
    x=media(lista)
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+(lista[i]-x)**2
        
    desvio=(soma/(len(lista)-1))**(1/2)
    return(desvio)
    
n=int(input('digite um valor:'))
x=[]
for i in range(1,n+1,1):
    valor=float(input('digite um valor:'))
    x.append(valor)
    
print('%.2f' %x[0])
print('%.2f' %x[len(x)-1])
print('%.2f' %media(x))
print('%.2f' %desvio(x))
        

