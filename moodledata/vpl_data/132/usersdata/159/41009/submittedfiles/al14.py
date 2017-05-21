# -*- coding: utf-8 -*-
n=int(input('Quantidade de pessoas:'))
soma=0
for i in range (1,n+1,1):
    x=int(input('Digite a idade:'))
    soma=soma+x
m=soma/n
print('A média é: %.5f' %m)