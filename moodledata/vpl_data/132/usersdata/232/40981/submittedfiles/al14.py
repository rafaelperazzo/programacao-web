# -*- coding: utf-8 -*-
soma=0
n=int(input('Digite a quantidade de pessoas: '))
for i in range (1,n+1,1):
    idade=int(input('Digite a idade: '))
    soma=soma+idade
media=soma/n
print(media)