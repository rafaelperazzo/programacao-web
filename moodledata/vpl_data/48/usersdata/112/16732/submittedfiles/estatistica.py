# -*- coding: utf-8 -*-
from __future__ import division
n=input('Digite a quantidade de números da lista')
def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    media = soma/len(lista)
    return media
J=[]
for i in range (0,n,1):
    soma1=0
soma1=(J[i]-media)**2+soma1
S=((1/(n-1))*soma1)**(1/2)
print(S)