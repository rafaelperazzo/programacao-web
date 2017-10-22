# -*- coding: utf-8 -*-
n = int(input('Digite seu numero: '))
soma = 0
while (n>0):
    resto = n%10
    n = (n-resto)/10
    soma += resto
print(soma)
