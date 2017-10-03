# -*- coding: utf-8 -*-

n = float(input('Valor do produto: '))
x = int(input('Digite forma de pagamento: ))

valor1 = n-(n*(15/100))
valor2 = n-(n*(10/100))
valor3 = n
valor4 = n+(n*(10/100))

if x == 1:
    print('%.2f' % valor1)
if x == 2:
    print('%.2f' % valor2)
if x == 3:
    print('%.2f' % valor3)
if x == 4:
    print('%.2f' % valor4)