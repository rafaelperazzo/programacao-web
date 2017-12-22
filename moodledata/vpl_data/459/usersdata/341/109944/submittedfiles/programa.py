# -*- coding: utf-8 -*-
c = int(input('Quantidade de pedidos: '))
soma = 0 
lista = []
for i in range (c):
    a = int(input('Comprimento do taco: '))
    if a in lista:
        lista.remove(a)
    else:
        soma+=2
        lista.append(a)
print(soma)

