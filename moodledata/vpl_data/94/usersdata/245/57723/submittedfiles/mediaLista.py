# -*- coding: utf-8 -*-
lista=[]
n=int(input('Digite o tamanho da lista:'))
for i in range(1,n+1,1):
    v=float(input('Digite o valor:'))
    lista.append(v)
def media(a):
    soma=0
    for i in range(0,len(a),1):
        soma=soma+a[i]
    media=soma/len(a)
    return(media)
print(lista[0])
print(lista[len(lista)-1]
print(media(lista))
print(lista)

