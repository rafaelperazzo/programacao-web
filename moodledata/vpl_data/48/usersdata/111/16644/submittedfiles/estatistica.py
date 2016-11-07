# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista

def dp(lista):
    soma=0
    for j in range(0,len(lista),1):
        x=(((lista[j]-media)**2)/(len(lista)-1)**0.5))
        soma = soma + x
        return dp
        

n=input('tamanho da lista: ')

a=[]
b = 0
for k in range(0,n,1):
    a.append(input('num:'))
    b=b+lista[k]
    
print media[b]


c=[]
d = 0
for m in range(0,n,1):
    c.append(input('num:'))
    d=d+lista[k]
    
print media[d]

    
    

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 