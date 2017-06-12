# -*- coding: utf-8 -*-
n=int(input('qte de valores:'))
lista=[]
for i in range(0,n,1):
    t=int(input('termos:'))
    lista.append(t)
def media(lista):
    soma=0
    for i in range (0,len(lista),1):
        soma=soma+lista[i]
    media=soma/len(lista)
    return(media)

print('%.2f'%media(lista))
print('%.2f'%lista[0])
print('%.2f'%len(lista))