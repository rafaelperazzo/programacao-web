# -*- coding: utf-8 -*-
n = int(input("digite um numero com 8 algarismos:  "))
soma = 0
while n < 72 :
    resto = n % 10
    n = (n - resto)/10
    soma = soma + resto
    print ('%d' % soma)
    break
    while n > 1:
        resto = n % 10
        n = (n - resto)/10
        soma = soma + resto
        print ('%d' % soma)
        while n > 72:
            print('NAO SEI')
            while n < 1:
                print('NAO SEI')
                
    




