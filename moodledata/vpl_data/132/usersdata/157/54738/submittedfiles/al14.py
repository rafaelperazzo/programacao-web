# -*- coding: utf-8 -*-
n=int(input('Quantidade de pessoas?: '))
soma=0
for i in range (0,n,1):
    idade=int(input('Qual idade das pessoas?: '))
    soma=soma+idade
media=soma/n
print(media)