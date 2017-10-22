# -*- coding: utf-8 -*-
n=input('Digite um número inteiro: ')
if (n>=10000000 and n<=99999999) :
    print(sum(int(i) for i in n))
else :
    print('NAO SEI')