# -*- coding: utf-8 -*-
n=int(input('Digite o numero de elementos da lista:'))
lista=[]
for i in range(1,n+1,1):
    numero=int(input('Digite um elemento da lista:'))
    lista.append(numero)
soma=0
for i in range(0,len(lista),1):
    soma=soma+lista[i]
media=soma/len(lista)
a=media
print('%.2f'%lista[0])
print('%.2f'%lista[len(lista)-1])
print('%.2f'%a)
print(lista)