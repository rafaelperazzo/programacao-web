# -*- coding: utf-8 -*-
def media (len(lista)):
    soma=0
    for i in range (0,len(lista),1):
        soma+=lista[i]
    media=soma/len(lista)
    return (media)

m= int(input('Digite a quantidade de listas: '))
n= int(input('Digite a quantidade de elementos das listas: ')) 
for i in range (0,m,1):
    lista=[]
    for i in range (0,n,1):
        lista.append(int(input('Digite o elemento %d da lista: ' %(i+1))))
    print(media(n))
