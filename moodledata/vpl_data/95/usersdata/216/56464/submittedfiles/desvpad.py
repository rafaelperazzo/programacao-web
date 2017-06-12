# -*- coding: utf-8 -*-
import math

#comece abaixo
s=int(input('Digite a qunatidade:'))
x=[]
for i in range(0,s,1):
    n=float(input('Digite um valor'))
    x.append(n)

def media(x):
    soma=0
    for i in range(0,len(x),1):
        soma=soma+x[i]
    media=soma/len(x)
    return(media)

def desvio(x):
    for i in range(0,len(x),1)):
        soma=soma+(x[i]-media(lista))
        desvio=(1)/(len(x)-1)*soma)
    return (desvio)
    
print(x[0])
print(x[len(x)-1])
print(media(x))
print(desvio(x))
    
print(media(x))

