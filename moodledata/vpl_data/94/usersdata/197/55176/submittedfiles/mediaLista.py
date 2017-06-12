# -*- coding: utf-8 -*-
n=float(input('Digite o numero de elementos da lista:'))
lista=[]
soma=0
for i in range(0,len(lista),1):
    numero=float(input('Digite um elemento da lista:'))
    lista.append(numero)
    soma=soma+lista[i]
media=soma/len(lista)
a=media
print('%.2f'%lista[0])
print('%.2f'%lista[len(lista)-1]
print('%.2f'%a)
print(lista)