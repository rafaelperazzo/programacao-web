# -*- coding: utf-8 -*-
n=int(input('qte de valores:'))
lista=[]
soma=0
def media(lista):
    for i in range (0,len(lista),1):
        soma=soma+lista[i]
    media=soma/len(lista)
    return(media)

print(media)
print(lista(0))
print(len(lista)-1)