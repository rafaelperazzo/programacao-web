# -*- coding: utf-8 -*-
quant = int(input('Quantos elementos você quer? '))
sompar = 0
somimpar = 0
qpar = 0
qimpar = 0

lista = []
for i in range(0,quant,1):
    lista.append(input('Digite o elemento: '))
 for i in range(0,quant,1):
     if lista[i]%2==0:
         sompar += lista[i]
         qpar +=1
    else :
        somimpar += 1
        qimpar += lista[i]

print(sompar)
print(somimpar)
print(qpar)
print(qimpar)