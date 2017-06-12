# -*- coding: utf-8 -*-
import math

#comece abaixo
n=int(input('digite n:'))
lista=[]
for i in range(0,n,1):
    t=float(input('termo:'))
    lista.append(t)
def media(lista):
    soma1=0
    for i in range (0,len(lista),1):
        soma1=soma1+lista[i]
    media=soma1/len(lista)
    return(media)
def DP(lista,media):
    soma2=0
    for i in range(0,n,1):
        soma2=soma2+((lista[i]-media)**2)
    r=soma2/(len(lista)-1)
    return(r)
    
dp=(DP(lista,media(lista)))**0.5
print('%.2f'%lista[0])
print('%.2f'%lista[n-1])
print('%.2f'%media(lista))
print(dp)