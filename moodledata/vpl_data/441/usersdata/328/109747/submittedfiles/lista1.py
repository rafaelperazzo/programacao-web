# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de elementos:'))
lista=[]
for i in range(n):
    lista.append(int(input('Digite Valores para a lista:')))
lista_im=[]
lista_par=[]
for i in range(n):
    if lista[i]%2==0:
        lista_par.append(lista[i])
    else:
        lista_im.append(lista[i])
print(sum(lista_im))
print(sum(lista_par))
print(len(lista_im))
print(len(lista_par))
print(lista)