# -*- coding: utf-8 -*-
from __future__ import division

n = input('Quantidade de pinos da fechadura: ')
m = input('Altura que o pino deve está: ')

i = 1
lista = []

while i<=n:
    lista.append(input('Digite o tamanho do pino: '))
    i = i+1
    

j = 0
cont = 0
    
while j<(n-1):
    while lista[j]>m and lista[j+1]>m:
        lista[j] = lista[j]-1
        lista[j+1] = lista[j+1]-1
        cont = cont+1
    while lista[j]<m and lista[j+1]<m:
        lista[j] = lista[j]+1
        lista[j+1] = lista[j+1]+1
        cont = cont+1
    while lista[j]>m:
        lista[j] = lista[j]-1
        cont = cont+1
    while lista[j]<m:
        lista[j] = lista[j]+1
        cont = cont+1
    j = j+1

print cont
print lista
