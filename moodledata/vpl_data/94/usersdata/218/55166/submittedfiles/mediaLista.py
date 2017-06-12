# -*- coding: utf-8 -*-
def media (lista):
    soma=0
    for i in range (0,len(lista),1):
        soma=soma+lista[i]
    soma=(soma/len(lista))
    return soma
n= int(input('digite o numero de elementos da lista:'))
for i in range (0,n,1):
    mumero=int(input('digite o elemento da lista:'))
    a.append(numero)
valor=media (a)
print(valor)