# -*- coding: utf-8 -*-
n=int(input("digite o tamanho da lista"))
lista=[]
media=0
for i in range(0,n,1):
    lista.append(int(input("digite o primeiro valor")))
    media=media+lista[i]
    media=media/len(lista)
print(lista[0])
print(lista[n-1])
print(media)
print(lista)
