# -*- coding: utf-8 -*-
import math

#comece abaixo
n=int(input('digite o tamanho da lista:'))
lista=[]
for i in range (0,n,1):
    lista.append(int(input('valores da lista:')))
    print(lista[0])
    print(lista[len(lista)-1])
soma=0
soma1=0
for i in range (0,n,1):
    soma=soma+lista[i]
    media=soma/len[lista]
    print('%d',media)
for i in range (0,n,1):
    soma1=soma1+((lista[i]-media)**2)
    desPad=(soma1/(n-1)**(1/2))
    print('%d',desPad)

