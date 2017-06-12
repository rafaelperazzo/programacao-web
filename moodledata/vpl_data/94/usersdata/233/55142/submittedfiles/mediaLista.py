# -*- coding: utf-8 -*-
n=int(input('n: '))
lista=[]
for i in range(1,n+1,1):
    a=int(input('Digite um elemento: '))
    lista.append(a)
soma=0
for i in range(0,len(lista),1):
    soma=soma+lista[i]
media=soma/len(lista)
print('%.2f'%lista[0])
print('%.2f'%lista[len(lista)])
print('%.2f'%media)
lista.sort()
print(lista)