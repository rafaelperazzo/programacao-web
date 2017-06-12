# -*- coding: utf-8 -*-
n=int(input('digite n:'))
soma=0
for i in range(0,n,1):
    b=int(input('digite a idade:'))
    soma=soma+b
media=soma/n
print('%.2f'%media)