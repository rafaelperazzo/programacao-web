# -*- coding: utf-8 -*-

n=int(input('Digite o numero de pessoas:'))
soma=0
i=n
media=soma/i
while n>0:
    a=int(input('Digite o valor da idade:'))
    soma=soma+a
    n=n-1
print('%.2f'%media)