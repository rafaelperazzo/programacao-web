# -*- coding: utf-8 -*-
n = int(input("digite um numero com 8 algarismos:  "))
soma = 0
while True:
    if n < 10000000 and n > 9999999:
        resto = n % 10
        n = (n - resto)/10
        soma = soma + resto
        break
    print ('%d' % soma)
else:
    print("NAO SEI")



