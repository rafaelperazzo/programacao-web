# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n = int(input('Digite a quantidade de elementos: '))
a = []
for i in range(0,n,1):
    a.append (int(input('Digite um valor: ')))
for i in range(0,n,1):
    if a[i]%2 == 0:
        print(a[i])