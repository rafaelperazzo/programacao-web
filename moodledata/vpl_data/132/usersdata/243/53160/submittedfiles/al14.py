# -*- coding: utf-8 -*-

n=int(input('digite a quantidade de pessoas:'))
i=0
soma=0
for i in range(1,n+1,1):
    idade=int(input('digite a idade:'))
    soma=soma+idade
media=soma/n
print('%.2f'%media)


