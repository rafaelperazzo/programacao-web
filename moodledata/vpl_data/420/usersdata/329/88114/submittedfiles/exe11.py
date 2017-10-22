# -*- coding: utf-8 -*-
n = int(input("digite um numero com 8 algarismos:  "))
soma = 0
while soma < 72 :
    resto = n % 10
    n = (n - resto)/10
    soma = soma + resto
    print ('%d' % soma)
    break
    while soma > 1:
        resto = n % 10
        n = (n - resto)/10
        soma = soma + resto
        print ('%d' % soma)
        while soma > 72:
            print('NAO SEI')
            while n < 1:
                print('NAO SEI')
                
    




