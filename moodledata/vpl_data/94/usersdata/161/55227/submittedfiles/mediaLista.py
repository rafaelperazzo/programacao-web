# -*- coding: utf-8 -*-
n=int(input('Informe a quantidade de elementos da lista:'))
lista=[]
soma=0
for i in range(1,n+1,1):
    numero=float(input('Informe um número:'))
    lista.append(numero)
for i in range(0,len(lista),1):
    soma=soma+lista[i]
media=soma/len(lista)
print('%.2f' %lista[0])
print('%.2f' %lista[len(lista)-1])
print('%.2f' %media)
print(lista)

    

