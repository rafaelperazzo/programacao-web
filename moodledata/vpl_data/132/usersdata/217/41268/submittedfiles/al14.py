# -*- coding: utf-8 -*-
n=int(input('digite o número de pessoas:'))
cont=1
idade=0
for i in range(cont,n+1,1):
    id=float(input('digite a idade:'))
    idade=idade+id
m=idade/n
print('%.2f'%m)
