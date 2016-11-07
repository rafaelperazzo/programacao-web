# -*- coding: utf-8 -*-
from __future__ import division

def media(lista):
    soma = 0
    for i in range(0,len(lista),1):
        soma = soma + lista[i]
    media = soma/len(lista)
    return media
#Baseado na função acima, escreva a função para calcular o desvio padrão de uma lista
def desviop(lista):
    soma=0
    for i in range(0,len(lista),1):
        soma=soma+((lista(i) - media)**2)
    desviop= (soma/(n-1))**0.5
    return desviop

n=input('digite o valor de n: ')
lista1=[]
lista2=[]
for i in range (0,n,1):
    lista1.append(input('digite os n valores: ')
    
for j in range (0,n,1):
    lista2.append(input('digite os n valores: ')
media_l1=media(lista1)
media_l2=media(lista2)
s_l1=desviop(lista1)
s_l2=desviop(lista2)

print media_l1
print s_l1
print media_l2
print s_l2
    

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 