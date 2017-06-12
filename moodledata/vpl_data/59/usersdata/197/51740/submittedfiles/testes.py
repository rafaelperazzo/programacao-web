# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('digite o tamanho da lista:'))
listaa=[]
soma=0
for i in range (1,n+1,1):
    valor=int(input('digite um numero da lista'))
    lista.append(valor)
    if lista[i]%2!=0:
        soma=soma+lista[i]
        print(soma)
print(lista)