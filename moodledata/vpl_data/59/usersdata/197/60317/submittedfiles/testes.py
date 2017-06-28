# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=int(input('Digite um numero de 4 digitios:'))
lista=[]
while n>0:
    valor=n%10
    n=n//10
    lista.insert(0,valor)
print(lista)