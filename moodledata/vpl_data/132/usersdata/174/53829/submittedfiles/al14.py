# -*- coding: utf-8 -*-
n=int(input('Quantidade de pessoas:'))
soma=0
for i in range(1,n+1,n):
    idade=int(input("Idade %d:"%i))
    soma=soma+idade
media=soma/n
print('%.2f'%media)