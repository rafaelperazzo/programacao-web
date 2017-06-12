# -*- coding: utf-8 -*-
lista=[]
n=int(input('digite o tamanho da lista:'))
for i in range(0,n,1):
    a=float(input('digite um elemento:'))
    lista.append(a)
soma=0
for i in range(0,len(lista),1):
    soma=soma+(lista[i])
media=soma/len(lista)
print('%.2f'%lista[0])
print('%.2f'%lista[n-1])
print('%.2f'%media)
print(lista)



