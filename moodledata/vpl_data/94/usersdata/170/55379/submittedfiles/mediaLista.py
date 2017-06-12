# -*- coding: utf-8 -*-
n=int(input('Digite o tamanho da lista:'))
lista=[]
def media(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+lista[i]
    media=soma/len(lista)
    return(media)
for i in range(0,n,1):
    x=float(input('Digite o valor:'))
    lista.append(x)
print('%.2f' %lista[0])
print('%.2f' %(lista[n-1]))
print('%.2f' %media(lista))
print(lista)
