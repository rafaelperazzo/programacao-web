# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    media = soma/len(lista)
    return media

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista

def desviopadrao(lista):
    soma=0
    for i in range (0,len(lista),1):
        soma=soma+((lista[i]-media(lista))**2)
    s=((1/(len(lista)-1))*soma)**(1/2)
    return s


a=[]
b=[]
n=input('digite os elementos:')
for i in range (0,n,1):
    a.append(input('digite o elemento:'))
    
for i in range (0,n,1):
    b.append(input('digite o elemento:'))


media_a = media(a)
media_b = media(b)
desvio_a=desviopadrao(a)
desvio_b=desviopadrao(b)


print ('%.2f'%media_a)
print ('%.2f'%desvio_a)
print ('%.2f'%media_b)
print ('%.2f'%desvio_b)

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 