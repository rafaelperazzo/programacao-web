# -*- coding: utf-8 -*-
n=int(input('Digite número de pessoas que deseja calcular média: '))
soma=0
for i in range(0,n,1):
    idade=int(input('Digite idades: '))
    soma=soma+idade
media=soma/n
print(media)