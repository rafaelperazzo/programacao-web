# -*- coding: utf-8 -*-

n = float(input('Valor do produto: '))
x = int(input('Digite forma de pagamento: '))

_1 = n-(n*(15/100))
_2 = n-(n*(10/100))
_3 = n
_4 = n+(n*(10/100))

if x == 1:
    print('%.2f' % _1)
if x == 2:
    print('%.2f' % _2)
if x == 3:
    print('%.2f' % _3)
if x == 4:
    print('%.2f' % _4)
if x > 4 or x <1:
    print('Nâo existe esta forma de pagamento')