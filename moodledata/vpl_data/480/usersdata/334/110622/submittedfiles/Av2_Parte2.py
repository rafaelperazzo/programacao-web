# -*- coding: utf-8 -*-
x = int(input('Digite um número: '))

soma = 0
while (True):
    if x!=0:
        soma = soma + x%10
        x = x//10
    else:
        break

print(soma)