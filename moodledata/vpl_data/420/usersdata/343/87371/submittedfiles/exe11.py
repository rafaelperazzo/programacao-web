# -*- coding: utf-8 -*-
n=input('Digite um número inteiro: ')

while (True) :
    if (n>=10000000 and n<=99999999) :
        print(sum(int(n)))
        break
    else :
        print('NAO SEI')
        break