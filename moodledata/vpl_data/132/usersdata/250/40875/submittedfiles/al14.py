# -*- coding: utf-8 -*-
n=int(input('quantidade de pessoas:'))
i=1
soma=0
while i<=n:
    idade=int(input('idade:'))
    soma=soma+idade
    media=soma/n
    i=i+1
print('%d'%media)