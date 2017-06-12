# -*- coding: utf-8 -*-
lista=[]
n=int(input('Digite o tamanho da lista:'))
for i in range(1,n+1,1):
    v=float(input('Digite o valor:'))
    lista.append(v)
soma=0
for i in range(0,len(lista),1):
    soma=soma+lista[i]
media=soma/len(lista)
print('%.2f'%lista[0])
print('%.2f'%lista[len(lista)-1)
print(media)
print(lista)