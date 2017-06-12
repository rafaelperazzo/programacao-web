# -*- coding: utf-8 -*-
n=float(input('Digite o numero de elementos da lista:'))
lista=[]
for i in range(1,n+1,1):
    numero=float(input('Digite um elemento da lista:'))
    lista.append(numero)
for i in range(o,len(lista),1):
    soma=soma+lista[i]
media=soma/len(lista)

print('%.2f'%lista[0])
print('%.2f'%lista[len(lista)-1]
print('%.2f'%media)
print(lista)