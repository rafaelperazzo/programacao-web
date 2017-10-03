# -*- coding: utf-8 -*-
#Entrada
v = int(input('Digite a condição do pagamento do produto que custa R$500.00: '))
c1 = 500.00 - (500.00*0.15)
c2 = 500.00 - (500.00*0.10)
c3 = 500.00
c4 = 500.00 + (500.00*0.10)
if v == c1:
    print('O valor do produto, com 15% de desconto, é: R${}'.format(c1))
if v == c2:
    print('O valor do produto, com 10% de desconto, é: R${}'.format(2))
if v == c3:
    print('O valor total do produto, quando parcelado em duas vezes, é R${}'.format(c3))
if v == c4:
    print('O valor do produto, quando parcelado em duas vezes, é R${}'.format(c4))
    

