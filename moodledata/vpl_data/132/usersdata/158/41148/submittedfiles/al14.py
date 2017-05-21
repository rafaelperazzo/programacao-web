# -*- coding: utf-8 -*-
q=int(input('digite quantidade de pessoas:'))
soma=0
for i in range(1,q+1,1):
    a=int(input('digite idade:'))
    soma=soma+a
media=soma/q
print('media:%.2f' %media)


