# -*- coding: utf-8 -*-
n=int(input('Digite um número com 8 dígitos:'))
soma=0
if (n<10000000):
    print('NAO SEI')
else:
    soma=0
    aux=num
    while (aux>0):
        soma+=aux%10
        aux=int(aux/10)
        print('soma')