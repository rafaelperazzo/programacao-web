# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado
def dp(lista):
    soma= 0
    for i in range(0,len(lista),1):
        soma=soma+(lista[i]-media(lista))**2
    resultado=(soma/(n-1))**0.5
    return resultado
a=[]
b=[]
n=input('n:')
for i in range (0,n,1):
    a.append(input('termos de a:'))
for i in range (0,n,1):
    b.append(input('termos de b:'))
media_a=media(a)
media_b=media(b)
dp_a=dp(a)
dp_b=dp(b)
print ('%.2f' %media(a))
print ('%.2f' %media(b))
print ('%.2f' %dp(a))
print ('%.2f' %dp(b))

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 