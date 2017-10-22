# -*- coding: utf-8 -*-

n=int(input('Digite o numero de pessoas:'))
soma=0
i=1
while n>0:
    a=int(input('Digite o valor da idade:'))
    media=(soma/i)
    soma=soma+a
    i=i+1
print('%.2f'%media)