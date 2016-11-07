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
    dpf=((soma)/(len(lista)-1))**0.5
    return dpf

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
a=[]
b=[]
n=input('Digite n:')

for j in range (0,n,1):
    a.append (input('Digite um elemento de a:'))

for k in range (0,n,1):
    b.append (input('Digite um elemento de b:'))

mediaa=media(a)
dpa=dp(a)
mediab=media(b)
dpb=dp(b)

print ('%.2f'%mediaa)
print ('%.2f'%dpa)
print ('%.2f'%mediab)
print ('%.2f'%dpb)
