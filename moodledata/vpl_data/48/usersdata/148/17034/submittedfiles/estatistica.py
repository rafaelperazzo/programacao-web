# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    resultado = soma/len(lista)
    return resultado

#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desvioPadrao(lista):
    med=media(lista)
    
    somad=0
    for i in range(0,len(lista),1):
        somad=somad+(((lista[i])-med)**2)
    desv=((((1)/(n-1))*somad)**(1/2))
    return desv 

    
#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
n=input('Digite n:')
a=[]
b=[]
i=0
while i<n:
    a.append(input('Digite um elemento para a lista 1:'))
    i=i+1

i=0
while i<n:
    b.append(input('Digite um elemento para a lista 2:'))
    i=i+1

media_a=media(a)
desv_a=desv(a)
media_b=media(b)
desv_b=desv(b)

print('%.2f' %media_a)
print('%.2f' %desv_a)
print('%.2f' %media_b)
print('%.2f' %desv_b)