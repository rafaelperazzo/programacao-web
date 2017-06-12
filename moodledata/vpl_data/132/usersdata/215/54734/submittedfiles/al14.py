# -*- coding: utf-8 -*-
n=int(input('digiten:'))
soma=0
for i in range(0,n,1):
    a=int(input('digite idade:'))
    soma=soma+a
media=soma/n
print('%.2f'%media)
