# -*- coding: utf-8 -*-
import math

#comece abaixo
def desvio(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+lista[i]
    media=soma/len(lista)
    soma2=0
    for i in range(0,len(lista),1):
        a=(lista[i]-media)**2
        soma2=soma2+a
    variancia=soma2/(len(lista)-1)
    desvio=variancia**(0.5)
n=int(input('n: '))
lista=[]
for i in range(1,n+1,1):
    a=float(input('Digite um elemento: '))
    lista.append(a)
soma=0
for i in range(0,len(lista),1):
    soma=soma+lista[i]
media=soma/len(lista)    
print('%.2f'%lista[0])
print('%.2f'%lista[len(lista)-1])
print('%.2f'%media)
print('%.2f'%desvio)