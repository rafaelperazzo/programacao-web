# -*- coding: utf-8 -*-
n=int(input('Digite um número com 8 dígitos:'))
soma=0
if (n<10000000):
    print('NAO SEI')
else:
    while n>0:
        resto=n%10
        n=((n-resto)/10)
        soma=soma+resto
        print('A soma dos algarismos é:')
        