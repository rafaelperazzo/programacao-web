# -*- coding: utf-8 -*-
n=int(input('Quantidade de pessoas:'))
soma=0
for i in range(1,n+1,1):
    idade=int(input("%dª Idade:"%i))
    soma=soma+idade
media=soma/n
print('%.2f'%media)