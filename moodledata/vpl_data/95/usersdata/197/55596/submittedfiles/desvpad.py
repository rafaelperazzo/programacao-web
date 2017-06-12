# -*- coding: utf-8 -*-
import math

#comece abaixo
n=int(input('Digite o numero de elementos da lista:'))
lista=[]
for i in range (1,n+1,1):
    numero=float(input('Digite um numero da lista:'))
    lista.append(numero)
soma=0
for i in range(0,len(lista),1):
    soma=soma+lista[i]
media=soma/len(lista)
soma2=0
for i in range(0,len(lista),1):
    soma2=soma2+(lista[i]-media)**2
desvio=(soma2/(n-1))**(0.5)
print('%.2f'%lista[0])
print('%.2f'%lista[len(lista)-1])
print('%.2f'%media)
print('%.2f'%desvio)