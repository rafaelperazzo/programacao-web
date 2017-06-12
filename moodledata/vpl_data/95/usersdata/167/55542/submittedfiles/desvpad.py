# -*- coding: utf-8 -*-
import math

#comece abaixo
n=int(input('digite n:'))
lista=[]
for i in range(0,n,1):
    t=float(input('termo:'))
    lista.append(t)
def media(lista):
    soma=0
    for i in range (0,len(lista),1):
        soma1=soma1+lista[i]
    media=soma1/len(lista)
    return(media)
for i in range(0,n-1,1):
    soma2=0
    r=(lista[0]-media(lista))**(1/2)
    soma2=soma2+r
dp=((1/(n-1)*r)**(1/2)
print('%.2f'%lista[0])
print('%.2f'%lista[n-1])
print('%.2f'%media(lista))
print(dp)