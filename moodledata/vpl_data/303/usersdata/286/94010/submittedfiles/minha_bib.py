# -*- coding: utf-8 -*-

#COMECE AQUI ABAIXO
quant = int(input('Quantos elementos você quer? '))
lista = []

soma = 0
desvpad = 0
media = 0
somatorio = 0

for i in range(0,quant,1):
    lista.append(int(input('Digite o elemento: ')))
for i in range(0,quant,1):
    soma += lista[i]
media = soma/float(quant)
for i in range(0,quant,1):
    somatorio += (lista[i] - media)**2
    
desvpad = ((1/(quant -1)) * (somatorio))**0.5


print(desvpad)
print(media)