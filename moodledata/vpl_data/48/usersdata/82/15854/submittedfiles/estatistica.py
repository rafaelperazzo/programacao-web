# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    media = soma/len(lista)
    return media

a=[]
b=[]
n= input ('Digite a quantidade de elementos:')
for i in range (0,n,1):
    a.append(input('Digite um elemento'))
for i in range (0,n,1):
    b.append(input('Digite um elento:'))

media_a = media(a)
media_b = media(b)

print(media_a)
print(media_b)
#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 