# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
a=0
def s(lista):
    for i in range (0,len(lista),1):
        a=(lista[i]-media)**2
        a=a+a
        s=(a)**0.5
    return s

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
lista_a=[]
lista_b=[]
n=input ('digite o valor de n:')

for i in range (0,n,1):
    lista_a.append(input('Digite um elemento:'))
    
for i in range (0,n,1):
    lista_b.append(input('Digite um elemento:'))
    
media_a=media(a)
media_b=media(b)
s_a=s(a)
s_b=s(b)
print media(a)
print media(b)