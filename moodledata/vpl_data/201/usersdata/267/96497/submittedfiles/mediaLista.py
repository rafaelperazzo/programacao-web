# -*- coding: utf-8 -*-
n=int(input('Quantidade de valores: '))
lista=[]
soma=0
for i in range(0,n,1):
    elem=int(input('Digite o elemento: '))
    lista.append(elem)
    soma=soma+lista[i]
print(soma/n)
print ('%.f' %(lista))

