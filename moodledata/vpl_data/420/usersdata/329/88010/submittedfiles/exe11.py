# -*- coding: utf-8 -*-
n = int(input("digite um numero com 8 algarismos:  "))
soma = 0
while n !=0:
    resto = n % 10
    n = (n - resto)/10
    soma = soma + resto
    print ('%d' % soma)




