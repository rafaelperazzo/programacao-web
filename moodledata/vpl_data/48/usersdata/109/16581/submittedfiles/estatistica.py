# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
cont=0
def desvio(lista):
    for i in range(0,len(lista),1):
        p=((a[i]-resultado)**2)
        cont=cont+p
    desvio=(cont/(len(lista)-1))**0.5
    return desvio

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
a1=[]
n=input('Digite o valor de n:')
for a in range (0,n,1):
    a.append()
    