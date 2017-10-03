# -*- coding: utf-8 -*-
#Entrada
v = int(input('Digite a condição do pagamento do produto que custa R$500.00: '))
1 = 500.00 - (500.00*0.15)
2 = 500.00 - (500.00*0.10)
3 = 500.00
4 = 500.00 + (500.00*0.10)
if v == 1:
    print('O valor do produto, com 15% de desconto, é: R${}'.format(1))
if v == 2:
    print('O valor do produto, com 10% de desconto, é: R${}'.format(2))
if v == 3:
    print('O valor total do produto, quando parcelado em duas vezes, é R${}'.format(3))
if v == 4:
    print('O valor do produto, quando parcelado em duas vezes, é R${}'.format(4))
    

