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
    for j in range(0,len(lista),1):
        x=((lista[j]-media(lista))**2)
        soma=soma+x
    d=((soma)/(len(lista)-1))**0.5
    return d
#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n=input('Digite o número de elementos das listas:')
a=[]
b=[]
for k in range (0,n,1):
    a.append(input('Digite um número para compor a lista a:'))
for l in range (0,n,1):
     b.append(input('Digite um número para compor a lista b:'))
media_a=media(a)
desvio_a=desvio(a)
media_b=media(b)
desvio_b=desvio(b)
print ('%.f'%media_a)
print ('%.f'%desvio_a)
print ('%.f'%media_b)
print ('%.f'%desvio_b)