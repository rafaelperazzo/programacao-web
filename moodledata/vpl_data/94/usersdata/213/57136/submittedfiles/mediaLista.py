# -*- coding: utf-8 -*-
n=int(input('Informe a quantidade de elementos da lista: '))
lista=[]
for i in range(0,n,1):
    elemento=int(input('Informe os elementos da lista: '))
    lista.append(elemento)

soma=0
for i in range(0, len(lista),1):
    soma=soma+lista[i]
media=soma/len(lista)

print('%.2f' %(lista[0]))
print('%.2f' %(lista[len(lista)])
print('%.2f' %media)
print('%.2f' %lista)
