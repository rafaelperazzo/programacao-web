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
    cont=0
    for i in range(0,len(lista),1):
        p=((a[i]-media)**2)
        cont=cont+p
    desviop=(cont/(len(lista)-1))**0.5
    return desviop

#Por último escreva o programa principal, que pede a entrada e chama as funções criadas. 
l1=[]
l2=[]
n=input('Digite o valor de n:')
for a in range (0,n,1):
    l1.append(input('Digite um elemento da lista 1:'))
    
for a in range (0,n,1):
    l2.append(input('Digite um elemento da lista:'))
m1= media(l1)
d1= desvio(l1)
m2= media(l2)
d2= desvio(l2)
print ('%.2f'%m1)
print ('%.2f'%d1)
print ('%.2f'%m2)
print ('%.2f'%d2)

    