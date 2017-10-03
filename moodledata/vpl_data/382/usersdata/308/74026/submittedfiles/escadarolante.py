# -*- coding: utf-8 -*-
i = 1
total = 0
limanterior = 0

np = int(input('Numero de pessoas: '))

while i <= np
    atual = int(input('Instante: '))
    total = total +10
    if atual < limanterior:
        total = total - (limanterior - atual)
    limanterior = atual + 10
    i += 1

print (total)