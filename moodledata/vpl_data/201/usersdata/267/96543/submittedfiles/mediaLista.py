# -*- coding: utf-8 -*-
n=int(input('Quantidade de valores: '))
lista=[]
soma=0
for i in range(0,n,1):
    elem=int(input('Digite o elemento: '))
    lista.append(elem)
    soma=soma+lista[i]
print('%.2f' %lista[0])
print('%.2f' %lista[n-1])
print(soma/n)
print(lista)
print ('%.2f' %(lista))

