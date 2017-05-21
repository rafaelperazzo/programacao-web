# -*- coding: utf-8 -*-
a=int(input('digite a quantidade de pessoas:'))
soma=0
for i in range(1,a+1,1):
    b=int(input('digite a idade de cada pessoa:'))
    soma=soma+b
media=soma/a
print(media'%.2f'%media)