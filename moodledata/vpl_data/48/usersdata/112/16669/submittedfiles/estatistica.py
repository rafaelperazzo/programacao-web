# -*- coding: utf-8 -*-
from __future__ import division
n=input('Digite a quantidade de números da lista')
def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    media = soma/len(lista)
    return media
for i in range (0,n-1,1):
    soma=0
    J=input('Digite os números da lista')
    soma=soma+J
    T=(J-media)**2
    
