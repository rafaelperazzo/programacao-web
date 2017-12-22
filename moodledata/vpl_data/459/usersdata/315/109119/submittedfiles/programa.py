# -*- coding: utf-8 -*-
c = int(input('Quantdade de pedidos: '))
soma = 0
lista = []
for i in range (c):
    a = int(input('comprimento do taco: '))
    if a in lista:
        lista.remove(a)
    else:
        soma+=2
        lista.append(a)
print(soma)