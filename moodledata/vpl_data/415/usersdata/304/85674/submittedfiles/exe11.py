# -*- coding: utf-8 -*-
n = int(input('n: '))
soma = 0
if (10000000 <= n and n <= 99999999):
    while not (n==0):
        resto = n % 10
        n = (n - resto)//10
        soma = soma + resto
    print (soma)
else:
    print('NAO SEI')