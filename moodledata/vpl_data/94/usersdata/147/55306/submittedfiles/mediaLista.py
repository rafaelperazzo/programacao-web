
# -*- coding: utf-8 -*-
n=int(input('digite numero de elementos:'))
lista=[]
for i in range(1,n+1,1):
    valor=float(input('digite valor:'))
    lista.append(valor)
soma=0
for i in range(0,len(lista),1):
    soma=soma+lista[i]
media=soma/len(lista)
print(lista[0])
print(lista[n-1])
print(media)
print(lista)


