# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    media = soma/len(lista)
    return media

def desvio(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + ((lista[i]-media(lista))**2)
    resultado=(soma/(n-1))**(1/2)
    return resultado

n=input('Digite n: ')

a=[]
b=[]

for i in range(0,n,1):
    a.append(input('Digite um elemento da primeira lista: '))
    
media_a=media(a)

somatorioa=0

desvio_a=desvio(a)

for i in range(0,n,1):
    b.append(input('Digite um elemento da segunda lista: '))
    
media_b=media(b)

somatoriob=0
desvio_b=desvio(b)

print('%.2f'%media_a)
print('%.2f'%desvio_a)
print('%.2f'%media_b)
print('%.2f'%desvio_b)
#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista


#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 