# -*- coding: utf-8 -*-
a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
da = 0
db = 0
while a >= da:
    da = da + 1
    a = a//100
while b > db:
    db = db + 1
    b = b//10000
print('Quantidade de digitos de a: %d' %da)
print('Quantidade de digitos de b: %d' %db)