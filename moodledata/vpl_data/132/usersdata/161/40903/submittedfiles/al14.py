# -*- coding: utf-8 -*-
n=int(input('Informe a quantidade de pessoas:'))
soma=0
for i in range(1,n+1,1):
    x=int(input('Informe a idade:'))
    soma=soma+x
    média=(soma/n)
print('%.2f' %média)    