# -*- coding: utf-8 -*-
c = int(input('informe a quantidade de pedidos: '))
soma = 0
lista = []
for i in range (c):
    a = int(input('comprimento do t: '))
    if a in lista:
        lista.remove(a)
    else:
        soma = soma + 2
        lista.append(a)
print(soma)
