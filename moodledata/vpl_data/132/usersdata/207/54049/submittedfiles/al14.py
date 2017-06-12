# -*- coding: utf-8 -*-
n=int(input('escreva n:'))
soma=0
for i in range(0,n,1):
    a=int(input('escreva a idade:'))
    soma=soma+a
media=soma/n
print('%.2f'%media)