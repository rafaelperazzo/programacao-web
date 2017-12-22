# -*- coding: utf-8 -*-
a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
da = 0
db = 0
while a >= 1:
    da = da + 1
    a = a//100
while b > 0:
    db = db + 1
    b = b//10000
print('Quantidade de digitos de a: %d' %da)
print('Quantidade de digitos de b: %d' %db)