# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
a=[]
b=[]
n=input('Digite o valor de n:')
for i in range(0,n,1):
    a.append(input('Digite um elemento:'))
for i in range(0,n,1):
    b.append(input('Digite o um elemento:'))
    


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 