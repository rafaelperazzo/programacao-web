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
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+(l[i]-(media(lista)))**2
    s=(soma/(len(lista)-1))**0.5
    return s

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n=input('Digite a quantdade de termos da lista: ')
a=[]
b=[]
for i in range(0,n,1):
    a.append(input('Digite um valor: '))
for i in range(0,n,1):
    b.append(input('Digite um valor: '))
    
print ('%.2f'%media(a))
print ('%.2f'%desvio(a))
print ('%.2f'%media(b))
print ('%.2f'%desvio(b))
