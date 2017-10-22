# -*- coding: utf-8 -*-
n = int(input("digite um numero com 8 algarismos:  "))
soma = 0
while n < 100000000 and n > 999999999:
    resto = n % 10
    n = (n - resto)/10
    soma = soma + resto
    print ('%d' % soma)
while n > 100000000 and n < 99999999:
    print('NAO SEI')
    




