# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista

def desvio(lista):
    dp = 0
    for j in range (0,len(lista),1):
        dp = dp + (((lista[j] - media(lista))**2)/(n-1))**0.5
    return dp

n = input ('Digite a quantidade de termos:')
a= []
b=[]
for x in range (0, n, 1):
    a.append (input('Digite um número:'))
for y in range (0, n, 1):
    b.append (input ('Digite um número:'))

media1 = media(a)
desvio1 = desvio(a)

media2 = media(b)
desvio2 = desvio(b)
    
print ('%.2f' %media1)
print ('%.2f' %desvio1)
print ('%.2f' %media2)
print ('%.2f' %desvio2)