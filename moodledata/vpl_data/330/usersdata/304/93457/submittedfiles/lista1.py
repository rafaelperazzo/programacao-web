# -*- coding: utf-8 -*-
n = int(input('Digite n: '))
a = []
for i in range (0,n,1):
    a.append(int(input('Digite um valor: ')))
soma = 0
if a[i] % 2 == 0:
    soma = soma + a[i]
print(soma)

