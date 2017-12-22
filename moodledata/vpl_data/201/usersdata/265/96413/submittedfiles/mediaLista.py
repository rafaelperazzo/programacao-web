# -*- coding: utf-8 -*-
n=int(input('digite a quantidade de termos da lista: '))
def media(lista):
    soam=0
    for i in range (0,len(lista),1):
        soma=soma+lista[i]
    resultado=soma/len(lista)
    return resultado

