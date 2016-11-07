# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desviopadrao(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+((lista[i]-media(lista))**2)
    d=((1/(n-1))*soma)**0.5
    return d

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n=int(input('Digite o número de elementos da lista:'))
a=[]
b=[]

for i in range(0,n,1):
    a.append(input('Digite os valores de a:'))
    
for i in range(0,n,1):
    b.append(input('Digite os valores de b:'))
    
media_a=media(a)
media_b=media(b)
desvio_a=desviopadrao(a)
desvio_b=desviopadrao(b)

print('%.2f'%media_a)
print('%.2f'%desvio_a)
print('%.2f'%media_b)
print('%.2f'%desvio_b)