# -*- coding: utf-8 -*-

'FORMA DE PAGAMENTO'
'1 - Á vista em dinheiro ou cheque, desconto de 15%'
'2 - Á vista em cartão de crédito, desconto de 10%'
'3 - Em duas vezes, sem juros'
'4 - Em duas vezes, com juros de 10%'
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