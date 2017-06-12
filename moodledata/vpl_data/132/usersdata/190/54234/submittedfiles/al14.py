# -*- coding: utf-8 -*-
n=int(input('número de pessoas: '))
soma=0
for i in range(1,n+1,1):
    idade=int(input('digite a idade: '))
    soma=soma+idade
    m=soma/n
print('%.2f'%m)
    
