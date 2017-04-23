# -*- coding: utf-8 -*-
n = int(input('Insira um numero inteiro qualquer: '))
i = 1
fatorial = 1

while i<=n:
    fatorial = fatorial*i
    i = i+1
print('%d'%fatorial)    