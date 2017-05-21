# -*- coding: utf-8 -*-
n=int(input('Digite o numero de pessoas:'))
soma=0
for i in range (1,n+1,1):
    i=int(input('Digite a idade:'))
    soma=soma+i
    Med=(soma/n)
print('%.2f' %Med)

