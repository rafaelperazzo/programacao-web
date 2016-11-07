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
    for i in range (0,len(lista),1):
        soma=soma+(lista[i]-media(lista))**2
    dp=(soma/(len(lista)-1))**0.5

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n=input('digite n:')
a=[]
b=[]
for i in range(0,len(a),1):
    a.append(input('digite um valor de a:')
for i in range(0,len(b),1):
    b.append(input('digite um valor de b:')

    
    
    
    
    
    
    
    
    