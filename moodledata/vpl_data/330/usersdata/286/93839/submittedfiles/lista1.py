# -*- coding: utf-8 -*-
quant = int(input('Quantos elementos você quer? '))
sompar = 0
somimpar = 0
qpar = 0
qimpar = 0

lista = []
for i in range (1 , quant, 1):
    lista.append(input('Digite o elemento: '))
    print(lista[i])
