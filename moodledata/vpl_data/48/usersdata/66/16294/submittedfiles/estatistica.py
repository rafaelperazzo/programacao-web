# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desviopadrao(lista):
    desvio=0
    for i in range(0,len(lista),1):
        desvio=desvio +(lista[i] - media))**2
    desvio=((desvio*(1/(n-1)))**0.5
    return desvio

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
x=[]
y=[]
n=input("digite a quantidade de elemento")
for i in range (0,n,1):
    x.append(input("digite os elementos:"))
nx=input('digite a quantidade de elementos de x: ')
for i in range(0,n,1):
    y.append(input('digite os elementos de y:'))

media_x = media(x)
media_y=media (y)
desvioparao_x=desviopadrao (x)
desviopadra_y=desviopadrao (y)

print ('%.2f'%media(x))
print ('%.2f'%desviopadrao(x))
print ('%.2f'%media(y))
print ('%.2f'%desviopadrao(y))