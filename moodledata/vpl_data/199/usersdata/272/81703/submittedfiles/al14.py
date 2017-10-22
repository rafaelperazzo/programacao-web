# -*- coding: utf-8 -*-

n= int(input('Digite o valor de n: '))
cont=0
soma=0
while(cont<=n):
    i=int(input('Digite o valor da idade:'))
    soma=soma+i
    cont=cont+1
media=soma/n
print('%.2f' %media)