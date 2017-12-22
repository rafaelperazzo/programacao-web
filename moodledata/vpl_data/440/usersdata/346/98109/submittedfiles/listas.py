# -*- coding: utf-8 -*-

n= int(input('Digite o valor de n: '))
lista= []
for i in range(0,n,1):
    lista.append(int(input('Digite um valor: ')))

anterior= lista[0]
maior_altura= 0

i=1
while i<n:
    atual= (lista[0]+1)
    i= i+1
    altura_degrau= atual-anterior
    if (altura_degrau<0):
        altura_degrau= -altura_degrau
    if (altura_degrau > maior_altura):
        maior_altura= altura_degrau
    anterior = atual
    
print(maior_altura)