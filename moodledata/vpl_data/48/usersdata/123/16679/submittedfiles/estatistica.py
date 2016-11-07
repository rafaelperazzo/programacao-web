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
    soma2 = 0
    for i in range(0,len(lista),1):
        soma2 = soma2 + ((lista[i]-media(lista))**2)
    s = (soma2/(len(lista)-1))**(1/2)
    return s
    
#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n= input('Insira n:')
a=[]
b=[]
for i in range (0,n,1):
    a.append(input('Insira a:'))
for i in range (0,n,1):
    b.append(input('Insira b:'))
mediaA=media(a)
dpA=desvio(a)
mediaB=media(b)
dpB=desvio(b)
print('%.2f'%mediaA)
print('%.2f'%dpA)
print('%.2f'%mediaB)
print('%.2f'%dpB)