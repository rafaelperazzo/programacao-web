# -*- coding: utf-8 -*-
quant = int(input('Quantos elementos você quer? '))
lista = []

sompar = 0
somimpar = 0
qpar = 0
qimpar = 0

for i in range(0,quant,1):
    lista.append(int(input('Digite o elemento: ')))
for i in range(0,quant,1):
    if lista[i]%2==0:
         sompar += lista[i]
         qpar +=1
    else :
        somimpar += 1
        qimpar += lista[i]

print(somimpar)
print(sompar)
print(qimpar)
print(qpar)
print(lista)