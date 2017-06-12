# -*- coding: utf-8 -*-
n=int(input('digite n:'))
soma=0
for i in range(0,n,1):
    a=int(input('digite idade:'))
    soma=soma+a
media=soma/n
print('%.4f'%media)
