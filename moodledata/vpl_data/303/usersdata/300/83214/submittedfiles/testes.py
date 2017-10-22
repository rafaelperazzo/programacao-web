# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n = int(input('Insira o valor de n: '))
x = 1
while n > 0:
    x = x*(n*(n-1))
    n = n-1
print(x)    