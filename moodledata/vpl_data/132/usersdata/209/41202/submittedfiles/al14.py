# -*- coding: utf-8 -*-
n=int(input('Pessoas:'))
soma=0
for i in range (1,n+1,1):
    x:int(input('Idade:'))
    soma=soma+x
media=soma/n
print('%.2f'%media)
    