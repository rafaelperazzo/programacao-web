# -*- coding: utf-8 -*-
n=int(input('digite o número de pessoas a qual vc desejar realizar a média das idades:'))
cont=0
soma=0
while cont < n:
    id=int(input('digite uma idade:'))
    soma=soma+id
    cont=cont+1
med=soma/n
print('%.2f'%med)