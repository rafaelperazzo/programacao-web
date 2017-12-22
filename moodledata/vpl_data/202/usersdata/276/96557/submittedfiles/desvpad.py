# -*- coding: utf-8 -*-
import math

#comece abaixo
n= int(input('Digite a quantidade de elementos: '))

a = []

for i in range (0,n,1):
    valor_a = float (input('Digite o elemento da lista: '))
    a.append (valor_a)

def media (lista):
    soma = 0
    for i in range (0,len(lista),1):
        soma = soma + a[i]
    media = soma /n
    return (media)
    
def desvio (lista):
    somatorio = 0
    for i in range  (0,len(lista),1):
        somatorio = somatorio + (lista[i]-media(lista))**2
    desvio = (somatorio/(n-1))**(1/2)
    return (desvio)

print ('%.2f' %a[0])
print ('%.2f' %a[n-1])
print ('%.2f' %media (a))
print ('%.2f' %desvio(a))
    
