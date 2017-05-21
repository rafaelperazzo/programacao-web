# -*- coding: utf-8 -*-
n=int(input('Digite a quantidade de pessoas: '))
soma=0
for i in range(1,n+1,1):
    idade=int(input('Digite a idade: '))
    soma=idade+idade
m=soma/n    
print('%.2f'%m)
    