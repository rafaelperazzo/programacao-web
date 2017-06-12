# -*- coding: utf-8 -*-
def media(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+lista[i]
    media=soma/len(lista)
    return soma

a=[]
n=input('digite a quantidade dos elementos de a:')
for i in range(0,n,1):
    a.append(input('digite um elemento:'))
media_a:media(a)
print media_a


