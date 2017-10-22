# -*- coding: utf-8 -*-

n = int (input('Digite a quantidade de pessoas: '))
contador = 1
soma = 0

while (contador<=n):
    idade = int(input('Digite a idade:'))
    soma = soma + idade
    contador = contador + 1

media = soma/n
print('%.2f' %media)
    
